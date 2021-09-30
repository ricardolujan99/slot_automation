import pyautogui 
import cv2


def captura():
    screenshot = pyautogui.screenshot(region=(375, 300, 210, 150))
    screenshot.save("screenshot.png")



