from datetime import datetime

from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置参数
desired_caps = {
    'platformName': 'Android',
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