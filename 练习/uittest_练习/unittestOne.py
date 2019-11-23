from selenium import webdriver
import time as t
import unittest,os

class BaiduTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("每个测试用例开始前执行")

    @classmethod
    def tearDownClass(cls) -> None:
        print("每个测试用例结束后执行")

    # def setUp(self):
    #     print("每个测试用例开始前执行")
    #
    # def tearDown(self):
    #     print("每个测试用例结束后执行")

    def test_01(self):
        """验证是否显示预期结果"""
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys('selenium')
        self.driver.find_element_by_id("su").click()
        self.driver.quit()

    def test_02(self):
        """验证是否显示预期结果"""
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys('python')
        self.driver.find_element_by_id("su").click()
        self.driver.quit()

    def test_03(self):
        """验证是否显示预期结果"""
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys('appium')
        self.driver.find_element_by_id("su").click()
        self.driver.quit()


# if __name__ == '__main__':
    #执行所有以test开头的用例
    # unittest.main() #方法一
    # testsuite测试套件  添加测试执行
    # suite = unittest.TestSuite  #方法二
    # suite.addTest(BaiduTest("test_01")) #添加用例
    # suite.addTest(BaiduTest("test_02")) #添加用例
    # suite.addTest(BaiduTest("test_02")) #添加用例
    #......add 100
    # runner = unittest.TextTestRunner() #执行测试方法
    # runner.run(suite)

    #方法三
    # path = os.path.dirname(__file__)
    # testlist = unittest.defaultTestLoader.discover(
    #     path = path,
    #     pattern = "unittestOne*.py",
    #     top_level_dir=None
    # )
    # runner = unittest.TextTestRunner()
    # runner.run(testlist)


def createsuite():
    suite = unittest.TestSuite()
    path = os.path.dirname(__file__)
    testlist = unittest.defaultTestLoader.discover(
        path = path,
        pattern = "unittestOne*.py",
        top_level_dir=None
    )
    for testsuite in testlist:
        for testcase in testsuite:
            suite.addTest(testcase)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(createsuite())
