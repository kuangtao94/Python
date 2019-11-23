# 推荐学习：https://www.w3school.com.cn/js/index.asp
#
# 下面以简书登录&注册定位元素为例
"""
js定位 id name class_name xpath css元素器

除了id是定位到的是单个的element元素对象，其他的都是elements返回的是list对象
1.通过id获取
js_id = 'document.getElementById("id的值");'
2.通过CLASS获取
js_class = 'document.getElementsByClassName("class的值")[0];'
3.通过Name获取
js_name = 'document.getElementsByName("name的值")[0];'
4.通过标签名选取元素
js_tag = 'document.getElementsByTagName("tag的值")[0];'
5.通过CSS选择器选取元素
js_css = 'document.querySelectorAll("CSS Selector语法")[0];'
"""

from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.get('https://www.jianshu.com/sign_in')

#js id 定位注册
js_id = 'document.getElementById("js-sign-up-btn").click();'
driver.execute_script(js_id)
t.sleep(2)

#返回首页
driver.get('https://www.jianshu.com/sign_in')

#js CLASS 定位登录
js_class = 'document.getElementsByClassName("active")[0].click();'
driver.execute_script(js_class)
t.sleep(2)

#js Name 输入用户名
js_name = 'document.getElementsByName("session[email_or_mobile_number]")[0].value="username";'
driver.execute_script(js_name)
t.sleep(2)

#js tag 输入密码
js_tag = 'document.getElementsByTagName("input")[3].value="123456";'
driver.execute_script(js_tag)
t.sleep(2)

#js Css 点击登录
js_css = 'document.querySelectorAll(".sign-in-button")[0].click();'
driver.execute_script(js_css)
t.sleep(2)

driver.quit()