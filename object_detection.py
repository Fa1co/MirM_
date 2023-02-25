import ctypes
import cv2 as cv
import win32gui
import numpy as np
from PIL import ImageGrab

WINDOW_SUBSTRING = "MIRMG(2)"

class ObjectDetection:


    @staticmethod
    def get_window_info():

        window_info = {}

        user32 = ctypes.windll.user32

        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        win32gui.EnumWindows(ObjectDetection.set_window_coordinates, window_info)
        return window_info
    @staticmethod
    # get information about albion online client
    def set_window_coordinates(hwnd, window_info):
        if win32gui.IsWindowVisible(hwnd):
            if WINDOW_SUBSTRING in win32gui.GetWindowText(hwnd):
                rect = win32gui.GetWindowRect(hwnd)
                x = rect[0]
                y = rect[1]
                w = rect[2] - x
                h = rect[3] - y
                window_info['x'] = x
                window_info['y'] = y
                window_info['width'] = w
                window_info['height'] = h
                window_info['name'] = win32gui.GetWindowText(hwnd)
                win32gui.SetForegroundWindow(hwnd)

    @staticmethod
    # take img of albion online
    def get_screen(x1, y1, x2, y2):
        box = (x1, y1, x2, y2)
        screen = ImageGrab.grab(box)
        img = np.array(screen.getdata(), dtype=np.uint8).reshape((screen.size[1], screen.size[0], 3))

        return img

    @staticmethod
    def find_pickaxe(template_path, threshold=0.8, method=cv.TM_CCOEFF_NORMED):
        # get information about albion online client (screen width, height)
        window_info = ObjectDetection.get_window_info()
        # make  rgb screenshot of location
        img_rgb = cv.cvtColor(
            ObjectDetection.get_screen(window_info.get('x'), window_info.get('x'), window_info.get('width'),
                                       window_info.get('height')), cv.COLOR_BGR2RGB)
        # transformation inage from rgb to gray
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        # open template and get information about width and height
        template = cv.imread(template_path, 0)
        w, h = template.shape[::-1]
        # find x and y coordinates from gray image using template and cv.TM_CCOEFF_NORMED
        res = cv.matchTemplate(img_gray, template, method)
        # level of threshold
        # coordinates which more than level of threshold
        loc = np.where(res >= threshold)

        if len(loc[0]) > 0:
            return loc[1][0], loc[0][0]
        else:
            return loc
