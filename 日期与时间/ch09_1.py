# -*- coding: utf-8 -*-


import time


# -----------------------------------------
# time时间模块
# -----------------------------------------
# 时间戳
t1 = time.time()         # 获取当前时间戳
print("第一个时间戳为：", t1)

t2 = time.time()
print("第二个时间戳为：", t2)

# 计算两个时间的间隔
print("时间差为：{.3f}".format(t2-t1))

# 时间元组
# localtime()：将以秒为单位的时间戳转化为本地时间（以时间元组的形式）
t3 = time.time()
st = time.localtime(t3)
# st = time.localtime() #不传入参数，打印出的是当前系统时间
print(st)

# 格式化时间
# 最简单的获取可读时间模式的函数是asctime()，字符串的格式为“星期 月份 日 时：分：秒 年”
print(time.asctime(time.localtime(time.time())))
# print(time.asctime()) #打印出格式为：Sun Jul 21 20:04:04 2019

# ctime()可以把一个时间戳转化为asctime()可视化时间的形式
print(time.ctime(t3))   #打印出的格式与asctime()一致

# strftime()可以使用time模块的strftime方法来格式化日期
print(time.strftime("%Y-%m-%d %A", time.localtime()))   # 默认为当前时间
print(time.strftime("%H:%M:%S", time.localtime()))      # 24小时制
print(time.strftime("%I:%M:%S", time.localtime()))      # 12小时制

# strptime()用于根据指定的格式把一个时间字符串转化为时间元组
print(time.strptime('2018-09-12 16:28:58', '%Y-%m-%d %X'))

# clock()函数返回目前的CPU时间。
# 第一次调用时，返回程序运行的实际时间
print(time.clock())
# 将当前进程置入睡眠状态5秒钟
time.sleep(5)
# 第二次调用时，返回自第一次调用到这一次调用的时间间隔
print(time.clock())

# gmtime()将时间戳转换为代表UTC（格林威治时间）的时间元组，默认为当前时间
secs = 1582414145
print(time.gmtime(secs))
print(time.gmtime())

# mktime()将时间元组转换为时间戳
lt = time.localtime()
print(time.mktime(lt))

