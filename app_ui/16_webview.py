# -*- coding: utf-8 -*-
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

# 配置参数
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'emulator-5556',
    'appPackage': 'com.android.browser',
    'appActivity': '.BrowserActivity',
    'automationName': 'UiAutomator2',
    'noReset': True,
    'disableWindowAnimation': False,
    'newCommandTimeout': 3600,
    'chromedriverExecutable': r'E:\APPTest\Android_Sdk\Android_Sdk\androidsdk\tools\chromedriver.exe'
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(5)
driver.find_element(AppiumBy.ID,'com.android.browser:id/url').click()
time.sleep(2)
url=driver.find_element(AppiumBy.ID,'com.android.browser:id/url')
url.clear()
url.send_keys('http://m.baidu.com')
time.sleep(2)
driver.press_keycode(66)
time.sleep(2)
# driver.switch_to.context(MobileBy.XPATH)
print(driver.context)