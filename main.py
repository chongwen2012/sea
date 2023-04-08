import win32gui
from PIL import ImageGrab

def capture_window(window_title):
    # 获取窗口句柄
    hwnd = win32gui.FindWindow(None, window_title)

    # 获取窗口位置和大小
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)

    # 捕获窗口截图
    bbox = (left, top, right, bottom)
    image = ImageGrab.grab(bbox)

    # 将截图保存到文件
    image.save('screenshot.png')

if __name__ == '__main__':
    window_title = "窗口标题"
    capture_window('Python image capturing. - Google Chrome')
