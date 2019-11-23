import HTMLTestRunner
import unittest
from TestCase.Request.Blog_case.test import *

suilt = unittest.TestSuite()
#引入测试的类,因为我们的类在test这个文件下,所有就直接文件名.类名
suilt.addTest(unittest.makesuite(test.Test_Blog))

#定义报告的路径
filename = "test.html"
#定义报告的文件权限,"wb",表示有读写权限
fp = open(filename,"wb")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title = "BlogTest",
    description = "测试报告"
)
#执行测试报告
runner.run(suilt)

#关闭文件,否则无法生成文件
fp.close()