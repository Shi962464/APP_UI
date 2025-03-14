import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
desired_caps = {
    'platformName': 'Android',  # 设备的系统
    'platformVersion': '12',  # 设备的版本
    'deviceName': '127.0.0.1:7555',  # 设备ID或模拟器ID
    'appPackage': 'com.android.settings',  # 设置应用包名
    'appActivity': 'com.android.settings.Settings',  # 设置应用启动的活动
    "appium:automationName": "UiAutomator2"  # ✅ 添加 automationName
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
print("启动成功！")
print(f"当前界面的包名为：{driver.current_package}\n当前界面的界面名为：{driver.current_activity}")
time.sleep(3)
driver.activate_app("tv.danmaku.bili")
print(f"切换后界面的包名为：{driver.current_package}\n切换后界面的界面名为：{driver.current_activity}")
time.sleep(3)
driver.background_app(5)
driver.activate_app("com.tpshop.malls")
print(f"切换后界面的包名为：{driver.current_package}\n切换后界面的界面名为：{driver.current_activity}")
driver.terminate_app("tv.danmaku.bili")
time.sleep(3)
driver.terminate_app("com.android.settings")
time.sleep(3)
driver.quit()