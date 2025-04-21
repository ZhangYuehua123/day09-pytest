import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from parameterized import parameterized
from page.page_login import PageLogin
from tool.get_driver import GetDriver
import pytest
import unittest
from time import sleep
from tool.get_logger import GetLogger
from tool.read_yaml import read_yaml


#获取日志
log = GetLogger().get_logger()
#获取数据
def get_data():
    datas = read_yaml("login1.yaml")
    arr=[]
    for data in datas.values():
        arr.append(tuple(data.values()))
    return arr
# print(get_data())

class TestLogin:
    driver = None
    def setup_class(self):
        #获取driver
        self.driver = GetDriver().get_driver()
        #获取页面对象
        self.login = PageLogin(self.driver)
        #点击登录链接
        self.login.page_login_link()

    def teardown_class(self):
        #关闭driver
        sleep(2)
        GetDriver().quit_driver()

    @pytest.mark.parametrize("username,password,code,expect_result,success", get_data())
    def test_login(self,username,password,code,expect_result,success):
        #进行登录验证
        self.login.page_login(username,password,code)
        #如果登录成功
        if success:
            try:
                #判断是否有安全退出按钮
                assert self.login.page_is_login()
                sleep(2)
                #有的话点击安全退出回到登录页面
                self.login.page_safe_logout()
                try:
                    #判断是否有登录链接
                    assert self.login.page_is_logout()
                    #有的话点击
                    self.login.page_login_link()
                except Exception as e:
                    #登录页面跳转不成功
                    self.login.page_get_screenshot()
                    log.error(e)
            except Exception as e:
                #退出失败
                self.login.page_get_screenshot()
                log.error(e)

        #登录不成功
        else:
            # 捕获异常
            try:
                #获取登录提示信息
                msg = self.login.page_get_text()
                print("登录提示框信息：",msg)
                assert msg==expect_result
                # #正确的话点击确认
                # self.login.page_click_ok_btn()
            except Exception as e:
                #出现异常了，截图
                self.login.page_get_screenshot()
                log.error(e)
            # 正确的话点击确认
            self.login.page_click_ok_btn()






