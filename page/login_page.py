from base.base_action import BaseAction
import page
class LoginPage(BaseAction):

    #SmsPage的构造函数
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 1.实现点击搜索按钮
    def click_text_my(self):
        self.click_element(page.home_page_textview_my)

    # 3.点击登录注册
    def click_btn_home_login(self):
        self.click_element(page.home_page_btn_login)

    # 4.使用邮箱登录注册
    def click_btn_email(self):
        self.click_element(page.login_page_btn_email)

    # 5.输入邮箱
    def input_edit_email_content(self,content):
        self.input_edit_content(page.login_page_edit_email,content)
    # 6.输入密码
    def input_edit_password_content(self,content):
        self.input_edit_content(page.login_page_edit_pwd,content)
    # 7.点击登录
    def click_btn_email_login(self):
        self.click_element(page.login_page_btn_email_login)

    #登录后用户信息
    def get_text_loginuser(self):
        return self.find_element(page.login_page_textview_loginuser).text





