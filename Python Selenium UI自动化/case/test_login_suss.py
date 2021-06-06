import unittest
from selenium import webdriver
from packages.login import Login


class Logins(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.login = Login(self.driver)

    def test_login(self):
        self.login.login_suss()

    def tearDown(self) -> None:
        self.driver.quit()
