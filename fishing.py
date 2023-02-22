import pyautogui
import ctypes
import time
from object_detection import *


class Fishing:
    @staticmethod
    # Основной метод для рыбалки:
    # Открывает карту и переходит на место рыбалки
    # Забрасывает удочку и проверяет прочность предмета, если прочность < 30 % идет ремонтировать
    def fishing_bot(flag, window_name):
        WINDOW_SUBSTRING = window_name
        if flag:
            while True:
                try:
                    broken_item_cords = ObjectDetection.find_pickaxe('./fishing/broken_item_icon1.jpg')

                    if broken_item_cords[0] > 0 and broken_item_cords[1] > 0:
                        print(broken_item_cords)
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
                        pyautogui.click(x=repair_icon_cords[0] + 15, y=repair_icon_cords[1] + 5, duration=0.6,
                                        button='left')
                        break
                except:
                    print("Проблема с repair_icon")

            while True:
                try:
                    move_to_cords = ObjectDetection.find_pickaxe('./fishing/moveTo_2.jpg')
                    print(move_to_cords)
                    if move_to_cords[0] > 0 and move_to_cords[1] > 0:
                        pyautogui.click(x=move_to_cords[0] + 80, y=move_to_cords[1] + 15, duration=0.6, button='left')
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
                    repair_all_cords = ObjectDetection.find_pickaxe('./fishing/close_icon.jpg')
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
                    resource_cords = ObjectDetection.find_pickaxe('./fishing/res.jpg')
                    if resource_cords[0] > 0 and resource_cords[1] > 0:
                        pyautogui.click(x=resource_cords[0] + 10, y=resource_cords[1] + 10, duration=0.6, button='left')
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
                        pyautogui.click(x=auto_move_cords[0] + 10, y=auto_move_cords[1] + 10, duration=0.6,
                                        button='left')
                        break
                except:
                    print("Проблема с поиском кнопки автоперемещение")

            while True:
                try:
                    auto_move_cords = ObjectDetection.find_pickaxe('./fishing/goTo.jpg')
                    if auto_move_cords[0] > 0 and auto_move_cords[1] > 0:
                        pyautogui.click(x=auto_move_cords[0] + 10, y=auto_move_cords[1] + 10, duration=0.6,
                                        button='left')
                        break
                except:
                    print("Проблема с поиском кнопки автоперемещение")

            while True:
                try:
                    fishing_icon_cords = ObjectDetection.find_pickaxe('./fishing/fish_icon.jpg')
                    if fishing_icon_cords[0] > 0 and fishing_icon_cords[1] > 0:
                        pyautogui.click(x=fishing_icon_cords[0] + 20, y=fishing_icon_cords[1] + 20, duration=0.6,
                                        button='left')
                        flag = True
                        return flag

                except:
                    print("Проблема с поиском кнопки рыбалки")

                time.sleep(0.5)