from selenium import  webdriver
import time
from common.base import Base
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
st = Base(driver)
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(4)

loc = (By.XPATH,'//*[@id="page"]/div/a[3]/span[2]')
st.js_fousc(loc)

# # 登录
# driver.find_element_by_id('username').send_keys('fanghongju@sunmi.com')
# driver.find_element_by_id('password_input').send_keys('Fhj100861')
# driver.find_element_by_id('tcloud_login_button').click()
# driver.save_screenshot('错误截图.png')
#
# # loc_add1 = (By.ID, 'quick-create-li')  # 点击快速添加
# #loc_add6 = (By.XPATH,('//*[@id="quickly-add-input"]') # 输入标题
# # loc_add2 = (By.ID, 'quickly-add-input')  # 输入标题需求
# # loc_add3 = (By.XPATH, "//*[@class='dk_select dk_cover']")  # 选择优先级
# # loc_add4 = (By.XPATH, '//*[@id="storyOwnerValue"]')  # 添加处理人
# # loc_add5 = (By.XPATH, "//*[@type='submit' and @value ]")  # 点击添加
#
# driver.find_element_by_id('quick-create-li').click()
# driver.find_element_by_xpath('//*[@id="quickly-add-input"]').send_keys('这是一个问题')
# driver.find_element_by_xpath("//*[@class='dk_select dk_cover']").click()
# driver.find_element_by_xpath("/html/body/div[12]/div[2]/table/tbody/tr[2]/td").click()
# driver.find_element_by_xpath('//*[@id="storyOwnerValue"]').send_keys('李四')
# driver.find_element_by_xpath("//*[@type='submit' and @value ]").click()
#
#
# # # 退出登录
#
# # time.sleep(4)
# # driver.find_element_by_xpath('//*[@id="new_nav_avatar_div"]/a/div/i').click()
# # driver.find_element_by_xpath('//*[@id="personal-setting-menu"]/ul/li[7]/a').click()
# # 获取页面数据
# time.sleep(4)
# #
# # # 断言页面数据
# #
# # aler1 = driver.find_element_by_xpath('//*[@class="worktable-action-item filter-text"]').text
# # print(aler1)
# #
# # if aler1 == '过滤':
# #     print(aler1)
# #     print('登录成功！！')
# # else:
# #     print('登录失败~')
# #
# # title1 = driver.title
# # # print(title1)
# # if  title1 == '我的工作台 - TAPD平台':
# #     print('页面标题是 %s , 登录成功' %title1)
# # else:
# #     print('登录失败！！！')
#
#
#
#
