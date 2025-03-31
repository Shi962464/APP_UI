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
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(24)
time.sleep(2)
driver.get_screenshot_as_file("{}.jpg".format(time.time()))
driver.press_keycode(4)
time.sleep(2)
driver.get_screenshot_as_file("{}.jpg".format(time.time()))
driver.press_keycode(25)
driver.press_keycode(25)