
def login(driver,user='fanghongju@sunmi.com',paw='Fhj100861'):
    driver.get('https://www.tapd.cn/cloud_logins/login')
    driver.find_element_by_id('username').send_keys(user)
    driver.find_element_by_id('password_input').send_keys(paw)
    driver.find_element_by_id('tcloud_login_button').click()




def login1(driver,user,paw):
    driver.get('https://www.tapd.cn/cloud_logins/login')
    driver.find_element_by_id('username').send_keys(user)
    driver.find_element_by_id('password_input').send_keys(paw)
    driver.find_element_by_id('tcloud_login_button').click()


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    login(driver)


