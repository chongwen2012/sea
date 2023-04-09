import win32gui
from PIL import ImageGrab
import cv2
import numpy as np
import pyautogui
import pytesseract

def capture_window(window_title):
    # 获取窗口句柄
    hwnd = win32gui.FindWindow(None, window_title)

    # 获取窗口位置和大小
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)

    # 捕获窗口截图
    bbox = (left, top, right, bottom)
    print(bbox)
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


def find_target_by_img(bbox):
    # 读取屏幕截图和需要匹配的图片
    screen = np.array(ImageGrab.grab(bbox))
    template = cv2.imread("E:\python\sea\gkgr.png")

    # 将需要匹配的图片转为灰度图像
    gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # 使用模板匹配函数在屏幕截图中找到匹配的位置
    res = cv2.matchTemplate(screen, gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 根据匹配结果确定目标位置
    x, y = max_loc
    w, h = template.shape[1], template.shape[0]
    center_x, center_y = x + w//2, y + h//2
    pyautogui.click(x=center_x,y=center_y)

if __name__ == '__main__':
    window_title = "海之乐章-重启 V1.60.01A  (Build:Apr  4 2023,10:50:20)"
    # 获取到窗口的位置
    bbox = capture_window(window_title)
    # 传入港口工人的颜色和窗口范围
    # lower_color=np.array([40,40,248])
    # upper_color=np.array([40,40,248])
    # find_target_area(bbox,lower_color,upper_color)   
    find_target_by_img(bbox)