import sys

import pyautogui

from fishing import *
import keyboard


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    status = 1
    flag = True
    fishing = Fishing()
    window_name = ""

    while True:
        choose_window = int(input("1) Окно игры MIRM(1)\n2) Окно игры MIRM(2)\n3)Выход из программы\nВыбор:"))
        if choose_window == 1:
            window_name = "MIRMG(1)"
            break
        elif choose_window == 2:
            window_name = "MIRMG(2)"
            break
        elif choose_window == 3:
            exit(0)


    while True:
        flag = fishing.fishing_bot(flag, window_name)