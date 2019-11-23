# -*- coding: utf-8 -*-


import calendar


# -----------------------------------------
# calendar日历模块
# -----------------------------------------
# 返回2018年10月日历
cal = calendar.month(2019, 10)
print("输出2019年10月份的日历：")
print(cal)

# 返回2019年的年历
cal1 = calendar.calendar(2019)
print(cal1)

# 判断年份是否为闰年
year = 2020
if calendar.isleap(year):
    print("%d年是闰年" % year)
else:
    print("%d年不是闰年" % year)

# 设置每周的起始日期码。0（星期一）到6（星期日）
calendar.setfirstweekday(6)
# 返回当前每周起始日期的设置。默认为0星期一
print("每周起始日期码为：", calendar.firstweekday())

# 返回给定日期的日期码，0（星期一）到6（星期日）
print(calendar.weekday(2019, 7, 21))
