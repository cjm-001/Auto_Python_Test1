# coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from framework.logger import Logger

# create a logger instance
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

        # quit browser and end testing

    def quit_browser(self):
        self.driver.quit()