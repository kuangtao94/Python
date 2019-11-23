"""
jquery操作处理
jquery语法
jq_id = '$("id").vla(值)'  --输入文本内容
jq_id = '$("id").click()'  --点击
jq 处理id 、type、tag层级定位
"""

from selenium import webdriver
import time as t

driver = webdriver.Chrome()
#简书站点
driver.get('https://www.jianshu.com/sign_in')

#根据id定位 #代表id
jq_id = '$("#session_email_or_mobile_number").val("username")'
driver.execute_script(jq_id)
t.sleep(2)

#根据type定位 type属性定位:属性值 输入密码
jq_type = '$(":password").val("123")'
driver.execute_script(jq_type)
t.sleep(1)

#按层次定位 勾选记住我
#1.带有标签 type定位
jq_remember = '$(".remember-btn > input:checkbox").val("123456")'
driver.execute_script(jq_remember)
t.sleep(2)
#2.不带标签
# jq_remember = '$(".remember-btn > :checkbox").click())'
# driver.execute_script(jq_remember)
# t.sleep(2)
#3.不带层次符号
# jq_remember = '$(".remember-btn :checkbox").click())'
# driver.execute_script(jq_remember)
# t.sleep(2)
#4.选择最后一个标签(input)的元素
# jq_remember = '$(".remember-btn > input:last").click())'
# driver.execute_script(jq_remember)
# t.sleep(2)

#class 定位 定位登录按钮
jq_remember = '$(".sign-in-button").click()'
driver.execute_script(jq_remember)
t.sleep(2)

driver.quit()