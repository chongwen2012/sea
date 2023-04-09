import win32gui
from PIL import ImageGrab
import cv2
import numpy as np
import pyautogui
import time
import pydirectinput




def capture_window(window_title):
    # 获取窗口句柄
    hwnd = win32gui.FindWindow(None, window_title)

    # 获取窗口位置和大小
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)

    # 捕获窗口截图
    bbox = (left, top, right, bottom)
    print(bbox)
    # 将窗口激活到前台
    # win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 还原窗口
    # win32gui.SetForegroundWindow(hwnd)  # 将窗口置于顶层
    return bbox
    #image = ImageGrab.grab(bbox)

    # 将截图保存到文件
    #image.save('screenshot.png')


# 根据颜色来获取位置并单击
def find_target_area(bbox, lower_color, upper_color):
    # 捕获屏幕区域
    screen = np.array(ImageGrab.grab(bbox))

    # 将图像从BGR颜色空间转换为HSV颜色空间
    hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)

    # 创建蒙版，检测指定颜色范围内的像素
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # 查找边界
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 获取最大边界的外接矩形
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        # return calculate_center(x, y, w, h)        
        # point=calculate_center(x, y, w, h)
        pyautogui.click(x=x,y=y)
    else:
        print('未找到')


# 计算中心点
def calculate_center(x, y, w, h):
    center_x = x + w//2
    center_y = y + h//2
    return center_x, center_y


def find_target_by_img(bbox,img,clickTimes=1,Deviation=0):    
    location=pyautogui.locateCenterOnScreen(img,confidence=0.6,region=bbox)
    if location is not None:
        try:
            pyautogui.click(location.x+Deviation,location.y+Deviation,clicks=clickTimes,interval=1,duration=0.2,button='left')   
        except pyautogui.FailSafeException as e:
            print(e) 
        # pyautogui.moveTo(location.x, location.y)
        # pydirectinput.mouseDown()
        # time.sleep(0.5)
        # pydirectinput.mouseUp()        
    else:    
        print("未找到匹配图片,0.1秒后重试")
    # time.sleep(0.1) 


if __name__ == '__main__':
    window_title = "海之乐章-重启 V1.60.01A  (Build:Apr  4 2023,10:50:20)"
    # window_title = "Spotify Premium"
    # 获取到窗口的位置
    bbox = capture_window(window_title)
    # 传入港口工人的颜色和窗口范围
    # lower_color=np.array([40,40,248])
    # upper_color=np.array([40,40,248])
    # find_target_area(bbox,lower_color,upper_color)   
    img='1.png'
    find_target_by_img(bbox,img)
    img2='2.png'
    find_target_by_img(bbox,img2)
    img3='3.png'
    find_target_by_img(bbox,img3,4)
    img4='4.png'
    find_target_by_img(bbox,img4)
    find_target_by_img(bbox,img)
    img5='5.png'
    find_target_by_img(bbox,img5)
    img6='6.png'
    time.sleep(12)
    find_target_by_img(bbox,img6,Deviation=-70)
    img7='7.png'
    time.sleep(1)
    find_target_by_img(bbox,img7)