# coding=utf-8
import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.'))
    Chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    def __init__(self,driver):
        self.driver = driver
    def open_browser(self,driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("You had select %s browser." %browser)
        url = config.get("testServer","URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("打开火狐浏览器")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.Chrome_driver_path)
            logger.info("打开谷歌浏览器")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("打开IE浏览器")

        driver.get(url)
        logger.info("open url: %s" % url)
        driver.maximize_window()
        logger.info("最大化窗口")
        driver.implicitly_wait(10)
        logger.info("等待10s")
        return driver
    def quit_driver(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()

