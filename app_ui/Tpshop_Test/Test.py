import os.path
import random

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from app_ui.fromemail import Email
import pyautogui

# 配置参数
desired_caps = {
    'platformName': 'Android',
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
driver.implicitly_wait(20)
time.sleep(5)
driver.find_element(AppiumBy.ID,'com.tpshop.malls:id/mine_img').click()
driver.find_element(AppiumBy.ID,'com.tpshop.malls:id/head_img').click()
time.sleep(1)
driver.find_element(AppiumBy.ID,'com.tpshop.malls:id/mobile_et').send_keys('13409834940')
time.sleep(1)
driver.find_element(AppiumBy.ID,'com.tpshop.malls:id/pwd_et').send_keys('123456789')
time.sleep(1)
driver.find_element(AppiumBy.ID,'com.tpshop.malls:id/agree_btn').click()
driver.find_element(AppiumBy.ID,'com.tpshop.malls:id/login_tv').click()
time.sleep(2)




