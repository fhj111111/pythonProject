
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('http://flash-admin.enilu.cn/#/login')


driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('admin')
driver.find_element_by_xpath('//*[@class="el-button el-button--primary"]').click()
time.sleep(3)
driver.quit()