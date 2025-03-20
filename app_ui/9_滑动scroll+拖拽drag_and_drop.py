import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
desired_caps = {
    'platformName': 'Android',  # 设备的系统
    'platformVersion': '9',  # 设备的版本
    'deviceName': 'emulator-5556',  # 设备ID或模拟器ID
    'appPackage': 'com.android.settings',  # 设置应用包名
    'appActivity': 'com.android.settings.Settings',  # 设置应用启动的活动
    "appium:automationName": "UiAutomator2" , # ✅ 添加 automationName
}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub", desired_caps)

driver.install_app(r"D:\APP_Test\tp.apk")
driver.install_app(r"D:\APP_Test\bilibili.apk")

# src=driver.find_element(AppiumBy.XPATH,"//*[@text='应用和通知']")
# dst=driver.find_element(AppiumBy.XPATH,"//*[@text='网络和互联网']")
# driver.execute_script("mobile:dragGesture", {
#     "elementId": src.id,
#     "endX": dst.location["x"],
#     "endY": dst.location["y"]
# })
# time.sleep(3)
# driver.scroll(origin_el=src,destination_el=dst)
# time.sleep(3)