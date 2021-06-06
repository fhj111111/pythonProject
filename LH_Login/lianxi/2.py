from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.keys import Keys

driver.get('file:///C:/Users/Administrator/Desktop/test.html')

all = driver.find_elements_by_xpath('//input[@type="checkbox"]') # click
st = driver.find_element_by_xpath('//input[@value="cv2"]').click()

# driver.find_element_by_xpath('//input[@value="cv2"]').send_keys(Keys.SPACE)  # send space

# if driver.find_element_by_xpath('//input[@value="cv3"]').is_displayed():
#     print('选择了')
# else:
#     print('没有选择')

all1 = driver.find_elements_by_xpath('//input[@type="checkbox"]')

def read(all):
    r = []
    for i in all:
        if i.is_selected():
            print('选中了~')
        else:
            i.click()
            r.append(i.is_selected())
    return r

at = read(all)
for i in at:
    assert i == True