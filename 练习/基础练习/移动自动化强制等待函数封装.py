from appium import webdriver
import time
import os

#创建启动参数函数封装
def Case(platformName,platformVersion,deviceName,app,appPackage,appActivity):
    #apk的路径
    PATH = lambda p : os.path.abspath(os.path.join(os.path.dirname(__file__),p))
    desired_caps = {}
    desired_caps["platformName"] = platformName #设置平台
    desired_caps["platformVersion"] = platformVersion #系统版本
    desired_caps["deviceName"] = deviceName #设备的id
    desired_caps["autoLaunch"] = "true" #是否自动启动
    desired_caps["noReset"] = "true" #应用是否重置
    desired_caps["noCommandTimeout"] = 20
    desired_caps["app"] = PATH(app) #安装包的路径，放在该py目录下
    desired_caps["appPackage"] = appPackage #启动应用的包名
    desired_caps["appActivity"] = appActivity #启动应用的Activity

    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
    waitFor(20)
    return driver

#创建等待函数
def waitFor(t):
    time.sleep(t)

#隐形等待函数
def implicit_for_wait(t):
    driver = Case()
    driver.implicitly_wait(t)

#显示等待函数
def WebDriverWait(t):
    driver = Case()
    #lambda函数：冒号前面是参数,冒号后面的是返回值
    WebDriverWait(driver,t,5).until(lambda driver : driver.find_element_by_id("kw"))

def getSize():
    driver = Case()
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    return (x,y)

#向左滑动
def LeftSwipe():
    driver = Case()
    x1 = int(getSize()[0]*0.9)
    y1 = int(getSize()[1]*0.5)
    x2 = int(getSize()[0]*0.1)
    #500是毫秒
    driver.swipe(x1,y1,x2,y1,500)

#向右滑动
def RightSwipe():
    driver = Case()
    x1 = int(getSize()[0] * 0.25)
    y1 = int(getSize()[1] * 0.5)
    x2 = int(getSize()[0] * 0.75)
    # 500是毫秒
    driver.swipe(x1, y1, x2, y1, 500)

#向上滑动
def UpSwipe():
    driver = Case()
    x1 = int(getSize()[0] * 0.5)
    y1 = int(getSize()[1] * 0.8)
    y2 = int(getSize()[1] * 0.4)
    # 500是毫秒
    driver.swipe(x1, y1, x1, y2, 500)

#向下滑动
def DownSwipe():
    driver = Case()
    x1 = int(getSize()[0] * 0.5)
    y1 = int(getSize()[1] * 0.25)
    y2 = int(getSize()[1] * 0.75)
    # 500是毫秒
    driver.swipe(x1, y1, x1, y2, 500)

#获取时间戳
def getTime():
    tamp = int(time.time())
    return tamp

#截图
def getScreenShot():
    driver = Case()
    time = getTime()
    filename = "../jpg/%s.png"%time
    driver.get_screenshot_as_file(filename)

#混个app；webview & native
def view():
    driver = Case()
    #获取当前页面所有的contexts
    webview = driver.contexts
    #在获取到的contexts中list依次循环的打印
    for context in webview:
        #判断单个循环context中是否是webview,如果有就切换，并且跳出循环
        if "WEBVIEW" in context:
            driver.switch_to.context(context)
            break
    driver.find_element_by_id("kw").click()
    #点击关闭按钮（可能会出错,需要跳出webview）或者自己封装个函数
    driver.find_element_by_id("eqds").click()

#loggin日志
"""
1.初始化 logger = logging.getLogger("endlesscode"),
getLogger()方法后面最好加上所要日志记录的模块的名字,
后面的日志格式中的%(name)s对应的是这里的模块的名字.
2.设置日志级别logger.setLevel(logger.DEBUG),
logging中有NOTSET<DEBUG<INFO<WARNING<ERROR<CRITICAL这几种级别,日志会记录设置级别以上的日志
3.handler,常用的是StreamHandler和FileHandler,Windows下你可以理解成为一个console和日志文件,
一个打印在CMD窗口上,一个记录在文件上.
4.formatter,定义了最终的log信息的顺序,结构,内容,一般为这样的格式
"[%(asctime)s] [%(levelname)s] [%(message)s] ","%Y-%h-%m %H:%M:%S"
%(name)s Logger的名字
%(levelname)s 文本形式的日志级别
%(message)s 用户输出的信息
%(asctime)s 字符串形式的当前时间.默认格式是"2019-9-2 23:00:52,413"逗号后面是毫秒
%(levelno)s 数字形式的日志级别
"""

