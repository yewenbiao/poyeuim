import page
from base.base_action import BaseAction


class NetworkPage(BaseAction):

    def __init__(self, driver):
         BaseAction.__init__(self, driver)

    # 1.点击更多
    def click_textview_more(self):
        self.click_element(page.network_page_textview_more)

    # 2.点击移动网络
    def click_textview_mobile_network(self):
        self.click_element(page.network_page_textview_mobile_network)

    # 3.首选网络类型
    def click_textview_first_network(self):
        self.click_element(page.network_page_textview_first_network)

    # 4.点击2G
    def click_textview_2g(self):
        self.click_element(page.network_page_textview_2g)

    # 5.点击3G
    def click_textview_3g(self):
        self.click_element(page.network_page_textview_3g)
