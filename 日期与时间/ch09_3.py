# -*- coding: utf-8 -*-


import datetime
import time

# -------------------------------------------------------------
# datetime模块定义了5个类：date、time、datetime、timedelta、tzinfo
# -------------------------------------------------------------
# date类
# 返回当前本地时间的date对象
today = datetime.date.today()
print("今天是{}年{}月{}日".format(today.year, today.month, today.day))

# 创建两个日期对象
d1 = datetime.date(2018, 8, 25)
d2 = datetime.date(2018, 9, 18)

# 比较两个日期的大小
d1.__eq__(d2)       # 判断两个日期是否相等
d1.__ge__(d2)       # 判断d1是否大于等于d2
d1.__gt__(d2)       # 判断d1是否大于d2
d1.__le__(d2)       # 判断d1是否小于等于d2
d1.__lt__(d2)       # 判断d1是否小于d2
d1.__ne__(d2)       # 判断d1是否不等于d2

# time类
# 创建一个时间对象
t = datetime.time(10, 28, 32, 680680)
print("{}时{}分{}秒{}微秒".format(t.hour, t.minute, t.second, t.microsecond))

# 同样可以比较两个时间的大小

# max属性表示时间的最大值
print(datetime.time.max)     #打印的是：23:59:59.999999
# min属性表示时间的最小值
print(datetime.time.min)     #打印的是：00:00:00

# __format__()函数将时间对象以指定的格式转化为字符串
print(t.__format__('%H:%M:%S'))

# datetime类可以看作date类和time类的合体，大部分方法和属性都与这两个类类似
# now()返回当前的日期时间的datetime对象
now = datetime.datetime.now()
print(now)

# time()返回datetime对象的时间部分
print(now.time())

# combine()将一个date对象和一个time对象合并生成一个datetime对象
new_datetime = datetime.datetime.combine(today, now.time())
print(new_datetime)

# timedelta类
# 用于计算两个date或datetime对象的差值
# 计算100天前的时间
delta = datetime.timedelta(days=100)
print(delta)
new_time = now - delta
print(new_time)

# 计算100天后的时间
new_time2 = now + delta
print(new_time2)

# 获取上个月的第一天和最后一天的日期
# 获取当前日期对象
today = datetime.date.today()
print(today)
delta = datetime.timedelta(days=1)

# 获取当月第一天的前面一天，即上个月的最后一天
last_day = datetime.date(today.year, today.month, 1) - delta
print(last_day)

# 再创建个上月第一天的日期对象
first_day = datetime.date(last_day.year, last_day.month, 1)
print(first_day)

# 获取时间差，可以用天数、小时、分钟、秒或微秒不同的单位
start_time = datetime.datetime.now()
time.sleep(6)
end_time = datetime.datetime.now()
print((end_time - start_time).seconds)

# 计算当前时间向后32小时的时间
dt1 = datetime.datetime.now()
dt2 = dt1 + datetime.timedelta(hours=32)
print(dt2)
