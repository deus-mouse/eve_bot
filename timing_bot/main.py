# -*- coding: utf-8 -*-
# version Python 3.7.9

import pyautogui
from time import sleep

DELAY_BETWEEN_COMMANDS = 1.00


def main():
        initialize_pyautogui()
        countdown_timer()

        go_to_nearest_doc()

        # Ending Point: Docked at Earth Station.
        print('Done')


def initialize_pyautogui():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True


def countdown_timer():
    # Countdown timer
    print("Starting", end='')
    for i in range(0, 10):
        print(".", end='')
        sleep(1)
    print('Go')


def hold_key(key, seconds=1.00):
    pyautogui.keyDown(key)
    sleep(seconds)
    pyautogui.keyUp(key)
    sleep(DELAY_BETWEEN_COMMANDS)


def report_mouse_position(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        sleep(1)


def go_to_nearest_doc():
    pyautogui.moveTo(1318, 161, duration=0.25)
    sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    pyautogui.moveTo(1317, 204, duration=0.25)
    hold_key('d', 1.00)
    pyautogui.click()


if __name__ == "__main__":
    main()
