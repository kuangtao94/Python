# -*- coding: utf-8 -*-


import re


# --------------------------------
# 常用数字表达式的校验
# --------------------------------
# 匹配纯数字
# search：查找字符串的单个匹配(只返回第一个匹配的元素)
#re.search()方法并不会立刻返回你可以使用的字符串，取而代之是返回一个匹配对象；
#使用group()才可以获得匹配的字符串，返回的如是子组，在group()中设置序号，提取相应捕获的内容
num_s = re.search('[0-9]+', '123abc1234')
print("num_s:", num_s.group())

# findall：返回所有符合要求的元素列表
num_f = re.findall('[0-9]+', '123abc1234def567')
print("num_f:", num_f)

# {n} 匹配n个指定字符
num1 = re.findall('^[0-9]{5}$', '56789')
print("num1:", num1)

# {n,} 匹配至少n位数字
num2 = re.findall('^[0-9]{1,}$', '3567')
print("num2:", num2)

# {n,m} 匹配n~m位数字
num3 = re.findall('^[0-9]{3,6}$', '456789')
print("num3:", num3)

# 匹配以非零开头，最多带两个小数位的数字
num4 = re.findall('^([1-9][0-9]*)+(.[0-9]{1,2})?$', '3780.65')
print("num4:", num4)

# 匹配非零的正整数
num5 = re.findall('^[1-9][0-9]*$', '32768')
print("num5:", num5)

