# -*- coding: utf-8 -*-

# ----------------------------------------
# 集合（set）：一个无序的不重复元素序列
# ----------------------------------------
# 创建一个空集合，必须使用set()，不能使用{}
set1 = set()

# 集合会自动去掉重复数据
cities = {'北京', '上海', '广州', '深圳', '海南', '广州'}
print(cities)

# 可以先创建一个列表，然后使用set函数将列表转化为集合
list2 = [100, 200, 300, 400, 300]
set2 = set(list2)
print(set2)

# 通过一个字符串来创建字符集合
set3 = set("Hello")
print(set3)

# 使用in和not in判断某个元素是否存在于集合中
print("200 in set2:", 200 in set2)
print("00 not in set2:", 200 not in set2)

a = {100, 200, 300}
b = {300, 400}
# a-b：差集(返回一个新的集合，包含a中有但b中没有的元素)
print("a-b:", a - b)
print(a.difference(b))

# a|b：并集（返回一个新的集合，包含a和b中的每一个元素）
print("a|b:", a | b)
print(a.union(b))

# a&b: 交集（返回一个新的集合，包含a和b中的公共元素）
print("a&b:", a & b)
print(a.intersection(b))

# a^b: 对称差集（返回一个新的集合，包含没有同时出现在a和b中的元素）
print("a^b:", a ^ b)
print(a.symmetric_difference(b))

# add() 往集合中添加一个元素
a.add(400)
print("add:", a)
# update() 更新集合中的元素。可以往集合中添加单个元素、列表、元组等
a.update([500, 600])
print("update:", a)

# a<=b：判断a是否是b的子集（检查a中的每一个元素是否都在b中）
print("a是b的子集：", a <= b)
# a>=b: 判断a是否是b的父集（检查b中的每一个元素是否都在a中）
print("a是b的父集：", a >= b)

# remove(x) 将元素x从集合中移除，如果元素不存在会报错
a.remove(600)
print("remove result:", a)

# discard(x) 也是将元素x从集合中移除，当元素不存在时不会报错
a.discard(500)
print("discard:", a)

# pop() 随机删除集合中的一个元素
a.pop()
print("pop:", a)

# len() 计算集合中元素的个数
print("集合中的元素个数：", len(a))

# clear() 清空集合
a.clear()




