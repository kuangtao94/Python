
# 线性脚本
# from selenium import webdriver
#
# #初始化webdriver
# driver = webdriver.Chrome()
#
# def getUrl(url):
#     """获取地址"""
#     return driver.get(url)
#
# def inputcontent(loctor,content):
#     """搜索框输入内容"""
#     return driver.find_element_by_id(loctor).send_keys(content)
#
# def click_bt(loc):
#     """点击百度一下按钮"""
#     return driver.find_element_by_id(loc).click()
#
# def close_browser():
#     """关闭浏览器"""
#     return driver.quit()
#
# def serach_content(url,loctor,content,loc):
#     """百度搜索封装"""
#     getUrl(url)
#     inputcontent(loctor,content)
#     click_bt(loc)
#     close_browser()
#
# if __name__ == '__main__':
#     # serach_content("http://www.baidu.com","kw","selenium","su")
#     getUrl("http://www.baidu.com")
#     inputcontent("kw","selenium")
#     click_bt("su")
#     close_browser()


# from selenium import webdriver
#
# #初始化webdriver
# driver = webdriver.Chrome()
#
# def getUrl(url):
#     """获取地址"""
#     return driver.get(url)
#
# def inputcontent(loctor,content):
#     """搜索框输入内容"""
#     return by_id(loctor).send_keys(content)
#
# def click_bt(loc):
#     """点击百度一下按钮"""
#     return driver.find_element_by_id(loc).click()
#
# def by_id(local):
#     """对selenium id定位二次封装"""
#     return driver.find_element_by_id(local)
#
# def by_css(local):
#     """对selenium css定位二次封装"""
#     return driver.find_element_by_css_selector(local)
#
# def by_xpath(local):
#     """对selenium xpath定位二次封装"""
#     return driver.find_element_by_xpath(local)
#
# def close_browser():
#     """关闭浏览器"""
#     return driver.quit()
#
# def serach_content(url,loctor,content,loc):
#     """百度搜索封装"""
#     getUrl(url)
#     inputcontent(loctor,content)
#     click_bt(loc)
#     close_browser()
#
# if __name__ == '__main__':
#     # serach_content("http://www.baidu.com","kw","selenium","su")
#     getUrl("http://www.baidu.com")
#     inputcontent("kw","selenium")
#     click_bt("su")
#     close_browser()


#面向对象封装设计
# from selenium import webdriver
#
# class TestBaidu:
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#
#     def getUrl(self,url):
#         """获取地址"""
#         return self.driver.get(url)
#
#     def by_id(self,loc):
#         """id 改写"""
#         return self.driver.find_element_by_id(loc)
#
#     def input_content(self,loc,text):
#         """搜索框输入内容"""
#         return self.by_id(loc).send_keys(text)
#
#     def click_bt(self,loc):
#         """点击百度一下按钮"""
#         return self.by_id(loc).click()
#
#     def close_browser(self):
#         """关闭浏览器"""
#         return self.driver.quit()
#
#     def all_serach_content(self,url,loc1,text,loc2):
#         """百度搜索封装"""
#         self.getUrl(url)
#         self.input_content(loc1,text)
#         self.click_bt(loc2)
#         self.close_browser()
#
# if __name__ == '__main__':
#     baidu = TestBaidu()
#     baidu.all_serach_content("http://www.baidu.com","kw","selenium","su")
