from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.so.com/")
sleep(1)

#点击360导航
driver.find_element_by_link_text("360导航").click()

#窗口的切换
#获取所有的窗口 windows_handles
#切换到指定的窗口 switch_to.windows(指定窗口)

#1.获取所有窗口的句柄
dr = driver.window_handles

#通过索引切换到第二个窗口
driver.switch_to_window(dr[1])
sleep(0.5)
driver.find_element_by_id("search-kw").send_keys("第二个窗口")
sleep(2)

#切换至第一个窗口
driver.switch_to_window(dr[0])
driver.find_element_by_id("input").send_keys("第一个窗口")
sleep(2)

#关闭所有窗口
driver.quit()






