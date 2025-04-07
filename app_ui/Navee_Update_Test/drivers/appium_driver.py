import yaml
from appium import webdriver

def get_driver():
    """
    集成了连接appium服务器的一些信息
    :return:
    """
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)  # 转换成字典对象

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", config)
    driver.implicitly_wait(20)  # 隐式等待20秒
    return driver   # 返回初始化好的driver对象
