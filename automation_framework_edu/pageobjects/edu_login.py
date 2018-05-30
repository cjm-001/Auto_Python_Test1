# coding=utf-8
from selenium import webdriver

class login_go(object):
    u'''登录类封装'''
    def __init__(self,driver):
        u'''初始化driver参数'''
        self.driver = driver
    def login(self,username,password):
        u'''输入用户名和密码,点击登录'''
        self.driver.find_element_by_id("loginform-username").clear()
        self.driver.find_element_by_id("loginform-username").send_keys(username)
        self.driver.find_element_by_id("loginform-password").clear()
        self.driver.find_element_by_id("loginform-password").send_keys(password)
        self.driver.find_element_by_id("login-form").click()