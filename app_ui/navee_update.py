import os.path
import random

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from fromemail import Email
import pyautogui

# 配置参数
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '14',
    'deviceName': '5baa00a4',
    'appPackage': 'com.navee.ucaret',
    'appActivity': 'com.uz.navee.MainActivity',
    'automationName': 'UiAutomator2',
    'noReset': True,
    'disableWindowAnimation': False,
    'newCommandTimeout': 3600
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(20)
WebDriverWait(driver, timeout=10).until(
    EC.element_to_be_clickable((AppiumBy.ID, "com.navee.ucaret:id/button_toolbar"))).click()
res = driver.find_elements(AppiumBy.ID, 'com.navee.ucaret:id/subtitleLabel')

for i in res:
    print(i.text)
    if i.text == '10A5625B5823':
        i.click()
        break


def save_result_data():
    if os.path.exists('data.txt'):
        os.remove('data.txt')
    else:
        with open('data.txt', 'a') as f:
            f.write('')


def random_click():
    screen_width, screen_height = pyautogui.size()
    x = random.randint(screen_width // 4, screen_width * 3 // 4)
    y = random.randint(screen_height // 4, screen_height * 3 // 4)

    pyautogui.moveTo(x, y, duration=0.5)
    print(f"移动位置: ({x}, {y})")


def click_toolbar():
    time.sleep(5)
    driver.find_element(AppiumBy.ID, 'com.navee.ucaret:id/bluetoothStatusButton').click()
    print("点击蓝牙")
    time.sleep(5)
    WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.navee.ucaret:id/infoButton"))).click()
    print("车辆信息")
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH, "//*[@text='检查固件更新']").click()
    print("点击检查更新")
    time.sleep(5)


save_result_data()

try:
    click_toolbar()
    update = driver.find_element(AppiumBy.XPATH, "//*[@text='立马升级']")
    update.click()
    current_text = update.text  # 获取初始文本
    number, up_num = 0, 1
    # while number < 100:
    while True:
        update_button = driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.navee.ucaret:id/updateButton']")
        new_text = update_button.text  # 获取按钮最新文本
        if new_text == "重新升级":
            print(f"检测到文本变化: {current_text} → {new_text}")
            with open('data.txt', 'a') as f:
                f.write("第{}次升级失败\t时间为{}\n".format(up_num, time.strftime('%Y-%m-%d %H-%M-%S')))
                up_num += 1
            # driver.get_screenshot_as_file("第{}次失败\t时间为：{}.png".format(i, time.strftime('%Y-%m-%d %H-%M-%S')))
            # print("截图成功！")
            # i += 1
            update_button.click()
        if new_text == "确定":
            with open("data.txt", "a") as f:
                f.write("第{}次升级成功\t时间为{}\n".format(up_num, time.strftime('%Y-%m-%d %H-%M-%S')))
                print('升级成功！')
                up_num += 1
            time.sleep(5)
            WebDriverWait(driver, timeout=10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='确定']"))).click()
            print("点击确定")
            time.sleep(5)
            WebDriverWait(driver, timeout=10).until(
                EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.ImageButton"))).click()
            print("点击返回")
            click_toolbar()
            WebDriverWait(driver, timeout=10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='立马升级']"))).click()
            print("点击立马升级")
        number += 1
        random_click()
        time.sleep(3)  # 每3秒检查一次
except Exception as e:
    Email('Update_Error！！！')
    print(e)
