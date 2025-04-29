import yaml
from appium import webdriver


def get_driver():
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)  # ת�����ֵ����

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", config)
    driver.implicitly_wait(20)  # ��ʽ�ȴ�20��
    return driver  # ���س�ʼ���õ�driver����
