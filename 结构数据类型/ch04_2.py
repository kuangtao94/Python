# -*- coding: utf-8 -*-


# ----------------------------------------
# 元组（tuple）：一组有序的元素。定义后元素不可修改
# ----------------------------------------
# 创建只有一个元素元组，必须在元素之后加上逗号
# t = ()
# one = (100)
only_one = (100,)

# + 对元组进行拼接，生成一个新的元组
info1 = '1001', '张晓晓'
info2 = ('女', '初一')
print("info1+info2:", info1 + info2)

# * 重复多次
print("info1*3:", info1 * 3)

# 使用in和not in判断某个元素是否存在于元组中
print("张晓晓 in info1:", '张晓晓' in info1)
print("张晓晓 not in info1:", '张晓晓' not in info1)

student_info = ('1001', '张晓晓', '女', '初一', 12, '广州')
# len() 返回元组的长度（元组中元素的个数）
print("元组的长度：", len(student_info))
# 同样可以通过索引和切片的方式访问元组
print(student_info[1:])

tuple1 = (88, 93, 76, 90)
# max() 返回元组中元素的最大值（元组中的数据类型必须一致）
print("最大值为：", max(tuple1))
# min() 返回元组中元素的最小值（数据类型必须一致）
print("最小值为：", min(tuple1))

# 将列表转换为元组
list2 = [100, 200, 300, 200, 400]
tuple2 = tuple(list2)
print("将列表转换为元组：", tuple2)

# sum() 返回元组中所有元素的和
print("总计：", sum(tuple2))

# count() 统计指定元素在元组中出现的次数
print("200出现的次数：", tuple2.count(200))

# index() 返回指定元素第一次在元组中出现的索引值
print("200第一次出现的位置：", tuple2.index(200))

# 将元组转换为列表
list3 = list(student_info)
print("将元组转换为列表：", list3)

# 元组中的元素值不允许删除，只能使用del语句删除整个元组
del student_info
