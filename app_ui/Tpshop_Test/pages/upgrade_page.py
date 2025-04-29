import base64
import io
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app_ui.Tpshop_Test.drivers.appium_driver import get_driver
from PIL import Image, ImageOps, ImageFilter
import random
import pytesseract
import pyautogui
import cv2
import numpy as np


class UpgradePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def Register(self):
        """
        注册
        :return:
        """
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/mine_img').click()
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/head_img').click()
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/register_tv').click()
        random_phone = self.random_phone_nimber()  # 调用生成随机手机号
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/phone_num_et').send_keys(random_phone)  # 填入生成的手机号
        result = self.recognize_text_from_screen(self.driver, 1057, 508, 343, 150)  # 调用图像识别
        print(result)
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/validate_code_et').send_keys(result)  # 填入识别结果
        self.driver.find_elements(AppiumBy.ID, 'com.tpshop.malls:id/password_et')[0].send_keys(random_phone)  # 将手机号做密码
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/re_password_et').send_keys(random_phone)  # 再次输入
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/register_tv').click()  # 点击注册

    def Random_Phone_Number(self):
        """
        随机生成11位手机号
        :return:
        """
        first_digit = random.choice(['3', '4', '5', '6', '7', '8', '9'])
        # 随机生成后面 9 位数字
        phone_number = '1' + first_digit + ''.join([random.choice('0123456789') for _ in range(9)])
        return phone_number

    def Login(self):
        """
        登录
        :param username: 用户名 13409834940
        :param password: 密码 123456789
        :return:
        """
        time.sleep(5)
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/mine_img').click()
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/head_img').click()
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/mobile_et').send_keys('13409834940')
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/pwd_et').send_keys('123456789')
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/agree_btn').click()
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/login_tv').click()

    def Shopping(self):
        """
        添加购物车
        :return:
        """
        self.driver.find_elements(AppiumBy.ID, 'com.tpshop.malls:id/recommend_ll')[0].click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='加入购物车']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='确定']").click()

    # 设置 tesseract.exe 路径（如未设置系统环境变量）
    # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # 修改为你自己的路径
    def Recognize_Text_From_Screen(self, driver, x, y, width, height, lang='chi_sim+eng',
                                   screenshot_path="phone_screen.png"):
        """
        使用 Appium 获取手机屏幕截图，并识别指定区域的验证码
        参数:
            driver  - Appium WebDriver 对象
            x, y    - 截图区域的左上角坐标（手机屏幕上的坐标）
            width   - 区域宽度
            height  - 区域高度
            lang    - 识别语言（默认中英文混合）
        返回:
            str: 识别出的文字内容
        """
        # 配置 tesseract 路径（请根据你本地安装情况修改）
        pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"
        try:
            # 1. 保存整个手机屏幕截图到本地
            driver.get_screenshot_as_file(screenshot_path)
            # 2. 打开截图文件
            image = Image.open(screenshot_path)
            # 3. 裁剪你要识别的区域
            cropped = image.crop((x, y, x + width, y + height))
            cropped.save("debug_crop.png")  # 可选：保存裁剪区域用于调试
            # 4. OCR 识别（限制只识别字母和数字）
            custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            text = pytesseract.image_to_string(cropped, lang=lang, config=custom_config)
            # 5. 删除空格和非字母数字
            clean_text = ''.join(filter(str.isalnum, text))
            return clean_text

        except Exception as e:
            print(f"识别失败: {e}")
            return ""

    def Address(self):
        """
        添加地址
        :return:
        """
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/mine_img').click()
        self.driver.find_elements(AppiumBy.ID, 'com.tpshop.malls:id/shortcut_lay')[13].click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='+新建地址']").click()
        self.driver.find_element(AppiumBy.ID, "com.tpshop.malls:id/consignee_name_et").send_keys("石磊")
        self.driver.find_element(AppiumBy.ID, "com.tpshop.malls:id/consignee_mobile_et").send_keys("18888888888")
        self.driver.find_element(AppiumBy.ID, "com.tpshop.malls:id/consignee_region_tv").click()
        self.driver.execute_script("mobile: dragGesture", {
            "startX": 700,  # 起点X坐标
            "startY": 3000,  # 起点Y坐标（较底部）
            "endX": 700,  # 终点X坐标（保持不变）
            "endY": 1100,  # 终点Y坐标（往上滑）
            "speed": 500  # 可选：滑动速度（越大越快）
        })
        # self.execute_script("mobile:dragGesture", {"elementId": src.id,"endX": dst.location["x"],"endY": dst.location["y"]})
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='新疆维吾尔自治区']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='阿克苏地区']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='阿克苏市']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='良种场']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='确定']").click()
        aa = input("输入你的详细地址：")
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/consignee_address_et').send_keys(aa)
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/save_tv').click()

    def Message(self):
        """
        消息中心
        点击消息中心的消息并返回
        :return:
        """
        # 进入消息界面
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/default_message_rl').click()

        # 获取所有消息标题元素（可能是多个）
        message_titles = self.driver.find_elements(AppiumBy.ID, 'com.tpshop.malls:id/message_title')

        # 遍历每个标题元素
        for title_elem in message_titles:
            title_text = title_elem.text
            print(f"点击消息标题: {title_text}")

            # 点击该标题进入详情
            self.driver.find_element(AppiumBy.XPATH, f"//*[@text='{title_text}']").click()

            # 点击返回按钮（通常只有一个）
            self.driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ImageView').click()

    def Search_Click(self):
        # aa = ['手机', '相机']
        # # 点击搜索框
        # self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/default_search_et').click()
        # # 循环搜索
        # for i in aa:
        #     # 再次点击搜索框确认，不然可能会报StaleElementReferenceException
        #     self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/search_et').click()
        #     self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/search_et').send_keys(i)
        #     self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/search_btn').click()
        #     text = self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/search_et')
        #     text.click()

        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/default_search_et').click()
        text = input("输入你要搜索的内容：")
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/search_et').send_keys(text)
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/search_btn').click()
        self.driver.find_elements(AppiumBy.ID, 'com.tpshop.malls:id/product_pic_img')[0].click()
        self.driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ImageView').click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='销量']").click()
        self.driver.find_elements(AppiumBy.ID, 'com.tpshop.malls:id/product_pic_img')[0].click()
        self.driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ImageView').click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='价格']").click()
        self.driver.find_elements(AppiumBy.ID, 'com.tpshop.malls:id/product_pic_img')[0].click()
        self.driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ImageView').click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='价格']").click()
        self.driver.find_elements(AppiumBy.ID, 'com.tpshop.malls:id/product_pic_img')[0].click()
        self.driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ImageView').click()

    def Classification(self):
        # 点击分类
        self.driver.find_element(AppiumBy.ID, 'com.tpshop.malls:id/category_ll').click()
        self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')[1].click()
        print("1111")
        while 1:
            name = self.driver.find_elements(AppiumBy.ID, 'com.tpshop.malls:id/category_item_tv')
            for i in name:
                if i.text=="aaaa":
                    pass
                else:
                    name = i.text
                    print(i.text)
                    self.driver.find_element(AppiumBy.XPATH, f"//*[@text='{name}']").click()
                    self.driver.implicitly_wait(10)
                self.driver.press_keycode(keycode=4)

