from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
import time
log_url = 'https://www.tapd.cn/30022210/prong/stories/stories_list'


class LoginPage(Base):

    '''
    登录定位
    '''
    loc_user = (By.ID, 'username')
    loc_psw = (By.ID, 'password_input')
    loc_button = (By.ID, 'tcloud_login_button')
    loc_WJpsw = (By.XPATH,"//*[@id='forget_password']")




    def input_user(self,text):
        self.sendKeys(self.loc_user,text)


    def input_psw(self,text):
        self.sendKeys(self.loc_psw,text)

    def click_login_button(self):
        self.click(self.loc_button)

    def clare_input(self):
        self.clear(self.loc_user)
        self.clear(self.loc_psw)

    def wj_psw(self): # 忘记密码
        self.click(self.loc_WJpsw)

    def get_title(self):
        title1 = self.driver.title
        return title1

    def login_1(self,user='fanghongju@sunmi.com', psw='Fhj100861'):
        '''登录流程'''

        self.driver.get(log_url)
        self.input_user(user)
        self.input_psw(psw)
        self.click_login_button()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    log_page = LoginPage(driver)
    # driver.get('https://www.tapd.cn/cloud_logins/login')
    # log_page.input_user('fanghongju@sunmi.com')
    # log_page.input_psw('Fhj100861')
    # log_page.click_login_button()
    log_page.login_1()