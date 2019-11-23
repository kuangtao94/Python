from selenium import webdriver
import time as t
import unittest

#用例执行顺序
#ASCII 数字 大写 小写 字符

class BaiduTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.baidu.com")
        print("每个测试用例开始前执行")

    @classmethod
    def tearDownClass(cls) -> None:
        print("每个测试用例结束后执行")
        cls.driver.quite()

    # def setUp(self):
    #     print("每个测试用例开始前执行")
    #
    # def tearDown(self):
    #     print("每个测试用例结束后执行")

    # @unittest.skip #跳过
    def test_01(self):
        """验证是否显示预期结果"""
        self.driver.find_element_by_id("kw").send_keys('selenium')
        self.driver.find_element_by_id("su").click()
        t.sleep(1)
        self.assertTrue("selenium" in self.driver.page_source)
    @unittest.skipIf(3>2,"条件为真，用例不执行，条件为假，用例执行")
    def test_02(self):
        """验证是否显示预期结果"""
        self.driver.find_element_by_id("kw").send_keys('python')
        self.driver.find_element_by_id("su").click()
        self.driver.quit()

    @unittest.skipUnless(3>2,"条件为真，用例执行，条件为假，用例不执行")
    def test_03(self):
        """验证是否显示预期结果"""
        self.driver.find_element_by_id("kw").send_keys('appium')
        self.driver.find_element_by_id("su").click()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
