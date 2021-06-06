from selenium import webdriver
driver = webdriver.Chrome()
import unittest
import time

class Login():

    def __init__(self,driver):
        self.driver = driver

    def send_name(self,name='fhj100861'):
        self.driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys(name)

    def send_paw(self,paw='Fhj100861!'):
        self.driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(paw)

    def button(self):
        self.driver.find_element_by_xpath('/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/div/app-sign-in/app-content-container/mat-card/div/form/div/button/span').click()

    def qc(self):
        self.driver.find_element_by_xpath('//*[@id="mat-input-0"]').clear()
        self.driver.find_element_by_xpath('//*[@id="mat-input-1"]').clear()

    def logout(self):
        self.driver.find_element_by_link_text('退出')
        alert1 = self.driver.switch_to.alert()
        print(alert1)
        time.sleep(4)
        alert1.accept()

    def dy(self):
        title1 = self.driver.title
        time.sleep(15)
        print(title1)
        if  title1 == '首页 - 园子 - 博客园':
            print('登录成功标题是：%s' %title1)
        else:
            print('登陆失败！！！')


if __name__ == '__main__':
    st = Login()
    st.send_name()
    st.send_paw()
    st.button()
    st.dy()