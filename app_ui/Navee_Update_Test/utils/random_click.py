import pyautogui
import random

def random_click():
    width, height = pyautogui.size()
    x = random.randint(width // 4, width * 3 // 4)
    y = random.randint(height // 4, height * 3 // 4)
    pyautogui.moveTo(x, y, duration=0.5)
    print(f"随机点击位置: ({x}, {y})")
