import os, sys
sys.path.append(os.getcwd())
import yaml
import pytest
import page
import time
from base.init_driver import get_driver
from page.setting_search_page import SettingSearchPage
from base import read_action


class TestSettingSearch:
    #获取driver
    def setup_class(self):
        #初始化手机驱动driver
        self.driver = get_driver(page.setting_appPackage,page.setting_appActivity)
        #实例化settingSearchPage
        self.settingSearchPage = SettingSearchPage(self.driver)

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

    #实现向接收者控件里面输入内容 input_receiver这个函数会优先test_send_sms执行 并且自动运行 且执行一次
    @pytest.fixture(scope='class', autouse=True)
    def click_btn_search(self):
        # 1.实现点击搜索按钮
        self.settingSearchPage.click_btn_search()


    #setting中搜索内容
    @pytest.mark.parametrize("content",read_action.get_data_lists("search_content.yaml","search_contents"))
    def test_edit_search_content(self,content):
        self.settingSearchPage.input_edit_search_content(content)


