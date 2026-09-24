import pyautogui
import keyboard
import time

pyautogui.PAUSE = 0
clicking = False


def toggle_clicking():
    global clicking
    clicking = not clicking
    print("Clicking:", clicking)


keyboard.add_hotkey("ü", toggle_clicking)

print("Press u to start/stop clicking. Press a to exit.")

while True:
    if clicking:
        pyautogui.click(button="left")
    if keyboard.is_pressed("ä"):
        break
    time.sleep(0.002)
