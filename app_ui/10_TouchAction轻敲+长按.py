import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains

desired_caps = {
    'platformName': 'Android',  # 设备的系统
    'platformVersion': '9',  # 设备的版本
    'deviceName': 'emulator-5556',  # 设备ID或模拟器ID
    'appPackage': 'com.android.settings',  # 设置应用包名
    'appActivity': 'com.android.settings.Settings',  # 设置应用启动的活动
    "appium:automationName": "UiAutomator2" , # ✅ 添加 automationName
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


driver.find_element(AppiumBy.XPATH,"//*[@text='网络和互联网']").click()
time.sleep(2)
driver.find_element(AppiumBy.XPATH,"//*[@text='WLAN']").click()
time.sleep(2)
ele=driver.find_element(AppiumBy.XPATH,"//*[@text='已连接']")
# ActionChains(driver).move_to_element(ele).click().perform()
x=ele.location['x']
y=ele.location['y']
driver.tap([(x,y)], 5000)

time.sleep(2)
