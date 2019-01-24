from base.base_action import BaseAction
import page
class SettingSearchPage(BaseAction):

    #SmsPage的构造函数
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 1.实现点击搜索按钮
    def click_btn_search(self):
        self.click_element(page.setting_page_btn_search)

    # 2.定位搜索输入框并输入搜索关键字
    def input_edit_search_content(self,content):
        self.input_edit_content(page.setting_page_edit_search_content,content)


