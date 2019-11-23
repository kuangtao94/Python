from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
url = "http://www.baidu.com"
driver.get(url)
driver.maximize_window()

dr = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(dr).perform() #执行操作
driver.find_element_by_link_text("搜索设置").click()
sleep(1)
driver.find_element_by_link_text("保存设置").click()

#切花到警告框
# switch_to.alert
# text 获取警告框的文本信息
# accept() 点击确认按钮
# dismiss() 点击取消按钮
# sendkeys("字符串") 输入文本信息

#获取警告框的文本信息
text1 = driver.switch_to_alert().text #已经记录下您的使用偏好
print(text1)

sleep(0.5)
# 点确认按钮
driver.switch_to_alert().accept() #点击确认按钮

sleep(1)
driver.quit()
