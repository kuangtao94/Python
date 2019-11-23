from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = "http://www.baidu.com"
driver.get(url)
driver.maximize_window()

tags = driver.find_elements_by_tag_name("input")

for tag in tags:
    #查询对应的属性值
    if tag.get_attribute("autocomplete") == "off":
        tag.send_keys("selenium")
sleep(1)
driver.find_element_by_id("su").click()

driver.quit()

