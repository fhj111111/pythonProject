'''
1.账号密码
2.输入账号不输入密码登录
3.输入账号，密码登录
4.点击忘记密码
'''

import unittest
import time
from selenium import webdriver
from pages.log_page import LoginPage,log_url
from common.base import Base
from pages.add_bug_page import Add_Gbug


class LoginPageCase(unittest.TestCase,Base):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.loginP = LoginPage(cls.driver)
        cls.bug = Add_Gbug(cls.driver)
        cls.driver.get(log_url)
        cls.loginP.login_1()
        # cls.driver.get(log_url)
        # a = LoginPage(cls.driver)
        # a.login_1()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        '''1.错误账号密码'''

        self.loginP.input_user('fanghongju@sunim.com')
        self.loginP.input_psw('123')
        self.loginP.click_login_button()
        st = self.loginP.get_title()
        self.assertTrue(st == '登录-TAPD' )
        # st = self.driver.title
        # if st == '登录-TAPD':
        #     print('登录失败，测试通过')
        # else:
        #     print('不是在首页位置')

    def test_02(self):
        '''账号密码为空登录'''
        self.loginP.clare_input()
        self.loginP.click_login_button()
        st = self.loginP.get_title()
        self.assertTrue(st == '登录-TAPD')

    def test_03(self):
        '''忘记密码'''
        self.loginP.wj_psw()
        st = self.loginP.get_title()
        self.assertTrue(st == '找回密码-TAPD')


    def test_04(self):
        '''正确用户名密码登录'''
        self.loginP.houtu()
        self.loginP.clare_input()
        self.loginP.input_user('fanghongju@sunmi.com')
        self.loginP.input_psw('Fhj100861')
        self.loginP.click_login_button()
        st = self.loginP.get_title()
        time.sleep(2)
        self.assertTrue(st == '我的工作台 - TAPD平台')
        self.driver.save_screenshot('错误截图1.png')
        # if self.driver.title == '我的工作台 - TAPD平台':
        #     print('页面标题是 %s , 登录成功' %self.driver.title)
        # else:
        #     print('登录失败！！！')


if __name__ == '__main__':
    unittest.main()