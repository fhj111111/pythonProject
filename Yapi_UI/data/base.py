from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    def urls(self, url):
        return self.driver.get(url)

    def find_Element(self, *loc):
        ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
        return ele

    def send_Keys(self, loc, text):
        ele = self.find_Element(*loc)
        ele.send_keys(text)


    def assert_text(self, loc, tex):
        tx = self.find_Element(loc).text
        if tx == tex:
            print('断言成功，断言文本是%s' % tex)
        else:
            print('断言失败，应当文本是%s' % tx)
