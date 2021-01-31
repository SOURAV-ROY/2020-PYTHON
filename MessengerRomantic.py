import pyautogui
import time

message = 100
while message > 0:
    time.sleep(1)
    pyautogui.typewrite(' I Love You !!')
    # time.sleep(2)
    pyautogui.press('enter')
    message = message - 1
