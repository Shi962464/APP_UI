import time
from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '12',
    'deviceName': '127.0.0.1:7555',
    'appPackage': 'com.tpshop.malls',
    'appActivity': 'com.tpshop.malls.SplashActivity',
    'automationName': 'UiAutomator2',
    'autoGrantPermissions': True,
    'noReset': True,
    # 添加以下关键参数
    'intentAction': 'android.intent.action.VIEW',  # 改用VIEW动作
    'dontStopAppOnReset': True,  # 不要停止应用
    'waitForIdleTimeout': 3000,  # 等待时间
    'androidInstallTimeout': 90000,
    # 如果应用有deep link，可以尝试指定URL
    # 'appWaitActivity': '*',  # 也可以尝试通配符
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

driver.install_app(r"E:\APPTest\tp.apk")
driver.install_app(r"E:\APPTest\bili.apk")
# driver.remove_app('com.bstar.intl')

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