import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# 初始化 desired_caps 字典
desired_caps = {
    'platformName': 'Android',  # 设备的系统
    'platformVersion': '12',  # 设备的版本
    'deviceName': '127.0.0.1:7555',  # 设备ID或模拟器ID
    'appPackage': 'com.android.settings',  # 设置应用包名
    'appActivity': 'com.android.settings.Settings',  # 设置应用启动的活动
    "appium:automationName": "UiAutomator2"  # ✅ 添加 automationName
}

# 打印 desired_caps 确认配置正确
print("Desired capabilities:")
for key, value in desired_caps.items():
    print(f"{key}: {value}")

# 初始化 WebDriver 会话，连接到 Appium 服务器
try:
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    print("启动成功！")
except Exception as e:
    print(f"Failed to start driver: {e}")
if driver.is_app_installed("tv.danmaku.bili"):
    driver.remove_app('tv.danmaku.bili')
else:
    driver.install_app(r'D:\APP_Test\bilibili.apk')
driver.quit()



driver.find_element(AppiumBy.ID("resource-id属性值"))
driver.find_element(AppiumBy.CLASS_NAME("class属性值"))
driver.find_element(AppiumBy.XPATH("xpath表达式"))
driver.find_element(AppiumBy.ACCESSIBILITY_ID("content-desc属性值"))
