import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()    # get the size of the PRIMARY monitor

time.sleep(3)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
