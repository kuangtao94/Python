# -*- coding: utf-8 -*-

from collections import Iterable  #可迭代对象
from collections import Iterator  #迭代器


# -----------------------------------------
# 迭代器（Iterator）
# -----------------------------------------
# 用for循环遍历集合元素
cities = ['北京', '上海', '广州', '深圳']
for city in cities:
    print(city)
print()

t = (100, 200, 300)
s = {'a', 'b', 'c'}
d = {'a': 100, 'b': 200, 'c': 300}
c = '南京'

# 判断是否为可迭代对象
print(isinstance(cities, Iterable))
print(isinstance(t, Iterable))
print(isinstance(s, Iterable))
print(isinstance(d, Iterable))
print(isinstance(c, Iterable))
print()

# 判断是否为迭代器(是可迭代对象非迭代器)
print(isinstance(cities, Iterator))
print(isinstance(t, Iterator))
print(isinstance(s, Iterator))
print(isinstance(d, Iterator))
print(isinstance(c, Iterator))

# 使用迭代器访问列表
cities = ['北京', '上海', '广州', '深圳']
i = iter(cities)        # 创建迭代器对象（才可进行遍历）
# 使用常规的for语句进行遍历
for city in i:
    print(city)
print()

cities = ['北京', '上海', '广州', '深圳']
i = iter(cities)
# 使用next()函数进行遍历，等价于for...in循环
while True:
    try:
        print(next(i))
    except StopIteration:
        print("停止迭代")
        break



