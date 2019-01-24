import os, sys

import pytest

sys.path.append(os.getcwd())
from page.login_page import LoginPage
import page
import time
from base.init_driver import get_driver
from base import read_action


class TestLogin:
    #获取driver
    def setup_class(self):
        #初始化手机驱动driver
        self.driver = get_driver(page.toutiao_appPackage,page.toutiao_appActivity)
        #实例化settingSearchPage
        self.loginPage = LoginPage(self.driver)

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

    def test_into_email_login_page(self):
        self.loginPage.click_text_my()
        self.loginPage.click_btn_home_login()
        self.loginPage.click_btn_email()

    @pytest.mark.parametrize("uname,pwd",read_action.get_data_lists("email_login.yaml","email_login_data"))
    def test_email_login(self,uname,pwd):
        self.loginPage.input_edit_email_content(uname)
        self.loginPage.input_edit_password_content(pwd)
        self.loginPage.click_btn_email_login()
        loginusername = self.loginPage.get_text_loginuser()
        assert loginusername == "xiha23"
        time.sleep(2)




