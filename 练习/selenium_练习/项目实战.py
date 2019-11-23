from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

#被测系统
# Url = "https://www.gjfax.com/"

class GjsTest(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    #输入被测站点
    def openbrowser(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        t.sleep(1)

    #封装元素定位
    def By_css(self,loc):
        # return self.driver.find_element_by_css_selector(loc)
        return self.driver.find_element(By.CSS_SELECTOR,loc)

    #点击首页登录按钮封装
    def click_bt(self,loc):
        self.By_css(loc).click()
        
    #输入账号
    def input_username(self,loc,text):
        self.By_css(loc).send_keys(text)
        
    #输入密码
    def input_password(self,loc,text):
        self.By_css(loc).send_keys(text)
        
    #点击登录页面按钮封装
    def click_button(self,loc):
        self.By_css(loc).click()
        
    #断言--登录后验证信息
    def Assert(self,loc):
        return self.By_css(loc).text

    
    #退出系统
    def logout_sys(self,loc):
        self.By_css(loc).click()
        t.sleep(2)
        self.driver.quit()

    #登录的流程封装
    def login_Gjs(self,Url,loc1,loc2,username,loc3,password,loc4,loc5,exceptText,loc6):
        self.openbrowser(Url)
        t.sleep(1)
        self.click_bt(loc1)
        t.sleep(1)
        self.input_username(loc2,username)
        t.sleep(1)
        self.input_password(loc3,password)
        t.sleep(1)
        self.click_button(loc4)
        t.sleep(1)
        if self.Assert(loc5) == exceptText:
            print("pass")
        else:
            print("Fail")
        self.logout_sys(loc6)


if __name__ == '__main__':
    gjs = GjsTest()
    Url = "https://www.gjfax.com/"
    loc1 = "span.footer-right >a"
    loc2 = "#mobilePhone"
    username = "18513600235"
    loc3 = "#password"
    password = "a123456"
    loc4 = "#loginBtn"
    loc5 = "#realName" #中间有空格的话,把空格换成.
    exceptText = "185****0235"
    loc6 = "a.fc-blue.mr-5"
    gjs.login_Gjs(Url,loc1,loc2,username,loc3,password,loc4,loc5,exceptText,loc6)



