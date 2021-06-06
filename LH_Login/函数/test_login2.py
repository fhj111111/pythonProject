from selenium import webdriver
import unittest
from 函数.login import *

class LoginCase1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login1(self):
        '''
        登录功能
        :return:
        '''
        login(self.driver)

