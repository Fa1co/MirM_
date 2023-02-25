import time

from fishing import *


if __name__ == '__main__':

    flag = True
    fishing = Fishing()
    window_name = "MIRMG(2)"

    # while True:
    #     choose_window = int(input("1) Окно игры MIRMG(1)\n2) Окно игры MIRMG(2)\n3)Выход из программы\nВыбор:"))
    #     if choose_window == 1:
    #         window_name = "MIRMG(1)"
    #         break
    #     elif choose_window == 2:
    #         window_name = "MIRMG(2)"
    #         break
    #     elif choose_window == 3:
    #         exit(0)


    while True:
        flag = fishing.fishing_bot(flag)
        time.sleep(1)
        # fishing.test_find_broke_item()