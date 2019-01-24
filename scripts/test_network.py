import os, sys

sys.path.append(os.getcwd())
from page.network_page import NetworkPage

import page
from base.init_driver import get_driver
import time


class TestSetting:
    # 初始化driver
    def setup(self):
        # 初始化手机驱动
        self.driver = get_driver(page.setting_appPackage,page.setting_appActivity)
        self.networkPage = NetworkPage(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    # 修改2g网络
    # def test_update_2g(self):
    #     time.sleep(1)
    #     #1.点击更多
    #     self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
    #     time.sleep(1)
    #     #2.点击移动网络
    #     self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
    #     time.sleep(1)
    #     #3.首选网络类型
    #     self.driver.find_element_by_xpath("//*[contains(@text,'首选网络')]").click()
    #     time.sleep(1)
    #     #4.点击2G
    #     self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()
    # #修改3g网络
    # def test_update_3g(self):
    #     # 1.点击更多
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
    #     # 2.点击移动网络
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
    #     time.sleep(1)
    #     # 3.首选网络类型
    #     self.driver.find_element_by_xpath("//*[contains(@text,'首选网络')]").click()
    #     time.sleep(1)
    #     # 4.点击3G
    #     self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()

    def test_update_2g(self):
        # 1.点击更多
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.networkPage.click_textview_more()
        # 2.点击移动网络
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.networkPage.click_textview_mobile_network()
        # 3.首选网络类型
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络')]").click()
        self.networkPage.click_textview_first_network()
        # 4.点击2G
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()
        self.networkPage.click_textview_2g()

    # 修改3g网络
    def test_update_3g(self):
        # 1.点击更多
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.networkPage.click_textview_more()
        # 2.点击移动网络
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.networkPage.click_textview_mobile_network()
        # 3.首选网络类型
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络')]").click()
        self.networkPage.click_textview_first_network()
        # 4.点击3G
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
        self.networkPage.click_textview_3g()
