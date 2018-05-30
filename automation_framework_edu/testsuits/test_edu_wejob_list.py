# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.edu_homepage import HomePage
from pageobjects.edu_courselist import CourseHomePage
from pageobjects.edu_webjoblist import WebjobHomePage

class Wejob_Lists(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_wejob_course_list(self):
        homepage = HomePage(self.driver)
        # homepage.click_course()
        homepage.img_close()
        time.sleep(2)
        self.driver.find_element_by_xpath("html/body/div[5]/ul/li[2]/p").click()
        '''courselist = CourseHomePage(self.driver)
        # courselist.course_click()
        self.driver.find_element_by_xpath("html/body/div[5]/div/div[4]/div[2]/h3/a").click()
        webjoblist = WebjobHomePage(self.driver)
        # webjoblist.wejob_click()
        self.driver.find_element_by_xpath("html/body/div[1]/div/ul/li[4]/a").click()
        webjoblist.get_windows_img()'''
if __name__ == '__main__ ':
    unittest.main()