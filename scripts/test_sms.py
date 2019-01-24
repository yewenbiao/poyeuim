import os, sys
sys.path.append(os.getcwd())
import pytest
import page
import time
from base.init_driver import get_driver
from page.sms_page import SmsPage
from base import read_action


class TestSms:
    #获取driver
    def setup_class(self):
        #初始化手机驱动driver
        self.driver = get_driver(page.sms_appPackage,page.sms_appActivity)
        #实例化smsPage
        self.smsPage = SmsPage(self.driver)

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

    #实现向接收者控件里面输入内容 input_receiver这个函数会优先test_send_sms执行 并且自动运行 且执行一次
    @pytest.fixture(scope='class', autouse=True)
    def input_receiver(self):
        #1.实现点击新增短信按钮
        self.smsPage.click_btn_add_sms()
        #2.定位到接收者
        self.smsPage.input_edit_recipient_content()

    #实现发送短信
    @pytest.mark.parametrize("content", read_action.get_data_lists("sms_content.yaml","sms_contents"))
    def test_send_sms(self,content):
        #1.找到输入框
        #1.1输入内容
        self.smsPage.input_edit_sms_content(content)

        #2.找到发送按钮
        self.smsPage.click_btn_send_sms()
        #3.verify短信是否发送成功
        sms_send_lists = self.smsPage.get_sms_content_lists()
        assert content in [i.text for i in sms_send_lists]


