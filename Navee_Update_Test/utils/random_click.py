import time

import pyautogui
import random

def random_click():
    time.sleep(6)
    pyautogui.FAILSAFE = False  # 关闭 fail-safe（确保脚本不中断）
    screen_width, screen_height = pyautogui.size()

    # 避开四角
    x = random.randint(screen_width // 4, screen_width * 3 // 4)
    y = random.randint(screen_height // 4, screen_height * 3 // 4)

    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()
    print(f"随机点击位置：({x}, {y})")