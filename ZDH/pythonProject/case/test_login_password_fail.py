import unittest
from config.login import login_obj

from selenium import webdriver


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_suss = login_obj(self.driver)

    def test_login(self):
        self.login_suss.login_password_fail()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()