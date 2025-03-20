import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

desired_caps = {
    'platformName': 'Android',  # 设备的系统
    'platformVersion': '9',  # 设备的版本
    'deviceName': 'emulator-5556',  # 设备ID或模拟器ID
    'appPackage': 'com.android.settings',  # 设置应用包名
    'appActivity': 'com.android.settings.Settings',  # 设置应用启动的活动
    "appium:automationName": "UiAutomator2" , # ✅ 添加 automationName
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.find_element(AppiumBy.XPATH,"//*[@text='安全性和位置信息']").click()
driver.implicitly_wait(2)
driver.find_element(AppiumBy.XPATH,"//*[@text='屏幕锁定']").click()
driver.implicitly_wait(2)
driver.find_element(AppiumBy.XPATH,"//*[@text='图案']").click()
driver.implicitly_wait(2)
pattern = [
    (268, 919),    # 点1
    (540, 919),    # 点2
    (812, 919),    # 点3
    (268, 1193),   # 点4
    (540, 1193),   # 点5
    (812, 1193),   # 点6
    (268, 1463),   # 点7
    (540, 1463),   # 点8
    (812, 1463),   # 点9
]
# 解锁路径，例如从 1 → 2 → 5 → 8 → 9
unlock_pattern = [pattern[4], pattern[2], pattern[7], pattern[0],pattern[5],pattern[6],pattern[1],pattern[8],pattern[3]]
# 创建 W3C 手势操作
finger = PointerInput("touch", "finger1")
actions = ActionBuilder(driver)
actions.add_pointer_input(finger)
# 按下第一个点
actions.pointer_action.move_to_location(*unlock_pattern[0])
actions.pointer_action.pointer_down()
# 按顺序滑动
for point in unlock_pattern[1:]:
    actions.pointer_action.move_to_location(*point)
    actions.pointer_action.pause(0.2)  # 增加一点停顿，使滑动更自然
# 释放手势
actions.pointer_action.pointer_up()
# 执行手势
actions.perform()
print("九宫格解锁完成！")