from selenium import webdriver
from config.logout_page import logout
from packages.login import Login

class Logout():
    def __init__(self, driver):
        self.driver = driver
        self.log = Login(self.driver)
        self.logout = logout(self.driver)

    def logout_suss(self):
        self.log.login_suss()
        self.logout.click_logout_select()
        self.logout.click_exit()
        self.logout.logout_suss_assert()

    def logout_fail(self):
        import time
        self.log.login_suss()
        self.logout.click_logout_select()
        time.sleep(2)
        self.logout.logout_fail_assert()




if __name__ == '__main__':
    driver = webdriver.Chrome()
    log = Logout(driver)
    log.logout_suss()

