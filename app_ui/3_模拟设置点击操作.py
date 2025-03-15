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
driver.find_element(AppiumBy.ID,"android:id/title").click()
time.sleep(2)
driver.find_elements(AppiumBy.ID,"android:id/title")[1].click()
time.sleep(2)
driver.find_element(AppiumBy.CLASS_NAME,"android.widget.TextView").click()
time.sleep(2)
driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText").clear()
time.sleep(3)
driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText").send_keys("China NR")
time.sleep(2)
driver.find_element(AppiumBy.ID,"android:id/button1").click()
time.sleep(3)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'向上导航').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//*[@content-desc="向上导航"]').click()
time.sleep(3)
driver.terminate_app('com.android.settings')
driver.quit()

