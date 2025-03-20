import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
desired_caps = {
    'platformName': 'Android',  # 设备的系统
    'platformVersion': '12',  # 设备的版本
    'deviceName': '127.0.0.1:7555',  # 设备ID或模拟器ID
    'appPackage': 'com.android.settings',  # 设置应用包名
    'appActivity': 'com.android.settings.Settings',  # 设置应用启动的活动
    "appium:automationName": "UiAutomator2" , # ✅ 添加 automationName
    "appium:enableAppiumBehavior": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

res=driver.find_elements(AppiumBy.ID,'android:id/title')
for re in res:
    print(re.text)
print(end="\n")
# driver.find_elements(AppiumBy.ID,'android:id/title')[0].click()
xpaths=driver.find_element
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
desired_caps = {
    'platformName': 'Android',  # 设备的系统
    'platformVersion': '12',  # 设备的版本
    'deviceName': '127.0.0.1:7555',  # 设备ID或模拟器ID
    'appPackage': 'com.android.settings',  # 设置应用包名
    'appActivity': 'com.android.settings.Settings',  # 设置应用启动的活动
    "appium:automationName": "UiAutomator2" , # ✅ 添加 automationName
    "appium:enableAppiumBehavior": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)(AppiumBy.XPATH, "//*[contains(@text, '网')]")
#
print(xpaths.text)
xpaths.click()
time.sleep(2)
driver.quit()
