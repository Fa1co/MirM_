import pyautogui
import ctypes
import time
import cv2 as cv

import object_detection
from object_detection import *




class Fishing:


    @staticmethod
    # Основной метод для рыбалки:
    # Открывает карту и переходит на место рыбалки
    # Забрасывает удочку и проверяет прочность предмета, если прочность < 30 % идет ремонтировать
    def fishing_bot(flag, window_name):
        try:
            objectDetection = ObjectDetection()
            objectDetection.set_window_substring(window_name)
        except:
            pass

        if flag:
            while True:
                try:
                    smith_cords = objectDetection.find_object("./fishing/broken_item.jpg", threshold=0.85)
                    if smith_cords[0] > 0 and smith_cords[1] > 0:
                        flag = False
                        return flag
                except:
                    print("Проблема с поиском кнопки сломанный предмет")

        elif not flag:
            objectDetection.get_window_info()
            time.sleep(1)
            pyautogui.press("i")
            while True:
                try:
                    repair_icon_cords = objectDetection.find_object('./fishing/repair_icon.jpg')
                    if repair_icon_cords[0] > 0 and repair_icon_cords[1] > 0:
                        pyautogui.click(x=repair_icon_cords[0] + 15, y=repair_icon_cords[1] + 5, duration=0.6,
                                        button='left')
                        break
                except:
                    print("Проблема с repair_icon")

            while True:
                try:
                    move_to_cords = objectDetection.find_object('./fishing/moveTo_2.jpg')
                    print(move_to_cords)
                    if move_to_cords[0] > 0 and move_to_cords[1] > 0:
                        pyautogui.click(x=move_to_cords[0] + 80, y=move_to_cords[1] + 15, duration=0.6, button='left')
                        break
                except:
                    print("Проблема с moveTo")
            time.sleep(1)
            pyautogui.press("i")

            while True:
                try:
                    repair_equip_cords = objectDetection.find_object('./fishing/rep_equip.jpg')
                    if repair_equip_cords[0] > 0 and repair_equip_cords[1] > 0:
                        pyautogui.click(x=repair_equip_cords[0], y=repair_equip_cords[1], duration=0.6, button='left')
                        break
                except:
                    pass
                time.sleep(0.5)

            while True:
                try:
                    repair_all_cords = objectDetection.find_object('./fishing/repair_all.jpg')
                    if repair_all_cords[0] > 0 and repair_all_cords[1] > 0:
                        pyautogui.click(x=repair_all_cords[0], y=repair_all_cords[1], duration=0.6, button='left')
                        break
                except:
                    print("Проблема с поиском ремонта всего 1")
            while True:
                try:
                    repair_all_cords = objectDetection.find_object('./fishing/repair_all_2.jpg')
                    if repair_all_cords[0] > 0 and repair_all_cords[1] > 0:
                        pyautogui.click(x=repair_all_cords[0] + 20, y=repair_all_cords[1] + 20, duration=0.6,
                                        button='left')
                        break
                except:
                    print("Проблема с поиском ремонта всего 2")
            time.sleep(1)
            pyautogui.press('M')
            time.sleep(1.5)
            pyautogui.press('esc')
            while True:
                try:
                    repair_all_cords = objectDetection.find_object('./fishing/close_icon.jpg')
                    if repair_all_cords[0] > 0 and repair_all_cords[1] > 0:
                        pyautogui.click(x=repair_all_cords[0] + 20, y=repair_all_cords[1] + 20, duration=0.6,
                                        button='left')
                        break
                except:
                    print("Проблема с поиском кнопки закрыть")

            time.sleep(0.5)
            pyautogui.press('m')

            while True:
                try:
                    resource_cords = objectDetection.find_object('./fishing/res.jpg')
                    if resource_cords[0] > 0 and resource_cords[1] > 0:
                        pyautogui.click(x=resource_cords[0] + 10, y=resource_cords[1] + 10, duration=0.6, button='left')
                        break
                except:
                    print("Проблема с поиском кнопки ресурсы")

            while True:
                try:
                    resource_cords = objectDetection.find_object('./fishing/fish.jpg')
                    if resource_cords[0] > 0 and resource_cords[1] > 0:
                        pyautogui.click(x=resource_cords[0] + 10, y=resource_cords[1] + 10, duration=0.6, button='left')
                        break
                except:
                    print("Проблема с поиском кнопки рыбалки")

            while True:
                try:
                    auto_move_cords = objectDetection.find_object('./fishing/teleport.jpg')
                    if auto_move_cords[0] > 0 and auto_move_cords[1] > 0:
                        pyautogui.click(x=auto_move_cords[0] + 10, y=auto_move_cords[1] + 10, duration=0.6,
                                        button='left')
                        break
                except:
                    print("Проблема с поиском кнопки автоперемещение")

            while True:
                try:
                    auto_move_cords = objectDetection.find_object('./fishing/goTo.jpg')
                    if auto_move_cords[0] > 0 and auto_move_cords[1] > 0:
                        pyautogui.click(x=auto_move_cords[0] + 10, y=auto_move_cords[1] + 10, duration=0.6,
                                        button='left')
                        break
                except:
                    print("Проблема с поиском кнопки автоперемещение")

            while True:
                try:
                    fishing_icon_cords = objectDetection.find_object('./fishing/fishing_icon.jpg')
                    if fishing_icon_cords[0] > 0 and fishing_icon_cords[1] > 0:
                        pyautogui.click(x=fishing_icon_cords[0], y=fishing_icon_cords[1], duration=0.6,
                                        button='left')
                        flag = True
                        return flag

                except:
                    print("Проблема с поиском кнопки рыбалки")

                time.sleep(0.5)

    def test_find_broke_item(self):
        objectDetection = ObjectDetection()
        while True:
            try:
                broke_item_cords = objectDetection.find_object("./fishing/test_fishing_icon/broken_item.jpg",
                                                               threshold=0.85)
                print(broke_item_cords)
                if broke_item_cords[0] > 0 or broke_item_cords[1] > 0:
                    pyautogui.moveTo(x=broke_item_cords[0], y=broke_item_cords[1], _pause=0.3)
            except:
                print("Error")
            time.sleep(1)

    def test_find_fishing_icon(self):
        objectDetection = ObjectDetection()
        while True:
            try:
                fishing_icon_cords = objectDetection.find_object("./fishing/test_fishing_icon/fishing_icon.jpg", threshold=0.85)
                print(fishing_icon_cords)
                if fishing_icon_cords[0] > 0 or fishing_icon_cords[1] > 0:
                    pyautogui.moveTo(x=fishing_icon_cords[0], y=fishing_icon_cords[1], _pause=0.3)
            except:
                print("Error")
            time.sleep(1)