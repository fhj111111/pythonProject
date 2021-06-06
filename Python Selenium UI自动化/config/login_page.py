from selenium import webdriver
from base.find_element import base
from config.open_yaml import open_yaml
import time
class login:

    def __init__(self,driver):
        self.driver = driver
        self.yaml = open_yaml()
        self.base = base(self.driver)

    def send_name_suss(self):
        """
        获取user定位
        :return:
        """
        xp = self.yaml.open_data()['login']['username']['type']
        ele = self.yaml.open_data()['login']['username']['user']
        text = self.yaml.open_data()['login']['text']['text']
        self.base.find_send((xp,ele),text)

    def send_password(self):
        """
        获取密码定位
        :return:
        """
        xp = self.yaml.open_data()['login']['username']['type']
        ele = self.yaml.open_data()['login']['password']['pass']
        text = self.yaml.open_data()['login']['text']['text']
        self.base.find_send((xp, ele), text)

    def send_login_user_fail(self):
        '''
        登录失败操作
        :return:
        '''
        xp = self.yaml.open_data()['login']['username']['type']
        ele = self.yaml.open_data()['login']['username']['user']
        text = self.yaml.open_data()['login']['text']['test_fail']
        self.base.find_send((xp, ele), text)

    def send_click(self):
        """
        点击操作
        :return:
        """
        xp = self.yaml.open_data()['login']['subimt']['type']
        ele = self.yaml.open_data()['login']['subimt']['subimt']
        self.base.click((xp,ele))
    def get_url(self):
        """
        获取URL
        :return:
        """
        url = self.yaml.open_data()['login']['url']['url']
        self.base.url(url)

    def login_suss_assert(self):
        xp = self.yaml.open_data()['login']['title_suss']['type']
        ele = self.yaml.open_data()['login']['title_suss']['ele']
        text = self.yaml.open_data()['login']['title_suss']['text']
        login_su = self.base.assert_text((xp,ele))
        time.sleep(5)
        if login_su == text:
            print('断言成功文字内容:%s'%login_su)
        else:
            print('断言失败未找到内容:%s'%login_su)

    def login_fail_assert(self):
        xp = self.yaml.open_data()['login']['title_suss']['type']
        ele = self.yaml.open_data()['login']['title_fail']['ele']
        text = self.yaml.open_data()['login']['title_fail']['text']
        login_fail = self.base.assert_text((xp,ele))
        time.sleep(3)
        if login_fail == text:
            print('断言成功文字内容:%s' % login_fail)
        else:
            print('断言失败未找到内容:%s' % login_fail)





if __name__ == '__main__':
    driver = webdriver.Chrome()
    log = login(driver)
    log.get_url()
    log.login_fail_assert()