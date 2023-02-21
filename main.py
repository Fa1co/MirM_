# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import ctypes

import time

import cv2 as cv
import win32api
import win32con
import win32gui
from datetime import datetime
from PIL import ImageGrab
import numpy as np
import pyautogui

# window name
WINDOW_SUBSTRING = "MIRMG(2)"

class ObjectDetection:
    @staticmethod
    def get_window_info():
        #установка информации о окне

        window_info = {}

        user32 = ctypes.windll.user32

        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)  # получени высоты и ширины монитора
        win32gui.EnumWindows(ObjectDetection.set_window_coordinates, window_info)
        return window_info

    @staticmethod
    #get information about albion online client
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
    def find_pickaxe(template_path):
        # get information about albion online client (screen width, height)
        window_info = ObjectDetection.get_window_info()
        # make  rgb screenshot of location
        img_rgb = cv.cvtColor(ObjectDetection.get_screen(window_info.get('x'), window_info.get('x'), window_info.get('width'), window_info.get('height')), cv.COLOR_BGR2RGB)
        # transformation inage from rgb to gray
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        # open template and get information about width and height
        template = cv.imread(template_path, 0)
        w, h = template.shape[::-1]
        # find x and y coordinates from gray image using template and cv.TM_CCOEFF_NORMED
        res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
        # level of threshold
        threshold = 0.8
        # coordinates which more than level of threshold
        loc = np.where(res >= threshold)

        if len(loc[0]) > 0:
            return loc[1][0], loc[0][0]
        else:
            return loc



def repair_fishing_rod(flag):
    if flag:
        while True:
            try:
                broken_item_cords = ObjectDetection.find_pickaxe('./fishing/broken_item_icon.jpg')
                
                if broken_item_cords[0] > 0 and broken_item_cords[1] > 0:
                    flag = False
                    return flag
            except:
                print("Проблема с поиском кнопки сломанный предмет")

    elif not flag:
        ObjectDetection.get_window_info()
        time.sleep(1)
        pyautogui.press("i")
        time.sleep(1)
        while True:
            try:
                repair_icon_cords = ObjectDetection.find_pickaxe('./fishing/repair_icon.jpg')
                if repair_icon_cords[0] > 0 and repair_icon_cords[1] > 0:
                    pyautogui.click(x=repair_icon_cords[0] + 15, y=repair_icon_cords[1] + 5, duration=0.6, button='left')
                    break
            except:
                print("Проблема с repair_icon")

        while True:
            try:
                move_to_cords = ObjectDetection.find_pickaxe('./fishing/moveTo_2.jpg')
                print(move_to_cords)
                if move_to_cords[0] > 0 and move_to_cords[1] > 0:
                    pyautogui.click(x=move_to_cords[0]+80, y=move_to_cords[1]+15, duration=0.6, button='left')
                    break
            except:
                print("Проблема с moveTo")
        pyautogui.press('i')
        while True:
            try:
                repair_equip_cords = ObjectDetection.find_pickaxe('./fishing/rep_equip.jpg')
                if repair_equip_cords[0] > 0 and repair_equip_cords[1] > 0:
                    pyautogui.click(x=repair_equip_cords[0], y=repair_equip_cords[1], duration=0.6, button='left')
                    break
            except:
                pass
            time.sleep(0.5)

        while True:
            try:
                repair_all_cords = ObjectDetection.find_pickaxe('./fishing/repair_all.jpg')
                if repair_all_cords[0] > 0 and repair_all_cords[1] > 0:
                    pyautogui.click(x=repair_all_cords[0], y=repair_all_cords[1], duration=0.6, button='left')
                    break
            except:
                print("Проблема с поиском ремонта всего 1")
        while True:
            try:
                repair_all_cords = ObjectDetection.find_pickaxe('./fishing/repair_all_2.jpg')
                if repair_all_cords[0] > 0 and repair_all_cords[1] > 0:
                    pyautogui.click(x=repair_all_cords[0]+20, y=repair_all_cords[1]+20, duration=0.6, button='left')
                    break
            except:
                print("Проблема с поиском ремонта всего 2")
        time.sleep(1)
        pyautogui.press('M')
        time.sleep(1.5)
        pyautogui.press('esc')
        while True:
            try:
                repair_all_cords = ObjectDetection.find_pickaxe('./fishing/close_icon.jpg')
                if repair_all_cords[0] > 0 and repair_all_cords[1] > 0:
                    pyautogui.click(x=repair_all_cords[0]+20, y=repair_all_cords[1]+20, duration=0.6, button='left')
                    break
            except:
                print("Проблема с поиском кнопки закрыть")
        # while True:
        #     try:
        #         zone_cords = ObjectDetection.find_pickaxe('./fishing/save_zone.jpg')
        #         if zone_cords[0] > 0 and zone_cords[1] > 0:
        #             pyautogui.click(x=zone_cords[0]+50, y=zone_cords[1]+50, duration=0.6, button='left')
        #             break
        #     except:
        #         print("Проблема с поиском карты")
        time.sleep(0.5)
        pyautogui.press('m')

        while True:
            try:
                resource_cords = ObjectDetection.find_pickaxe('./fishing/res.jpg')
                if resource_cords[0] > 0 and resource_cords[1] > 0:
                    pyautogui.click(x=resource_cords[0]+10, y=resource_cords[1]+10, duration=0.6, button='left')
                    break
            except:
                print("Проблема с поиском кнопки ресурсы")

        while True:
            try:
                resource_cords = ObjectDetection.find_pickaxe('./fishing/fish.jpg')
                if resource_cords[0] > 0 and resource_cords[1] > 0:
                    pyautogui.click(x=resource_cords[0] + 10, y=resource_cords[1] + 10, duration=0.6, button='left')
                    break
            except:
                print("Проблема с поиском кнопки рыбалки")

        while True:
            try:
                auto_move_cords = ObjectDetection.find_pickaxe('./fishing/teleport.jpg')
                if auto_move_cords[0] > 0 and auto_move_cords[1] > 0:
                    pyautogui.click(x=auto_move_cords[0] + 10, y=auto_move_cords[1] + 10, duration=0.6, button='left')
                    break
            except:
                print("Проблема с поиском кнопки автоперемещение")

        while True:
            try:
                auto_move_cords = ObjectDetection.find_pickaxe('./fishing/goTo.jpg')
                if auto_move_cords[0] > 0 and auto_move_cords[1] > 0:
                    pyautogui.click(x=auto_move_cords[0] + 10, y=auto_move_cords[1] + 10, duration=0.6, button='left')
                    break
            except:
                print("Проблема с поиском кнопки автоперемещение")

        while True:
            try:
                fishing_icon_cords = ObjectDetection.find_pickaxe('./fishing/fish_icon.jpg')
                print(fishing_icon_cords)
                if fishing_icon_cords[0] > 0 and fishing_icon_cords[1] > 0:
                    pyautogui.click(x=fishing_icon_cords[0] + 20, y=fishing_icon_cords[1] + 20, duration=0.6, button='left')
                    flag = True
                    return flag

            except:
                print("Проблема с поиском кнопки рыбалки")

            time.sleep(0.5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    status = 1
    flag = False
    while True:
        flag = repair_fishing_rod(flag)
