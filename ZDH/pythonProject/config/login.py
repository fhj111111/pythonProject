from selenium import webdriver
from data_config.readexcel import OpenYaml
from basepages.base_page import BasePage
from icecream import ic
import time


class login_obj():
    def __init__(self, driver):
        self.op = OpenYaml()
        self.driver = driver
        self.bp = BasePage(self.driver)

    def login_url(self):
        url = self.op.getdata()['login']['url']
        ic(url)
        self.bp.urls(url)

    def username_fail(self):
        xp = self.op.getdata()['login']['username']['type']
        ele = self.op.getdata()['login']['username']['name']
        send1_t = self.op.getdata()['login']['user_pas']['user_fail']
        ic(xp,ele,send1_t)
        self.bp.send_keys((xp, ele), send1_t)

    def username_suss(self):
        xp = self.op.getdata()['login']['username']['type']
        ele = self.op.getdata()['login']['username']['name']
        send1_t = self.op.getdata()['login']['user_pas']['user_suss']
        ic(xp,ele,send1_t)

        self.bp.send_keys((xp, ele), send1_t)

    def password_fail(self):
        xp = self.op.getdata()['login']['password']['type']
        ele = self.op.getdata()['login']['password']['name']
        send1_t = self.op.getdata()['login']['user_pas']['pas_fail']
        ic(xp,ele,send1_t)

        self.bp.send_keys((xp, ele), send1_t)

    def password_suss(self):
        xp = self.op.getdata()['login']['password']['type']
        ele = self.op.getdata()['login']['password']['name']
        send1_t = self.op.getdata()['login']['user_pas']['pas_suss']
        ic(xp,ele,send1_t)

        self.bp.send_keys((xp, ele), send1_t)

    def sublime(self):
        xp = self.op.getdata()['login']['sub']['type']
        ele = self.op.getdata()['login']['sub']['name']
        ic(xp,ele)

        self.bp.clicks((xp,ele))

    def login_err_text(self):
        xp = self.op.getdata()['login']['login_err']['type']
        ele = self.op.getdata()['login']['login_err']['name']
        text = self.op.getdata()['login']['login_err']['login_fail_text']
        # 登录失败断言
        login_er = self.bp.assert_text((xp,ele))
        time.sleep(2)
        if login_er == text:
            print('断言成功文字内容是"%s"' % login_er)
        else:
            print('断言失败，未找到"%s"' % login_er)

    def login_suss_text(self):
        xp = self.op.getdata()['login']['login_suss']['type']
        ele = self.op.getdata()['login']['login_suss']['name']
        text = self.op.getdata()['login']['login_suss']['login_fail_text']
        # 登录失败断言
        login_er = self.bp.assert_text((xp,ele))
        time.sleep(2)
        if login_er == text:
            print('断言成功文字内容是"%s"' % login_er)
        else:
            print('断言失败，未找到"%s"' % login_er)


    def login_suss(self):
        self.login_url()
        self.username_suss()
        self.password_suss()
        self.sublime()
        self.login_suss_text()

    def login_password_fail(self):
        self.login_url()
        self.username_suss()
        self.password_fail()
        self.sublime()
        self.login_err_text()

    def login_name_fail(self):
        # 登录失败，账号错误
        self.login_url()
        self.username_fail()
        self.password_suss()
        self.sublime()
        self.login_err_text()

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     l = login_obj(driver)
#     l.login_url()
#     l.login_name_fail()
