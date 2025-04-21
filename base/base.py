import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from tool.get_logger import GetLogger

#使用单例
log = GetLogger().get_logger()
class Base:
    def __init__(self,driver):
        log.info("获取driver对象{}".format(driver))
        self.driver = driver

    #查找元素方法 封装
    def base_find_element(self,loc,timeout=30,poll=0.5):
        log.info("查找元素{}".format(loc))
        #使用显示等待
        return WebDriverWait(self.driver,
                            timeout=timeout,
                            poll_frequency=poll).until(lambda x: x.find_element(*loc))

    #点击元素 方法封装
    def base_click(self,loc):
        log.info("点击{}元素".format(loc))
        self.base_find_element(loc).click()

    #输入元素 方法封装
    def base_input_text(self,loc,value):
        log.info("正在给元素{}输入内容:{}".format(loc, value))
        #获取元素
        el = self.base_find_element(loc)
        #清空
        el.clear()
        log.info("正在给{}元素清空".format(loc))
        #输入元素
        el.send_keys(value)

    #获取文本信息 方法封装
    def base_get_text(self,loc):
        log.info("获取的文本内容{}".format(self.base_find_element(loc).text))
        return self.base_find_element(loc).text

    # 截图 方法封装
    def base_get_screenshot(self):
        self.driver.get_screenshot_as_file(r'D:/web测试/day09_pytest/image/{}.png'.format(time.strftime('%Y-%m-%d %H-%M-%S')))


    #判断元素是否存在 方法封装
    def base_element_is_exist(self,loc):
        try:
            self.base_find_element(loc,timeout=2)
            log.info("判断元素:{}存在！".format(loc))

            return True  #代表元素存在
        except:
            log.info("元素{}不存在".format(loc))
            return False  #代表元素不存在