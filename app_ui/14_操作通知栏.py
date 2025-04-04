from datetime import datetime

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置参数
desired_caps = {
    'platformName': 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:deviceName': 'emulator-5556',
    'appium:platformVersion': '9',
    'appium:appPackage': 'com.android.settings',
    'appium:appActivity': 'com.android.settings.Settings',
    'automationName': 'UIAutomator2',
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.open_notifications()
time.sleep(2)
app_name = driver.find_elements(AppiumBy.ID, "android:id/app_name_text")[1]
print(app_name.text)
driver.find_element(AppiumBy.XPATH, "//*[@text='配置实体键盘']").click()
time.sleep(2)
driver.press_keycode(4)
time.sleep(2)
