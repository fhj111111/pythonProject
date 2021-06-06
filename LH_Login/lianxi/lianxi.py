from selenium.webdriver.common.by import By
from common.base import Base
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get('https://www.tapd.cn/cloud_logins/login')
# tf = Base(driver)

# loc1 = (By.ID, 'username')
# ell = tf.findElement(loc1)
# # 判断是否显示
# rl = ell.is_displayed()
# print(rl)
#
# ll =(By.XPATH,"//*[@class='other-login']")
# e = tf.findElement(ll)
# tt = e.is_displayed()
# print(tt)
#
# loc2 = (By.ID, 'password_input')
#
# # loc3 = (By.ID, 'tcloud_login_button')
# #
# #
# # tf.sendKeys(loc1,'fanghongju')
# # tf.sendKeys(loc2,'fanghongju')
# # tf.click(loc3)
# #
# # t = driver.title
# # print(t)
from common.base import Base
bs = Base(driver)
loc = bs.is_title ('登录-TAPD')
print(loc)
assert  True

loc1 = ('xpath','//*[@id="password_input"]')
rl = bs.is_text(loc1,'请输入密码')

loc2 = ('xpath','//*[@id="login_cn_form"]/h1')
rl1 = bs.is_text(loc2,'欢迎来到TAPD')
print(rl1)