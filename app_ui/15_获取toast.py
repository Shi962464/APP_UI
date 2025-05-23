from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
time.sleep(5)
driver.find_element(AppiumBy.ID,'com.tpshop.malls:id/mine_ll').click()
time.sleep(2)
driver.find_element(AppiumBy.ID,'com.tpshop.malls:id/head_img').click()
WEb = WebDriverWait(driver, 10,0.1).until(lambda x: x.find_element(AppiumBy.XPATH,"//*[contains(@text,'请先')]"))
print(WEb.text)
time.sleep(2)
