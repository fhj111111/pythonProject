'''
1.账号密码
2.输入账号不输入密码登录
3.输入账号，密码登录
4.点击忘记密码
'''
import ddt
import unittest
import time
from selenium import webdriver
from pages.log_page import LoginPage,log_url
from common.base import Base
from pages.add_bug_page import Add_Gbug
from common.read_excel import Excel1Util
import os

curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath = os.path.join(curpath,'common','datas.xlsx')
print(filepath)
data = Excel1Util(filepath)
testdates = data.dict_Data()
print(testdates)
@ddt.ddt
class LoginPageCase(unittest.TestCase,Base):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.loginP = LoginPage(cls.driver)
        cls.bug = Add_Gbug(cls.driver)
        cls.driver.get(log_url)

    def setUp(self):
        self.driver.get(log_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def login_case(self,user,psw,title):

        self.loginP.input_user(user)
        self.loginP.input_psw(psw)
        self.loginP.click_login_button()
        st = self.loginP.get_title()
        self.assertTrue(st == title)



    @ddt.data(*testdates)
    def test_01(self,data):
        '''1.错误账号密码'''
        print('测试数据:%s' % data)
        self.login_case(data['user'], data['psw'], data['title'])

    # def test_02(self):
    #     '''账号密码为空登录'''
    #     data2 = testdates[1]
    #     print('测试数据：%s'%data2)
    #     self.login_case(data2['user'],data2['psw'],data2['title'])
    #
    # def test_03(self):
    #     '''正确用户名密码登录'''
    #     data3 = testdates[2]
    #     print('测试数据：%s'%data3)
    #     self.login_case(data3['user'],data3['psw'],data3['title'])
    #     self.driver.save_screenshot('错误截图1.png')


if __name__ == '__main__':
    unittest.main()