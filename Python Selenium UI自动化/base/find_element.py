import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class base:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def url(self, url):
        return self.driver.get(url)

    def find_title(self):
        """
        获取标题
        :param text:
        :return:
        """
        return self.driver.title

    def find_element(self, *loc):
        STYLE = "background: green; border: 2px solid red;"  # 高亮的样式

        try:
            ele = WebDriverWait(self.driver, 6, 0.5).until(EC.presence_of_element_located(*loc))
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", ele, STYLE)
            return ele
        except Exception as e:
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('../img/%s.png' % nowTime)
            print('定位未找到元素已截图:%s' % e)

    def find_elements(self, *loc):
        try:
            STYLE = "background: green; border: 2px solid red;"  # 高亮的样式
            ele = WebDriverWait(self.driver, 6, 0.5).until(EC.presence_of_all_elements_located(*loc))
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", ele, STYLE)
            return ele
        except Exception as e:
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('../img/%s.png' % nowTime)
            print('定位未找到元素已截图:%s' % e)

    def find_send(self, loc, text):
        # 封装输入事件

        try:
            ele = self.find_element(loc)
            ele.send_keys(text)
        except Exception:
            print('元素定位失败%s,无法输入的内容是：%s' % (loc, text))

    def click(self, loc):

        try:
            ele = self.find_element(loc)
            ele.click()
        except Exception:
            print('点击元素定位失败未找到：', loc)

    def find_select(self, loc, index):
        """
        :param loc:
        :param index: 根据索引选择内容  注意索引从0开始
        :return:
        """
        try:
            select = Select(self.find_element(loc))
            select.select_by_index(index)
        except Exception:
            print('元素定位失败%s,无法输入的内容是：%s' % (loc, index))

    def find_select_text(self, loc, text):
        """
        :param loc:
        :param text: 根据text选择内容
        :return:
        """
        try:
            select = Select(self.find_element(loc))
            select.select_by_visible_text(text)
        except Exception:
            print('元素定位失败%s,无法输入的内容是：%s' % (loc, text))

    def find_select_value(self, loc, value):
        """
        :param loc:  元素定位
        :param value: 根据value值选择内容
        :return:
        """
        try:
            select = Select(self.find_element(loc))
            select.select_by_value(value)
        except Exception:
            print('元素定位失败%s,无法输入的内容是：%s' % (loc, value))

    def find_del_select(self, loc):
        """
        :param loc:
        :return: 取消原来的选择
        """
        try:
            select = Select(self.find_element(loc))
            select.deselect_all()
        except Exception:
            print('元素定位失败%s,无法输入的内容是：%s' % loc)

    def find_move(self, loc1, loc2):
        try:
            element = self.driver.find_element(loc1)
            target = self.driver.find_element(loc2)
            action_chains = ActionChains(self.driver)
            action_chains.drag_and_drop(element, target).perform()
        except Exception:
            print('元素定位失败%s,无法输入的内容是：%s' % (loc1, loc2))

    def find_alert_accept(self):
        '''接受弹窗'''
        try:
            alert = self.driver.switch_to.alert().accept()
            return alert
        except:
            print('弹窗接受失败，没有找到')

    def find_alert_text(self):
        '''获取弹窗消息'''
        try:
            alert = self.driver.switch_to.alert().text
            return alert
        except:
            print('获取弹窗消息失败，没有找到')

    def find_alert_dismiss(self):
        '''取消弹窗'''
        try:
            alert = self.driver.switch_to.alert().dismiss()
            return alert
        except:
            print('取消弹窗失败，没有找到')

    def find_alert_ouput(self, text):
        '''弹窗输入内容'''
        try:
            alert = self.driver.switch_to.alert().send_keys(text)
            return alert
        except:
            print('弹窗输入内容失败，没有找到')

    def find_windows_handles(self):
        """
        切换浏览器Tab页
        :return:
        """
        try:
            window_1 = driver.current_window_handle  # 获得打开的第一个窗口句柄
            windows = driver.window_handles  # 获得打开的所有的窗口句柄
            for current_window in windows:
                if current_window != window_1:
                    driver.switch_to.window(current_window)
        except:
            print('页面切换失败')

    def find_frame_enter(self, text):
        '''
        :param text: ifrname 切换
        :return: 可以用 定位元素/索引
        '''
        try:
            frame = driver.switch_to.frame(text)
            return frame
        except:
            print('切换frame 失败')

    def find_frame_exit(self):
        """
        :return: 退出frame
        """
        try:
            frame = driver.switch_to.default_content()
            return frame
        except:
            print('退出frame失败')

    def assert_text(self, loc):
        """
       :param loc:
        :return: selenium 断言
        """
        ele = self.find_element(loc).text
        time.sleep(2)
        return ele
        # try:
        #
        # except Exception as e:
        #     print('断言文本失败', e)


if __name__ == '__main__':
    from selenium import webdriver

    url = 'http://flash-admin.enilu.cn/#/login'
    username = (By.NAME, 'username')
    password = ('name', 'password')
    submit = (By.XPATH, '//*[@class="el-button el-button--primary"]')
    text1 = 'admin'
    import time

    driver = webdriver.Chrome()
    print(time.thread_time())
    ls = base(driver)
    ls.url(url)
    # ls.find_send(password, text1)
    # ls.click(submit)
    # print(time.thread_time())
    # text = 'web-flash'
    # tes = ('xpath','//*[@class="title-container"]/h3')
    # aa = ls.assert_text(tes)
    tt= ls.find_title()
    if ls.find_title() == '欢迎光临 | web-flash后台管理':
        print('断言成功')
    else:
        print('断言失败')
    # print(aa)