import unittest
from packages.login import Login
from selenium import webdriver

class Login_fail(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.login_fail = Login(self.driver)

    def test_login_fail(self):
        self.login_fail.login_fail()

    def tearDown(self) -> None:
        self.driver.quit()