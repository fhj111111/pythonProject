import unittest
from 函数.login import *


class LoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_login(self):
        '''
        登录功能
        :return:
        '''
        login(self.driver)
        login1(self.driver,'','')