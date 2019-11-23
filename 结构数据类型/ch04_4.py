# -*- coding: utf-8 -*-

# ----------------------------------------------------------
# 字典（dict）：一种可变容器模型，可以存储任意类型的对象。由键-值对组成
# ----------------------------------------------------------
# 键必须是唯一且不可改变的
dic = {1: '一季度', '2': '二季度'}
# 不能通过索引访问，只能通过键进行访问
print(dic['2'])

dic = {1: '一季度', '2': '二季度', '2': '三季度'}
print(dic)

dic['2'] = '二季度'    # 修改元素的值
dic['3'] = '三季度'    # 增加新的键值对
print(dic)

del dic['3']          # 删除字典中的元素
print(dic)

# len() 计算字典元素的个数，即键值的总数
print("字典长度为：", len(dic))

# str() 将字典的元素转化为可打印的字符串形式
print(str(dic))

# copy() 复制字典(浅拷贝)
dic1 = dic.copy()
print("dic1:", dic1)

# clear() 清除字典中的所有元素
dic.clear()
print("dic:", dic)

dic3 = {'一季度': 10000, '二季度': 12000, '三季度': 18000}
# get(key[, value]) 返回指定键的值。如果指定的键不存在，返回value
print("一季度的销量为：", dic3.get('一季度'))
print("四季度的销量为：",  dic3.get('四季度'))
print("四季度的销量为：",  dic3.get('四季度', '未统计'))

# setdefault(k[, v]) 如果k存在，就返回其值；否则返回v，并将新的元素添加到字典中
print(dic3.setdefault('一季度'))
print(dic3.setdefault('四季度', 17000))

# 使用in和not in检测键（key)是否存在于字典中
print("一季度存在于字典中：", '一季度' in dic3)
print("四季度不存在于字典中:", '四季度' not in dic3)

# items() 使用字典中的元素创建一个由元组对象组成的列表(一个元组对应一个键-值对)
print(dic3.items())

# keys() 使用字典中的键创建一个列表
print(dic3.keys())

# values() 使用字典中的值创建一个列表
print(dic3.values())

# dic1.update(dic2) 将字典dic2的键/值对更新到dic1中
dic4 = {'一月份': 3500, '二月份': 3800}
dic3.update(dic4)
print(dic3)

# pop() 删除字典中指定key对应的值，并且返回被删除的值
print(dic3.pop('一月份'))

# popitem() 删除字典中的最后一元素，并返回这个元素的键值
print(dic3.popitem())







