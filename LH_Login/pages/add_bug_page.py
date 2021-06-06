from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
from pages.log_page import LoginPage
import time


class Add_Gbug(Base):
    loc_add1 = (By.ID, 'quick-create-li')  # 点击快速添加
    loc_add2 = (By.ID, 'quickly-add-input')  # 输入标题需求
    loc_add3 = (By.XPATH, "//*[@class='dk_select dk_cover']")  # 点击选择优先级下拉框
    loc_add4 = (By.XPATH, "/html/body/div[12]/div[2]/table/tbody/tr[2]/td")  # 选择优先级
    loc_add5 = (By.XPATH, '//*[@id="storyOwnerValue"]')  # 添加处理人
    loc_add6 = (By.XPATH, "//*[@type='submit' and @value ]")  # 点击添加

    def add_click_biaoti(self):
        self.click(self.loc_add1)

    def add_bug_biaoti(self, title='Bug 标题'):
        self.sendKeys(self.loc_add2, title)

    def add_serch_xialakuang(self):
        self.click(self.loc_add3)

    def add_select_xailakuang(self):
        self.click(self.loc_add4)

    def add_chuliren(self, name='小花'):
        self.sendKeys(self.loc_add5, name)

    def add_submit(self):
        self.click(self.loc_add6)
        # self.js_top(10)

    def add_bug_1(self):
        time.sleep(3)
        self.add_click_biaoti()
        self.add_bug_biaoti()
        self.add_serch_xialakuang()
        self.add_select_xailakuang()
        self.add_chuliren()
        self.add_submit()



if __name__ == '__main__':
    driver = webdriver.Chrome()
    bug1 = Add_Gbug(driver)

    from pages.log_page import LoginPage

    a = LoginPage(driver)
    a.login_1()

    timest = time.strftime('%Y_%m_%d_%H_%M_%S')
    time.sleep(3)
    bug1.add_bug_1()
