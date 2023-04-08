import win32gui


def print_window_titles(hwnd, window_list):
    if win32gui.IsWindowVisible(hwnd):
        window_list.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_window_text():
    # 获取当前激活窗口的标题
    # title = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    # print(title)

    windows = []
    win32gui.EnumWindows(print_window_titles, windows)
    for hwnd, title in windows:
        print(title)


if __name__ == '__main__':
    get_window_text()