from boke.login.login import Login
from selenium import webdriver
import unittest
import time


class TestLoginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.dl = Login(cls.driver)

    def setUp(self):
        self.driver.get('https://account.cnblogs.com/signin')

    def tearDown(self):
        self.dl.logout()
        self.dl.qc()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        self.dl.send_name()
        self.dl.send_paw()
        self.dl.button()
        self.dl.dy()

    def test_02(self):
        self.dl.send_name('saidq')
        self.dl.send_paw('1231232')
        self.dl.button()
        self.dl.dy()


if __name__ == '__main__':
    unittest.main()
