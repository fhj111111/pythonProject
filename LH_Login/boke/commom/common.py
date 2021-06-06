from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver


class Base():

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElement(self, locaet):
        ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locaet))
        return ele

    def sendKeys(self, locaet, test):
        ele = self.findElement(locaet)
        ele.send_keys(test)

    def click(self, locaet):
        els = self.findElement(locaet)
        els.click()

if __name__ == '__main__':
    driver =  webdriver.Chrome()
    driver.get('https://www.tapd.cn/cloud_logins/login')
    ct = Base(driver)
    # driver.find_element_by_id('username').send_keys('fanghongju@sunmi.com')
    # driver.find_element_by_id('password_input').send_keys('Fhj100861')
    # driver.find_element_by_id('tcloud_login_button').click()
    # driver.save_screenshot('错误截图.png')
    loc1 = (By.ID,'username')
    loc2 = (By.ID,'password_input')
    loc3 = (By.ID,'tcloud_login_button')
    ct.sendKeys(loc1,'fanghongju@sunmi.com')
    ct.sendKeys(loc2,'Fhj100861')
    ct.click(loc3)