"""
类里面包含公共的操作 比如查找元素 点击元素 向输入框里面输入内容...
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=10, poll=1.0):
        """
        这个方法就是查找元素的方法
        :param loc: 元组
        :param timeout: 超时时长timeout=10
        :param poll: 间隔时长poll=1.0
        :return: 返回单个元素element
        """
        time.sleep(1)  # 找元素之前等一会
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=10, poll=1.0):
        """
        返回查找元素的列表的方法
        :param loc:  元组
        :param timeout: 超时时长timeout=10
        :param poll: 间隔时长poll=1.0
        :return: 返回一个元素列表elements
        """
        time.sleep(1)  # 找元素之前等一会
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        """
        点击元素的方法
        :param loc:  元组
        :return: 无
        """
        self.find_element(loc).click()

    def input_edit_content(self, loc, content):
        """
        向输入框里面输入内容
        :param loc: 元组
        :param content: 输入内容
        :return:
        """
        input_element = self.find_element(loc)
        input_element.clear()
        input_element.send_keys(content)

    def get_toast(self, message):
        """
        获取提示消息
        :param message: 需要查找的吐司信息
        :return:  返回吐司文本
        """
        try:
            xpath = "//*[contains(@text,'{}')]".format(message)
            toast_message = self.search_element((By.XPATH,xpath), timeout=5, poll=0.1)
            return toast_message.text
        except Exception as e:
            return False