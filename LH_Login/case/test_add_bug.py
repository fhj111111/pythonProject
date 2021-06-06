import unittest
from selenium import webdriver
from case.test_add import ZenTaoBug
import time


class Test_add_Bug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.bug = ZenTaoBug(cls.driver)
        cls.bug.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_bug1(self):
        self.bug.add_bug()
if __name__ == '__main__':
    unittest.main()