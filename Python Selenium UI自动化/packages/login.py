from selenium import webdriver
from config.login_page import login

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.login = login(self.driver)

    def login_suss(self):
        self.login.get_url()
        self.login.send_name_suss()
        self.login.send_password()
        self.login.send_click()
        self.login.login_suss_assert()

    def login_fail(self):
        self.login.get_url()
        self.login.send_login_user_fail()
        self.login.send_password()
        self.login.send_click()

        ss = self.login.login_fail_assert()
        print(ss)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    log = Login(driver)
    # log.login_fail()
    log.login_suss()
