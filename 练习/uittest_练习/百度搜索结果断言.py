from selenium import webdriver
import unittest
import time as t

Url = "http://www.baidu.com"
class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def getUrl(self,url):
        """获取地址"""
        return self.driver.get(url)

    def by_id(self,loc):
        """id 改写"""
        return self.driver.find_element_by_id(loc)

    def input_content(self,loc,text):
        """搜索框输入内容"""
        return self.by_id(loc).send_keys(text)

    def click_bt(self,loc):
        """点击百度一下按钮"""
        return self.by_id(loc).click()

    def close_browser(self):
        """关闭浏览器"""
        return self.driver.quit()

    def all_serach_content(self,url,loc1,text,loc2):
        """百度搜索封装"""
        self.getUrl(Url)
        self.input_content(loc1,text)
        self.click_bt(loc2)
        t.sleep(2)

    def Assert(self):
        """实际结果 断言"""
        try:
            title = self.driver.title
            print("打印出标题:{}".format(title))
            return title
        except Exception as message:
            print("元素没有找到:{}".format(message))

    def test_all_serach_text(self):
        """搜索-用例1"""
        self.all_serach_content(Url,"kw","selenium","su")
        #验证搜索成功
        self.assertIn("selenium",self.driver.title)


if __name__ == '__main__':
    unittest.main(verbosity=2) #2 详细日志