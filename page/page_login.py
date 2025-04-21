from base.base import Base
import page
from time import sleep
class PageLogin(Base):
    #开始进行页面操作
    #点击登录按钮，进入登录页面
    def page_login_link(self):
        self.base_click(page.login_link)
    #输入用户名
    def page_input_username(self,username):
        self.base_input_text(page.login_username,username)
    #输入密码
    def page_input_password(self,pwd):
        self.base_input_text(page.login_password,pwd)
    #输入验证码
    def page_input_code(self,code):
        self.base_input_text(page.login_code,code)
    #点击登录
    def page_login_click(self):
        self.base_click(page.login_but)
    #获取异常提示信息
    def page_get_text(self):
        return self.base_get_text(page.login_msg)
    #点击确定ok
    def page_click_ok_btn(self):
        self.base_click(page.login_btn_ok)
    #截图
    def page_get_screenshot(self):
        self.base_get_screenshot()
    #判断是否登录成功，找安全退出按钮
    def page_is_login(self):
        return self.base_element_is_exist(page.login_btn_safe_logout)
    #判断是否退出成功,找登录链接
    def page_is_logout(self):
        return self.base_element_is_exist(page.login_link)
    #登录成功后，安全退出
    def page_safe_logout(self):
        self.base_click(page.login_btn_safe_logout)
    #组合业务逻辑
    def page_login(self,username,pwd,code):
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_input_code(code)
        self.page_login_click()