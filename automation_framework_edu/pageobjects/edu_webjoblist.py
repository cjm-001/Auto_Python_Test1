# coding=utf-8
from framework.base_page import BasePage

class WebjobHomePage(BasePage):
    webjob = "xpath=>html/body/div[1]/div/ul/li[4]/a"
    def wejob_click(self):
        self.click(self.webjob)
        self.sleep(2)