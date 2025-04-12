import yaml
from appium import webdriver

def get_driver():
    with open("tp_config/tp_config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", config)
    driver.implicitly_wait(20)
    return driver
