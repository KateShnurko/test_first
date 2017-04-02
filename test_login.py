# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_login(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("https://phlatbed.dev.cleveroad.com/")

    def login(self, wd, group):
        wd.find_element_by_link_text("LOGIN").click()
        wd.find_element_by_xpath("//div[@id='login-modal']/div/form/div[1]/input").click()
        wd.find_element_by_xpath("//div[@id='login-modal']/div/form/div[1]/input").clear()
        wd.find_element_by_xpath("//div[@id='login-modal']/div/form/div[1]/input").send_keys(group.email)
        wd.find_element_by_xpath("//div[@id='login-modal']/div/form/div[2]/input").click()
        wd.find_element_by_xpath("//div[@id='login-modal']/div/form/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@id='login-modal']/div/form/div[2]/input").send_keys(group.password)
        wd.find_element_by_css_selector("button.login-btn").click()

    def open_edit_profile_page(self, wd):
        wd.find_element_by_css_selector("div.arrow.dropdown-toggle").click()
        wd.find_element_by_link_text("Edit profile").click()
    
    def test_login_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd,  Group(email="user@gmail.com", password="qwerty1"))
        self.open_edit_profile_page(wd)

    def test_login_incorrect_credentials(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd,  Group(email="notexist@gmail.com", password="123qwe"))

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
