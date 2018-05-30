# coding=utf-8
from framework.base_page import BasePage


class HomePage(BasePage):
    img_box = "xpath=>.//*[@id='pop_one']/div[2]/div/span/img"
    input_box = "id=>searchQ"
    search_submit_btn = "xpath=>.//*[@id='Search']/button"

    def img_close(self):
        self.click(self.img_box)

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)