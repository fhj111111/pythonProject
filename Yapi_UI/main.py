from data.read_yaml import OpenYaml
from data.base import Base
class Login:
    def __init__(self,driver):
        self.driver = driver
        self.yl = OpenYaml()
        self.ba = Base(self.driver)


    def login(self):
        u_types = (self.yl.read_yaml()['login']['user']['type'],self.yl.read_yaml()['login']['user']['ele'])
        # u_eles = self.yl.read_yaml()['login']['user']['ele']
        p_types = self.yl.read_yaml()['login']['pas']['type']
        p_eles = self.yl.read_yaml()['login']['pas']['ele']
        send = self.yl.read_yaml()['login']['u_send']['text']
        urls = self.yl.read_yaml()['login']['url']
        # sub =
        self.ba.urls(urls)
        self.ba.send_Keys(u_types,send)
        self.ba.send_Keys((p_types,p_eles),send)
        # self.driver.find_element_by_xpath("//*[@type='text']").send_keys('kkkk')
        # self.driver.find_element_by_xpath("//*[@type='password']").send_keys('uuuu')
        # self.driver.find_element_by_xpath("//*[@type='submit']")

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    loo = Login(driver)
    loo.login()
