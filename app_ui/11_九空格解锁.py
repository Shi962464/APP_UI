from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 配置参数
desired_caps = {
    'platformName': 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:deviceName': 'emulator-5556',
    'appium:platformVersion': '9',
    'appium:appPackage': 'com.android.settings',
    'appium:appActivity': 'com.android.settings.Settings',
}

def unlock():
    pattern = [
        (268, 919), (540, 919), (812, 919),
        (268, 1193), (540, 1193), (812, 1193),
        (268, 1463), (540, 1463), (812, 1463)
    ]
    # 解锁路径，使用九宫格索引（0 - 8），按顺序依次连接点
    unlock_path = [4, 2, 7, 0, 5, 6, 1, 8, 3]  # 使用索引更易维护
    # 根据解锁路径获取具体的坐标点
    unlock_points = [pattern[i] for i in unlock_path]

    # 创建 W3C Actions（高级触摸手势）
    actions = ActionBuilder(driver)

    # 添加 PointerInput（用于触摸输入）
    actions.add_pointer_input(POINTER_TOUCH, "finger_input")

    # 开始绘制解锁图案
    actions.pointer_action \
        .move_to_location(*unlock_points[0]) \
        .pointer_down() \
        .pause(0.1)  # 初始按压停顿

    # 按照路径顺序移动到每个点
    for point in unlock_points[1:]:
        (actions.pointer_action \
         .move_to_location(*point) \
         # 移动到下一个点
         .pause(0.05))
        # 轻微停顿，使滑动更流畅

    # 释放触摸（松开手指）
    actions.pointer_action.pointer_up()
    # 执行手势操作
    actions.perform()
    print("九宫格解锁成功！")


try:
    # 初始化驱动
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    # 导航到九宫格设置
    # wait_click(driver, AppiumBy.XPATH, "//*[@text='安全性和位置信息']")
    # wait_click(driver, AppiumBy.XPATH, "//*[@text='屏幕锁定']")
    # wait_click(driver, AppiumBy.XPATH, "//*[@text='图案']")
    WebDriverWait(driver, timeout=20).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='安全性和位置信息']"))).click()
    WebDriverWait(driver, timeout=20).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='屏幕锁定']"))).click()
    WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='图案']"))).click()
    # 九宫格解锁坐标（需要根据设备的实际分辨率调整）
    unlock()
    WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='下一步']"))).click()
    unlock()
    WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='确认']"))).click()
except Exception as e:
    print(e)
finally:
    # 确保退出 WebDriver，释放资源
    if 'driver' in locals():
        driver.quit()
        print("退出成功！")