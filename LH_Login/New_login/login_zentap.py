import time
class LoginZenTao():

    def __init__(self,driver):
        self.driver = driver

    def login( self,user='fanghongju@sunmi.com', paw='Fhj100861'):
        self.driver.get('https://www.tapd.cn/cloud_logins/login')
        self.driver.find_element_by_id('username').send_keys(user)
        self.driver.find_element_by_id('password_input').send_keys(paw)
        self.driver.find_element_by_id('tcloud_login_button').click()
        time.sleep(10)


    def duanyan(self):
        aler1 = self.driver.find_element_by_xpath('//*[@class="worktable-action-item filter-text"]').text
        print(aler1)
        time.sleep(5)
        if aler1 == '过滤':
            print(aler1)
            print('登录成功！！')
        else:
            print('登录失败~')

    def title1(self):
        try:
            title1 = self.driver.title
            if title1 == '我的工作台 - TAPD平台':
                print('页面标题是 %s , 登录成功' % title1)
            else:
                print('登录失败！！！')
        except:
            aler1 = self.driver.find_element_by_xpath('//*[@class="worktable-action-item filter-text"]').text
            print(aler1)
            if aler1 == '过滤':
                print(aler1)
                print('登录成功！！')
            else:
                print('登录失败~')

    def logout(self):
        time.sleep(4)
        self.driver.find_element_by_xpath('//*[@id="new_nav_avatar_div"]/a/div/i').click()
        self.driver.find_element_by_xpath('//*[@id="personal-setting-menu"]/ul/li[7]/a').click()
        # 获取页面数据

    def clare1(self):
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('password_input').clear()
        time.sleep(2)

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    DL = LoginZenTao(driver)
    DL.login()
    DL.duanyan()