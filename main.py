import win32gui
import cv2
import numpy as np
import pyautogui
import time
from PIL import ImageGrab 

WINDOW_TITLE = "海之乐章-重启 V1.60.01A  (Build:Apr  4 2023,10:50:20)"
TARGET_IMAGES = [
    ("1.png", 1, 0,0),
    ("2.png", 1, 0,0),
    ("3.png", 4, 0,0),
    ("4.png", 1, 0,0),
    ("1.png", 1, 0,0),
    ("5.png", 1, 0,0),
    ("6.png", 1, -70,12),
    ("7.png", 1, 0,0),
]
CONFIDENCE_LEVEL = 0.6
CLICK_INTERVAL = 1
CLICK_DURATION = 0.2


def capture_window(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    rect = win32gui.GetWindowRect(hwnd)
    return rect


def find_target(rect, target, click_times=1, deviation=0,waiting_time=0):
    time.sleep(waiting_time)
    if isinstance(target, np.ndarray):
        image = target
    else:
        image = cv2.imread(target, cv2.IMREAD_COLOR)

    result = pyautogui.locateCenterOnScreen(image, confidence=CONFIDENCE_LEVEL, region=rect)
    if result is not None:
        try:
            pyautogui.click(
                x=result.x + deviation,
                y=result.y + deviation,
                clicks=click_times,
                interval=CLICK_INTERVAL,
                duration=CLICK_DURATION,
                button="left",
            )
        except pyautogui.FailSafeException as e:
            print(e)
    else:
        print(f"未找到匹配图片 {target}，0.1秒后重试")
        time.sleep(0.1)

from PIL import ImageGrab


def find_pixel_location(color, region=None):
    im = ImageGrab.grab()
    width, height = im.size
    if region is None:
        region = (0, 0, width, height)
    for x in range(region[0], region[2]):
        for y in range(region[1], region[3]):
            if im.getpixel((x, y)) == color:
                return (x, y)
    return None


if __name__ == "__main__":
    # with ImageGrab.grab() as _:
    #     window_rect = capture_window(WINDOW_TITLE)
    color=(185,227,117)
    regin=find_pixel_location(color)
    if regin is not None:
        pyautogui.moveTo(regin)
        pyautogui.click()
    else:
        print('未找到')
    # for target_image, click_times, deviation,waiting_time in TARGET_IMAGES:
    #     find_target(window_rect, target_image, click_times, deviation , waiting_time)
