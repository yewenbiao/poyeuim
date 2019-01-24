from base.base_action import BaseAction
from selenium.webdriver.common.by import By
import page
class SmsPage(BaseAction):

    #SmsPage的构造函数
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 1.实现点击新增短信按钮
    def click_btn_add_sms(self):
        self.click_element(page.sms_page_btn_add_sms)
        # self.driver.find_element_by_id("com.android.mms:id/action_compose_new").click()

    # # 2.定位到接收者
    def input_edit_recipient_content(self):
        self.input_edit_content(page.sms_page_edit_recipient,"10086")
        # self.driver.find_element_by_id("com.android.mms:id/recipients_editor").send_keys("100101")

    # # 1.找到输入框
    def input_edit_sms_content(self,content):
        self.input_edit_content(page.sms_page_edit_sms_content,content)
        #1.1输入内容
        # input_sms_content = self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor")
        # input_sms_content.send_keys(content)
    # # 2.找到发送按钮
    def click_btn_send_sms(self):
        self.click_element(page.sms_page_btn_send_sms)
        # self.driver.find_element_by_id("com.android.mms:id/send_button_sms").click()

    # 3.获取当前页所有短信内容
    def get_sms_content_lists(self):
        return self.find_elements(page.sms_page_textview_sms_contents)

