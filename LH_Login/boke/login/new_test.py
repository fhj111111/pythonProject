from boke.commom.common import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.tapd.cn/cloud_logins/login')

    def tearDown(self):
        time.sleep(4)
        self.driver.quit()

    def test_1(self):
        st = Base(self.driver)
        loc1 = (By.ID, 'username')
        loc2 = (By.ID, 'password_input')
        loc3 = (By.ID, 'tcloud_login_button')
        st.sendKeys(loc1,'fanghongju@sunmi.com')
        st.sendKeys(loc2,'Fhj100861')
        st.click(loc3)

if __name__ == '__main__':
    unittest.main()

