import unittest
import time
from selenium import webdriver

 
class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.tapd.cn/cloud_logins/login')

    def tearDowm(self):
        time.sleep(4)
        # self.driver.close()
        self.driver.quit()

    def test1(self):
        self.driver.find_element_by_id('username').send_keys('fanghongju@sunmi.com')
        self.driver.find_element_by_id('password_input').send_keys('Fhj100861')
        self.driver.find_element_by_id('tcloud_login_button').click()
        time.sleep(10)
        self.logout()
    def test_02(self):

        self.driver.find_element_by_id('username').send_keys('fan2ghongju@sunmi.com')
        self.driver.find_element_by_id('password_input').send_keys('Fhj100861')
        time.sleep(10)
        self.driver.find_element_by_id('tcloud_login_button').click()
        time.sleep(10)
        self.logout()

    def logout(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="new_nav_avatar_div"]/a/div/i').click()
            time.sleep(10)
            self.driver.find_element_by_xpath('//*[@id="personal-setting-menu"]/ul/li[7]/a').click()
            xt = self.driver.title('登录-TAPD')
            print(xt)
        except:
            print('登录失败！！！')

if __name__ == '__main__':
    unittest.main()