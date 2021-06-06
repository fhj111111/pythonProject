from New_login.login_zentap import LoginZenTao
from selenium import webdriver
import unittest
import time


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.zento = LoginZenTao(cls.driver)

    def setUp(self):
        self.driver.get('https://www.tapd.cn/30022210/prong/stories/stories_list')

    def tearDown(self):
        self.zento.duanyan()
        self.zento.logout()
        self.zento.clare1()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        '''
        登录失败
        :return:
        '''
        time.sleep(2)
        self.zento.login('fahiqn', '4513215')

    def test_02(self):
        '''
        登录成功
        :return:
        '''
        time.sleep(2)
        self.zento.login()


if __name__ == '__main__':
    unittest.main()
