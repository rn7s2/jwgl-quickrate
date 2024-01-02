import random
import time

import pyautogui


def clickCourse():
    select = [1 for _ in range(12)]
    select[0] = 0
    select[1] = 0
    random.shuffle(select)

    for i, ploc, aloc in zip(
        range(12),
        pyautogui.locateAllOnScreen("perfect.png"),
        pyautogui.locateAllOnScreen("almost.png"),
    ):
        if select[i] == 1:
            pyautogui.leftClick(x=ploc[0] - 10, y=ploc[1] + 10)
        else:
            pyautogui.leftClick(x=aloc[0] - 10, y=aloc[1] + 10)

    teacher = pyautogui.locateAllOnScreen("teacher.png")
    for _ in range(3):
        pos = teacher.__next__()
        pyautogui.leftClick(x=pos[0] - 10, y=pos[1] + 10)

    pyautogui.scroll(-1000)

    time.sleep(0.5)

    save = pyautogui.locateOnScreen("save.png")
    pyautogui.leftClick(x=save[0], y=save[1])


while True:
    try:
        clickCourse()
    except:
        pass
    time.sleep(3)
