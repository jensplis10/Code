import json
import pyautogui
import time
time.sleep(5)
xold = 1000
zold = 1000

with open(f"C:\\Users\\Jens\\AppData\\Roaming\\norisk\\NoRiskClientV3\\data\\profiles\\noriskclient\\new\\minescript\\minecraft-circle(1).json", "r", encoding="utf-8") as circledatei:
    data = json.load(circledatei)

for i in range(0,len(data)):
    x = data[i]["x"]
    z = data[i]["z"]
    if z != zold:
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite(f"//cyl iron_block {165-x}")
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.keyDown('space')
        time.sleep(0.2)
        pyautogui.keyUp('space')

    xold = x
    zold = z
