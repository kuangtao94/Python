# -*- coding: utf-8 -*-


import math                     # 导入一个模块
import os, sys                  # 导入多个模块

import datetime
from datetime import date       # 导入模块中某个具体的类
from math import pi             # 导入模块中某个变量

# import ch08_2

import xml
# import xml.sax                  # 需要使用全名去访问
# from xml import sax
# from xml import *
# from xml.sax.handler import version

a = 1024
print("a的平方根为：", math.sqrt(a))  # 求平方根
print(pi)

print("当前工作平台：", os.name)       # 'nt': Windows  'posix': Linux/Unix
print("当前系统平台：", sys.platform)

print("今天的日期：", datetime.date.today())
print("今天的日期：", date.today())

ver = xml.sax.handler.version
print("版本号：", ver)



