# coding=utf-8
from framework.base_page import BasePage

class CourseHomePage(BasePage):
    course = "xpath=>html/body/div[5]/div/div[4]/div[2]/h3/a"
    def course_click(self):
        self.click(self.course)
        self.sleep(2)