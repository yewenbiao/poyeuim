from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import page
class DisplayPage(BaseAction):

    #driver是外面传递进来的
    def __init__(self,driver):
        # self.driver = driver
        BaseAction.__init__(self,driver)

    # 点击显示
    def click_textview_show(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element(By.XPATH,"//*[contains(@text,'显示')]").click()
        #self.driver.find_element(self.display_page_textview_show[0],self.display_page_textview_show[1]).click()
        # self.find_element(self.display_page_textview_show).click()
        self.click_element(page.display_page_textview_show)

    # 点击搜索按钮
    def click_btn_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        #self.driver.find_element(By.ID, "com.android.settings:id/search").click()
        # self.find_element(self.display_page_btn_search).click()
        self.click_element(page.display_page_btn_search)

    #向搜索框输入内容
    def input_edit_search_content(self,content):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("aaaa")
        # self.find_element(self.display_page_edit_search_content).send_keys("bbbb")
        self.input_edit_content(page.display_page_edit_search_content,content)
        print("sdjaflsadjflksadjfl")

    #点击返回按钮
    def click_btn_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.find_element(self.display_page_btn_back).click()
        self.click_element(page.display_page_btn_back)





