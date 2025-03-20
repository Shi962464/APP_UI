import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    'platformName': 'Android',  # 设备的系统
    'platformVersion': '9',  # 设备的版本
    'deviceName': 'emulator-5556',  # 设备ID或模拟器ID
    'appPackage': 'tv.danmaku.bili',  # 设置应用包名
    'appActivity': 'tv.danmaku.bili.MainActivityV2',  # 设置应用启动的活动
    "appium:automationName": "UiAutomator2" , # ✅ 添加 automationName
}
try :
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
except Exception as e:
    print(f"Error is {e}")
time.sleep(3)
driver.find_element(AppiumBy.XPATH,"//*[@text='同意并继续']").click()
time.sleep(5)
driver.get_screenshot_as_file("{}.png".format(time.strftime('%Y-%m-%d %H-%M-%S')))
str=driver.get_window_size()
print(str)
driver.swipe(700,1700,700,400,duration=0)
time.sleep(5)
driver.get_screenshot_as_file("{}.png".format(time.strftime('%Y-%m-%d %H-%M-%S')))
driver.swipe(730,125,430,125,duration=0)
time.sleep(5)
driver.get_screenshot_as_file("{}.png".format(time.strftime('%Y-%m-%d %H-%M-%S')))
driver.find_element(AppiumBy.XPATH,"//*[@text='两会']").click()
time.sleep(3)
driver.get_screenshot_as_file("{}.png".format(time.strftime('%Y-%m-%d %H-%M-%S')))
driver.quit()