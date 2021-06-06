from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.tapd.cn/cloud_logins/login')

# ele = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_id('username'))
#
# print(ele)
#
# ele.send_keys('fanghongju@sunmi.com')
#
# ele1 = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_id('password_input'))
#
# print(ele1)
# ele1.send_keys('Fhj100861')
#
# ele2 = ele1 = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_id('tcloud_login_button'))
# ele2.click()
loctor = ('by', 'value')


def findElement(driver, loctor, timeout=10, t=0.5):
    ele = WebDriverWait(driver, 10, 1).until(lambda x: x.find_element(*loctor))
    return ele

driver.find_element(By.ID, 'username')
driver.find_element(By.ID, 'password_input')
driver.find_element(By.ID, 'tcloud_login_button')

loc1 = (By.ID, 'username')
loc2 = (By.ID, 'password_input')
loc3 = (By.ID, 'tcloud_login_button')

findElement(driver, loc1).send_keys('fanghongju@sunmi.com')
findElement(driver, loc2).send_keys('Fhj100861')
findElement(driver, loc3).click()
