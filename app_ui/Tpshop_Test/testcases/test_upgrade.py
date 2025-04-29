import time
from drivers.appium_driver import get_driver
from pages.upgrade_page import UpgradePage

def test_upgrade_loop():
    driver = get_driver()
    up_page = UpgradePage(driver)
    up_page.Classification()
    # up_page.address()
    # up_page.shopping()
    # up_page.Register()
    # up_page.aa()
    # up_page.login()
