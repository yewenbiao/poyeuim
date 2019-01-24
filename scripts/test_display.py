import os,sys
sys.path.append(os.getcwd())
import page
from base.init_driver import get_driver
from page.display_page import DisplayPage
import time
class TestSetting:
    #初始化driver
    def setup(self):
        #1.初始化driver
        self.driver = get_driver(page.setting_appPackage,page.setting_appActivity)
        #2.获取displaypage对象
        self.displaypage = DisplayPage(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()
    #显示 搜索
    def test_display_search(self):
        # 1.点击显示
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        self.displaypage.click_textview_show()
        # 2.点击搜索按钮
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.displaypage.click_btn_search()
        #3.定位到搜索框 并输入内容
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        self.displaypage.input_edit_search_content("eee")
        #4.点击返回按钮
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        self.displaypage.click_btn_back()