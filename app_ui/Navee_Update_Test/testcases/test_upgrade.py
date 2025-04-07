import time
from drivers.appium_driver import get_driver
from pages.upgrade_page import UpgradePage
from utils.file_helper import clear_result_file, append_result
from utils.random_click import random_click
from utils.email_helper import send_error_email


def test_upgrade_loop():
    driver = get_driver()
    up_page = UpgradePage(driver)
    clear_result_file()

    try:
        up_page.select_device()
        up_page.click_toolbar()
        up_page.click_upgrade()

        up_num = 1

        while True:
            text = up_page.get_upgrade_button_text()
            if text == "重新升级":
                append_result(False, up_num)
                print("检测到升级失败，重新点击")
                up_page.click_update_button()
                up_num += 1
            elif text == "确定":
                append_result(True, up_num)
                print("升级成功！")
                up_page.confirm_success()
                up_page.click_toolbar()
                up_page.click_update_button()
                up_num += 1
            random_click()
            time.sleep(3)

    except Exception as e:
        send_error_email("Update_Error!!!")
        print("异常:", e)
    finally:
        driver.quit()
