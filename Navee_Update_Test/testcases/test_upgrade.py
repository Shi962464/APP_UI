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
        up_page.goif_select_device()
        up_page.click_toolbar()
        up_page.click_upgrade()

        up_num = 1
        scee=0
        res=0
        number=0
        while True:
            print("升级成功：{}升级失败：{}".format(scee, res))
            # random_click()
            text = up_page.get_upgrade_button_text()

            if text == "重新升级":
                append_result(success=False, count=up_num)
                print("检测到升级失败，重新点击")
                up_page.again_click()
                up_num += 1
                res+=1

            elif text == "确定":
                append_result(success=True, count=up_num)
                print("升级成功！")
                up_page.confirm_success()
                up_page.click_toolbar()
                up_page.click_upgrade()
                up_num += 1
                scee+=1

            time.sleep(4)
            number+=1
            # num += 1

    except Exception as e:
        send_error_email()
        print("异常:", e)
# send_error_email("Sucessfully Upgrade")