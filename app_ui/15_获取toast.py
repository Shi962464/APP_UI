<<<<<<< HEAD
import os.path
import random

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from fromemail import Email
import pyautogui
=======
from datetime import datetime

from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
>>>>>>> 99ec674d0e6a1c026f52dd82cb9817c488409721

# 配置参数
desired_caps = {
    'platformName': 'Android',
<<<<<<< HEAD
    'platformVersion': '14',
    'deviceName': '5baa00a4',
    'appPackage': 'com.tpshop.malls',
    'appActivity': '.SplashActivity',
    'automationName': 'UiAutomator2',
    'noReset': True,
    'disableWindowAnimation': False,
    'newCommandTimeout': 3600
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(5)
driver.find_element(AppiumBy.ID,'com.tpshop.malls:id/mine_ll').click()
time.sleep(2)
driver.find_element(AppiumBy.ID,'com.tpshop.malls:id/head_img').click()
WEb = WebDriverWait(driver, 10,0.1).until(lambda x: x.find_element(AppiumBy.XPATH,"//*[contains(@text,'请先')]"))
print(WEb.text)
time.sleep(2)
=======
    'platformVersion': '9',
    'deviceName': 'emulator-5556',
    'appPackage': 'com.tpshop.malls',
    'appActivity': '.SPMainActivity',
    'automationName': 'UiAutomator2',
    'autoGrantPermissions': True,
    'noReset': True,
    # 添加以下关键参数
    'intentAction': 'android.intent.action.VIEW',  # 改用VIEW动作
    'dontStopAppOnReset': True,  # 不要停止应用
    'waitForIdleTimeout': 3000,  # 等待时间
    'androidInstallTimeout': 90000,
    # 如果应用有deep link，可以尝试指定URL
    'appWaitActivity': '*',  # 也可以尝试通配符
}

try:
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
except Exception as e:
    print(e)
>>>>>>> 99ec674d0e6a1c026f52dd82cb9817c488409721
