import time
import os.path
import webbrowser
from icecream import ic

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.time = 0.5
        self.timeout = 15


    def urls(self,url):
        return self.driver.get(url)

    def find_element(self, *locator):
        # 封装定位元素
        try:
            # ele = WebDriverWait(self.driver, self.timeout, self.time).until(lambda x: x.find_element(*locator))
            ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
            return ele
        except Exception as e:
            print('定位未找到元素', e)

    def find_elements(self, *locator):
        # 封装定位元素
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.time).until(lambda x: x.find_elements(*locator))
            return ele
        except Exception as e:
            print('定位未找到元素', e)

    def send_keys(self, locator, text):
        # 封装输入事件
        try:
            ele = self.find_element(*locator)
            ele.send_keys(text)
        except Exception as e:
            print('输入事件失败', e)

    def clicks(self, locator):
        # 封装点击事件
        try:
            ele = self.find_element(*locator)
            ele.click()
        except Exception as e:
            print('点击元素未找到', e)

    def clears(self, locator):
        # 封装清除事件
        try:
            ele = self.find_element(locator)
            ele.clear()
        except Exception as e:
            print('清除元素没找到', e)

    def assert_text(self, locator):
        try:
            yt = self.find_element(*locator).text
            time.sleep(2)
            return yt
        except Exception as e:
            print('断言文本失败', e)

    def quits(self):
        # 退出浏览器
        try:
            self.driver.quit()
        except Exception as e:
            print('退出浏览器失败', e)

# if __name__ == '__main__':
    # from selenium import webdriver
    # # url = 'http://www.test.loonglink.net/user/login'
    # # name_ele = (By.XPATH, "//*[@type='text']")  # 账号输入框定位
    # # pas_ele = (By.XPATH, "//*[@type='password']")  # 密码输入框定位
    # # submit = (By.XPATH, "//*[@class='el-button ll-button submit-button el-button--primary']/span")  # 点击定位
    # # login_err = (By.XPATH, "//*[@class='el-button ll-button submit-button el-button--primary']/span")  # 登录失败断言定位
    # # login_sus = (By.XPATH, "//*[@class='login-button logout']")  # 登录成功断言定位
    # import yaml
    # from data_config.readexcel import OpenYaml
    # l = BasePage(driver=webdriver.Chrome())
    # file = open('../data/page_data.yaml', 'r')
    # ic(file)
    # data = yaml.load(file)
    # lo_url =  'http://www.test.loonglink.net/user/login'
    # username =data['login']['name']
    # ic(username)
    # print(lo_url)
    # l.driver.get(lo_url)
    # # l.find_element(username)
    # # print(l)
    # xpth = data['login']['type']
    # ele = data['login']['name']
    # loc = (xpth,ele)
    # l.find_element(By.XPATH,lo_url)
    # ll = l.find_element(loc,username)
    # ll.send_keys('123')