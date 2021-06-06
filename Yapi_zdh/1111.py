
import time

class Login:
    def __init__(self,driver):
        self.driver = driver


    def login(self):
        self.driver.get('http://127.0.0.1:3000/login')
        self.driver.find_element_by_xpath("//*[@type='text']").send_keys('kkkk')
        self.driver.find_element_by_xpath("//*[@type='password']").send_keys('uuuu')
        self.driver.find_element_by_xpath("//*[@type='submit']")
if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    loo = Login(driver)
    loo.login()