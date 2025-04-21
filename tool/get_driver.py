from selenium import webdriver
from page import url
class GetDriver:
    #定义一个变量来保存单例
    driver = None
    #获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            driver = cls.driver
            driver.maximize_window()
            driver.get(url)
            return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None


if __name__ == '__main__':
    driver = GetDriver()
    driver.get_driver()
    driver.quit_driver()
