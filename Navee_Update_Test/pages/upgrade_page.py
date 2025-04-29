import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UpgradePage:
    def __init__(self, driver):
        """
        :param driver: 使用appium_driver里的方法
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navee_select_device(self, name="10A5628B83CD"):
        """
        NAVEE
        :param name: 自己想要测试的Mac地址
        :return:
        """
        self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, "com.navee.ucaret:id/button_toolbar"))).click()  # 点击APP首页切换按钮
        devices = self.driver.find_elements(AppiumBy.ID, "com.navee.ucaret:id/subtitleLabel")  # 获取元素
        for i in devices:
            if i.text == name:  # 判断元素
                i.click()  # 点击连接该设备
                break
        print("获取成功")

    # def goif_select_device(self, name='10A5628B83AE'):
    def goif_select_device(self, name='10A5628B83CD'):
        """
        GOIF
        :param name:自己想要测试的Mac地址
        :return:
        """
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.navee.ucaret:id/switch_toolbar"))).click()
        devices = self.driver.find_elements(AppiumBy.ID, "com.navee.ucaret:id/subtitleLabel")  # 获取元素
        for i in devices:
            if i.text == name:  # 判断元素
                i.click()  # 点击连接该设备
                break
        print("获取成功")

    def click_toolbar(self):
        """
        创建一个需要多次用到的函数，方便调用
        :return:
        """
        self.driver.find_element(AppiumBy.ID, 'com.navee.ucaret:id/bluetoothStatusButton').click()  # 点击APP上蓝牙图标
        print("点击蓝牙图标")
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.navee.ucaret:id/infoButton"))).click()  # 点击了解车辆
        print("点击了解车辆")
        time.sleep(10)
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='检查固件更新']").click()  # 点击检查固件和更新
        print("点击检查更新")
        time.sleep(2)

    def click_upgrade(self):
        time.sleep(2)
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='立马升级']").click()
        time.sleep(2)
        print("点击立马升级")
    def again_click(self):
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='重新升级']").click()
        time.sleep(2)
        print("点击重新升级")
    def get_upgrade_button_text(self):
        """
        获取升级界面的文本
        :return:
        """
        return self.driver.find_element(AppiumBy.ID, "com.navee.ucaret:id/updateButton").text

    # def click_update_button(self):
    #     """
    #     点击升级界面的立马升级按钮
    #     :return:
    #     """
    #     self.driver.find_element(AppiumBy.ID, "com.navee.ucaret:id/updateButton").click()

    def confirm_success(self):
        """
        升级完之后点击确认，并在了解车辆返回上一级
        :return:
        """
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='确定']"))).click()
        print("点击确定")
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.ImageButton"))).click()
        print("点击返回")
        time.sleep(3)