from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from common.base import Base
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
tf = Base(driver)

loc1 = (By.LINK_TEXT, '设置')
ell = tf.findElement(loc1)
ActionChains(driver).move_to_element(ell).perform()
loc2 = (By.LINK_TEXT,'搜索设置')
tf.click(loc2)

loc3 = (By.XPATH,'')