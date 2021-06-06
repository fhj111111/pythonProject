from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('https://www.12306.cn/index/')
time.sleep(4)

driver.find_element_by_id('fromStationText').send_keys('上海南',Keys.ENTER)
driver.find_element_by_id('toStationText').send_keys('北京西',Keys.ENTER)



# js_cf ="document.getElementById('fromStationText').value='上海南'"
# driver.execute_script(js_cf)
# time.sleep(5)
# js_dd = "document.getElementById('toStationText').value='北京西'"
# driver.execute_script(js_dd)
time.sleep(5)
js_time = '''document.getElementById('train_date').removeAttribute('readonly')
          document.getElementById('train_date').value="2020-11-25"'''
driver.execute_script(js_time)



driver.find_element_by_id('search_one').click()

