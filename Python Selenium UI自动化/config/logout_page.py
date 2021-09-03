from selenium import webdriver
from base.find_element import base
from config.open_yaml import open_yaml
from packages.login import Login
import time


class logout:

    def __init__(self, driver):
        self.driver = driver
        self.yaml = open_yaml()
        self.logs = Login(self.driver)
        self.base = base(self.driver)

    def click_logout_select(self):
        """
        点击弹出登出下拉框
        :return:
        """
        xp = self.yaml.open_data()['logout']['click']['type']
        ele = self.yaml.open_data()['logout']['click']['ele']
        self.base.click((xp, ele))

    def click_exit(self):
        """
        点击登出账号
        :return:
        """
        xp = self.yaml.open_data()['logout']['exit']['type']
        ele = self.yaml.open_data()['logout']['exit']['ele']
        ele2 = self.yaml.open_data()['logout']['exit']['ele2']
        one = self.base.click((xp, ele))
        tow = self.base.click((xp, ele2))
        if one == True:
            self.base.click((xp, ele))
        else:
            self.base.click((xp, ele2))

    def logout_fail_assert(self):
        """
        登出失败断言
        :return:
        """
        text = self.yaml.open_data()['logout']['text']['text_exit_fail']

        if self.base.find_title() == text:
            print('断言成功文字内容:%s' % self.base.find_title())
        else:
            print('断言失败未找到内容:%s' % self.base.find_title())

    def logout_suss_assert(self):
        """
        登出成功断言
        :return:
        """
        text = self.yaml.open_data()['logout']['text']['text_exit_suss']

        if self.base.find_title() == text:
            print('断言成功文字内容:%s' % self.base.find_title())
        else:
            print('断言失败未找到内容:%s' % self.base.find_title())


if __name__ == '__main__':
    driver = webdriver.Chrome()
    log = logout(driver)
    log.logs.login_suss()
    log.click_logout_select()
    log.click_exit()
    # import time
    # time.sleep(4)
    # log.logout_suss_assert()