from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class Base():

    def __init__(self,driver:webdriver.Chrome):
        self.timeout = 10
        self.driver = driver
        self.t = 0.5
    #
    # def findElementNew(self,loctor):
    #     ele = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(*loctor))
    #     return ele


    def findElement(self,*loctor):
        # ele = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*loctor))
        element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loctor))
        return element

    def sendKeys(self,locar,text):
        ele = self.findElement(locar)
        ele.send_keys(text)

    def click(self,locar):
        ele = self.findElement(locar)
        ele.click()

    def clear(self,locar):
        ele = self.findElement(locar)
        ele.clear()

    def isSelected(self,locar):
        ele = self.findElement(locar)
        r = ele.is_selected()
        return r

    def idElenentExist(self,loc):
        try:
            self.findElement(loc)
        except:
            return False

    def isElementExit2(self,loc):
        ele = self.findElement(loc)
        n = len(ele)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print('定位到%s'%n)
            return True

    def houtu(self):
        self.driver.back()

    def is_title(self,_loc):
        '''
        返回bool值
        :param loc:
        :return:
        '''
        result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_loc))
        return result


    def is_text(self,loc,text):
        result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(loc,text))
        return result

    def move_to_element(self,loc):
        ''' 鼠标悬停操作事件'''
        ele = self.findElement(loc)
        ActionChains(driver).move_to_element(ele).perform()


    def select_index(self,loc,index=0):
        '''通过索引定位，默认第一个'''
        ele = self.findElement(loc)
        Select(ele).deselect_by_index(index)


    def select_Value(self,loc,value):
        '''通过value定位'''
        ele = self.findElement(loc)
        Select(ele).deselect_by_value(value)


    def select_text(self,loc,text):
        '''通过文本定位'''
        ele = self.findElement(loc)
        Select(ele).deselect_by_visible_text(text)

    def js_gundong_300(self):
        '''滚动页面'''
        js = "var q=document.documentElement.scrollTop=300"

        self.driver.execute_script(js)

    def js_top(self,number):
        '''滚动顶部'''
        body = number
        js = "var q=document.documentElement.scrollTop=%s"%body

        self.driver.execute_script(js)

    def js_end(self):
        '''滚动底部'''
        js = "var q=document.documentElement.scrollTop=100000"

        self.driver.execute_script(js)
    def js_fousc(self,loctor):
        '''聚焦元素'''
        taager = self.findElement(loctor)
        self.driver.execute_script("arguments[0].scrollIntoView();", taager)







if __name__ == '__main__':
    import json
    driver = webdriver.Chrome()
    driver.get('https://www.tapd.cn/cloud_logins/login')
    tf = Base(driver)
    # import json
    # fb = open('../data/Elements.json')
    # data = json.load(fb)
    # print(data['send_user']['user_ele'])
    # loc1 = (data['send_user']['user_ele'])
    # loc2 = (data['send_paw']['psw_ele'])
    # loc3 = (data['sub']['sub_ele'])


    loc1 = ('id', 'username')
    loc2 = ('id', 'password_input')
    loc3 = ('id', 'tcloud_login_button')

    tf.sendKeys(loc1,'fanghongju')
    tf.sendKeys(loc2,'fanghongju')
    tf.click(loc3)
    # # tf.findElement(loc1).send_keys('fanghongju@sunmi.com')
    # # tf.findElement(loc2).send_keys('Fhj100861')
    # # tf.findElement(loc3).click()
    # t = driver.title
    # print(t)