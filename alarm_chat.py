
import pyautogui
import time
position = pyautogui.position()
pesan = "Test Alarm Spam In WA with Phyton"
for i in range(30):
    pyautogui.click(position.x, position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(0.5)
    pyautogui.typewrite(["enter"])
