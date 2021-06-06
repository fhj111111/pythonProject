from pages.log_page import LoginPage,log_url
from pages.add_bug_page import Add_Gbug
from selenium import webdriver
import unittest
import time

class Add_Bug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.bug = Add_Gbug(cls.driver)
        a = LoginPage(cls.driver)
        a.login_1()

    def test_Add_bug(self):
        self.bug.add_bug_1()

if __name__ == '__main__':
    unittest.main()