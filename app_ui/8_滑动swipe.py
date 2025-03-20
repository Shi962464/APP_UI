import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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
time.sleep(3)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'分区，按钮').click()
time.sleep(3)
# driver.swipe(666,1523,666,804,duration=0)
size=driver.get_window_size()
time.sleep(3)
start_Y=size.get("height")*0.75
end_Y=size.get("height")*0.25
driver.swipe(200,start_Y,200,end_Y,duration=0)
print("滑动成功")
time.sleep(3)
driver.quit()



# size=driver.get_window_size()
# start_Y=size.get("height")*0.75
# end_Y=size.get("height")*0.25
# driver.swipe(200,start_Y,200,end_Y,duration=None)
