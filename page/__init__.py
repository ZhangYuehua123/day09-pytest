from selenium.webdriver.common.by import By

#url
#页面地址
url = "https://hmshop-test.itheima.net/"
#登录链接
login_link = By.PARTIAL_LINK_TEXT,"登录"
#用户名
login_username = By.ID,"username"
#密码
login_password =By.ID,"password"
#验证码
login_code = By.ID,"verify_code"
#登录按钮
login_but = By.CSS_SELECTOR,".J-login-submit"
#消息提示框
login_msg = By.CSS_SELECTOR,".layui-layer-content"
#ok按钮
login_btn_ok = By.CSS_SELECTOR,".layui-layer-btn0"
#安全退出
login_btn_safe_logout = By.PARTIAL_LINK_TEXT,"安全退出"