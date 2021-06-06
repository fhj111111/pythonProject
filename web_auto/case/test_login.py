from selenium import webdriver
import time
import unittest


class LongTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.get('https://www.tapd.cn/cloud_logins/login')

    def tearDown(self):
        self.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.quit()

    def test_01(self):

        self.driver.find_element_by_id('username').send_keys('fanghongju@sunmi.com')
        self.driver.find_element_by_id('password_input').send_keys('Fhj100861')
        self.driver.find_element_by_id('tcloud_login_button').click()

        # 判断是否成功
        time.sleep(4)
        s = self.get_login_username()
        print('登录成功，获取结果：%s' % s)
        self.assertTrue(s == '新需求')

    def test_02(self):

        self.driver.find_element_by_id('username').send_keys('fan2ghongju@sunmi.com')
        self.driver.find_element_by_id('password_input').send_keys('Fhj100861')
        self.driver.find_element_by_id('tcloud_login_button').click()

        # 判断是否成功
        time.sleep(4)
        t = self.get_login_username()
        print('登录失败，获取结果：%s' % t)
        self.assertTrue(t == '邮箱或手机不存在')

    def get_login_username(self):
        try:
            s = self.driver.find_element_by_xpath("//*[text()='新需求']").text
            print(s)
            return s
        except:
            t = self.driver.find_element_by_id('error-tips').text
            print(t)
            return t

    def is_alert_exist(self):
        ''' 判断是否有弹窗'''
        try:
            alet = self.driver.switch_to.alert
            text = alet.text
            alet.accept()

            return text
        except:
            return ''


if __name__ == '__main__':
    unittest.main()
