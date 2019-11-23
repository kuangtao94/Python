from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t

#广金所
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#被测站点
url = "https://www.gjfax.com/"
driver.get(url)
driver.maximize_window()
t.sleep(1)

Wait = WebDriverWait(driver,10,0.5)

#元素定位方法封装
def find_element(*loc):
    return Wait.until(lambda x:x.find_element(*loc))
    # return driver.find_element(*loc)

#页面元素操作方法
#定位器定位元素的方式

loginBut_loc = (By.CSS_SELECTOR,"span.footer-right >a") #首页页面元素登录按钮
username_loc = (By.CSS_SELECTOR,"#mobilePhone") #输入账号
password_loc = (By.ID,"password") #输入密码
loginButton_loc = (By.CSS_SELECTOR,"#loginBtn") #登录页面点击登录按钮
loginInfo_loc = (By.CSS_SELECTOR,'#realName') #登录后验证信息
logout_loc = (By.CSS_SELECTOR,"a.fc-blue.mr-5") #点击安全退出按钮

#点击登录按钮,跳转到登录页面
def click_but_login(*loginBut_loc):
    find_element(*loginBut_loc).click()
#输入账号
def input_username(username,*username_loc): #可变长不能放形参前面
    find_element(*username_loc).send_keys(username)
#输入密码
def input_password(password,*password_loc):
    find_element(*password_loc).send_keys(password)
#登录页面点击登录按钮
def login_button(*loginButton_loc):
    find_element(*loginButton_loc).click()
#登录后验证信息
def Assert_Info(*loginInfo_loc):
    return find_element(*loginInfo_loc).text
#点击安全退出按钮
def logout_button(*logout_loc):
    find_element(*logout_loc)

if __name__ == '__main__':
    click_but_login(*loginBut_loc)  #点击登录按钮,跳转到登录页面
    input_username("18513600235",*username_loc) #输入账号
    input_password("a123456",*password_loc)  #输入密码
    login_button(*loginButton_loc)  #登录页面点击登录按钮
    if Assert_Info(*loginInfo_loc) == "185****0235":  #登录后验证信息
        print("pass")
    else:
        print("Fail")
    logout_button(*logout_loc)  #点击安全退出按钮
    t.sleep(2)
    driver.quit()





