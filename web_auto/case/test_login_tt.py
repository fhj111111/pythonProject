from selenium import webdriver
import time
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://lanhuapp.com/web/#/user/login')

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.quit()

    def test_01(self):  # 登录成功

        self.driver.find_element_by_name('email').send_keys('fanghongju@sunmi.com')
        self.driver.find_element_by_name('password').send_keys('fhj100861')
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[1]/div[1]/button/div/div').click()
        time.sleep(3)
        self.alear()
        s = self.get_username()
        print('登录成功，结果获取:%s' % s)
        self.assertTrue(s == '哇哦，蓝湖的忠粉竟是这样的大牌！')

    def test_02(self):  # 登录失败

        self.driver.find_element_by_name('email').send_keys('fanghongju@s1unmi.com')
        self.driver.find_element_by_name('password').send_keys('fhj100861')
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[1]/div[1]/button/div/div').click()
        time.sleep(3)
        self.alear()
        t = self.get_username()
        print('登录失败，结果获取:%s' % t)
        self.assertTrue(t == '忘记密码')

    def get_username(self):
        try:
            s = self.driver.find_element_by_xpath('//*[@class="notice_feature_btn start_lanhu"]/div').text
            time.sleep(3)
            print(s)
            return s
        except:
            t = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[1]/div[2]/span[2]').text
            time.sleep(3)
            print(t)
            return t

    def alear(self):
        try:
            s = self.driver.switch_to.alert
            t = s.text
            s.accept()
            return t
        except:
            return ''


if __name__ == '__main__':
    unittest.main()
