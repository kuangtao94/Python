# -*- coding: utf-8 -*-

# ----------------------------------------
# 列表（list）：一组有序的元素
# ----------------------------------------
# 定义一个空的列表
s = []
# 定义一个全是数字的成绩列表
score = [90, 92, 88, 79, 95, 82]

# 可以通过索引值来访问列表中的元素，从左到右，起始值为0，最后一个元素为n-1
first_one = score[0]
# 也可以从右到左通过一个负数索引值进行访问，倒数第一个元素为-1，最后一个元素为-n
last_one = score[-1]

# 修改元素的值
score[-1] = 80
print(score)

# 列表中的元素可以是不同的数据类型
student_info = ['1001', '张晓晓', '女', 12, [86, 88, 92]]
# 使用切片打印学生基本信息
print("学生基本信息：", student_info[1:4])

# + 将运算符两侧的列表组合在一起
grade = ['七年级']
student_info = grade + student_info
print(student_info)

# 同理也可以用+=
student_info += ['广东省', '广州市']
print(student_info)

# append() 在列表尾部追加新的元素（一次只能追加一个元素）
student_info.append('番禺区')
print(student_info)

# extend() 在列表尾部追加另一个列表(追加的不是列表，而是列表中的元素)
address = ['南村镇', '东环街']
student_info.extend(address)
print(student_info)

# insert(x, y) 向列表中的x位置插入数据y
student_info.insert(-1, "同乐路") #由于东环街是-1，对应同乐路，则不是添加到末尾
student_info.insert(len(student_info), "同乐路") #把同乐路加入到末尾
print(student_info)

# * 将列表中的元素重复n次，并且拼接成一个列表
scores = [90, 100] * 5
print(scores)

# 使用in和not in判断某个元素是否存在于列表中
print("100 in scores:", 100 in scores)
print("100 not in scores:", 100 not in scores)

# len() 返回列表的长度
score = [90, 92, 88, 79, 95, 90, 82]
print("score列表中有%d个元素" % len(score))

# max() 返回列表元素中的最大值(元素的数据类型必须一致，否则会出错)
print("最高分是：", max(score))
# min() 返回列表元素中的最小值
print("最低分为：", min(score))
# sum() 返回列表中所有元素的和
print("总分：", sum(score))

# count(x) 统计列表中相同元素值x出现的次数
print("90分有%d个" % score.count(90))

# sort() 将列表中的元素进行排序,默认为升序（需要是统一的单一数据类型）
score.sort()
print("升序排列：", score)
score.sort(reverse=True)
print("降序排列：", score)

# index(x) 获得指定元素x第一次在列表中的位置（索引值）
index = score.index(90)
print("90分的排名为：", index + 1)

# pop(index) 删除列表中索引值为index的元素，默认删除最后一个元素
score.pop()
print("删除一个最低分：", score)

# reverse() 将列表中的元素颠倒排列
score.reverse()
print("将列表中的元素进行颠倒：", score)

# remove(value) 将列表中元素值为value的项删除，一次只删除一个元素
score.remove(90)
print("删除90分：", score)

# clear() 清空列表
score.clear()
print(score)

score = [90, 92, 88, 79, 95, 90, 82]
# del 删除指定位置的元素，并且可以使用切片的方式进行删除
del score[2]
print(score)
del score[0:3]
print(score)
del score
print(score)
