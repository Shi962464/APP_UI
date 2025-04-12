import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app_ui.Tpshop_Test.drivers.appium_driver import get_driver

class UpgradePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        """
        登录功能
        :param username: 用户名 13409834940
        :param password: 密码 123456789
        :return:
        """
        time.sleep(5)
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/mine_img').click()
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/mobile_et').send_keys(username)
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/pwd_et').send_keys(password)
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/agree_btn').click()
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/login_tv').click()

    def shopoing(self):
        pass

if __name__ == '__main__':
    driver = get_driver()
    aa=UpgradePage(driver)
    aa.login(13409834940, '123456')


