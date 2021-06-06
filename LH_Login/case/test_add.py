from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
import time

class ZenTaoBug(Base):

    '''
    登录定位
    '''
    loc1 = (By.ID, 'username')
    loc2 = (By.ID, 'password_input')
    loc3 = (By.ID, 'tcloud_login_button')


    loc_add1 = (By.ID,'quick-create-li')  # 点击快速添加
    loc_add2 = (By.ID,'quickly-add-input') # 输入标题需求
    loc_add3 = (By.XPATH,"//*[@class='dk_select dk_cover']") # 点击选择优先级下拉框
    loc_add4 = (By.XPATH,"/html/body/div[12]/div[2]/table/tbody/tr[2]/td") # 选择优先级
    loc_add5 = (By.XPATH,'//*[@id="storyOwnerValue"]') # 添加处理人
    loc_add6 = (By.XPATH,"//*[@type='submit' and @value ]") # 点击添加

    def login(self,user='fanghongju@sunmi.com',psw='Fhj100861'):
        self.driver.get('https://www.tapd.cn/30022210/prong/stories/stories_list')
        self.sendKeys(self.loc1,user)
        self.sendKeys(self.loc2,psw)
        self.click(self.loc3)
        time.sleep(3)
        self.js_gundong_300()

    def add_bug(self,title='提交bug',name='666'):
        self.click(self.loc_add1)
        self.sendKeys(self.loc_add2,title)
        self.click(self.loc_add3)
        self.click(self.loc_add4)
        self.sendKeys(self.loc_add5,name)
        self.click(self.loc_add6)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # driver.get('https://www.tapd.cn/30022210/prong/stories/stories_list')
    bug = ZenTaoBug(driver)
    bug.login()
    bug.add_bug()