# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://account.cnblogs.com/signin')
driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys('fhj100861')

driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys('Fhj100861!')
driver.find_element_by_xpath('/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/div/app-sign-in/app-content-container/mat-card/div/form/div/button/span').click()

title1 = driver.title
if  title1 == '博客园 - 开发者的网上家园':
    print('登录成功标题是：%s' %title1)
else:
    print('登陆失败！！！')
    driver.save_screenshot('错误截图.png')
time.sleep(10)
driver.find_element_by_xpath('//*[@id="header_user_right"]/a[5]')
alert1 = driver.switch_to.alert()
print(alert1)
time.sleep(4)
alert1.accept()


