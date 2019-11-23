# -*- coding: utf-8 -*-

# ----------------------------------------------------
# 选择结构：通过判断某些特定条件是否满足来决定程序的执行顺序。
# ----------------------------------------------------
# 布尔表达式中常用的操作运算符：<、<=、>、>=、==、!=、in和not in
# 单分支选择结构
a = 100
b = 200
if a < b:
    a, b = b, a
    print("将a和b进行了交换，a中保存较大的值")
print("a, b:", a, b)


# bool() 将其他值转换为布尔类型
print(bool(1))
print(bool("非空的元素，转换后都为True。"))
print(bool([10, 20]))
#以下执行的结果为False
print(bool(0))
print(bool(""))
print(bool([]))

# 双分支选择结构
student_info1 = ['张晓晓', '女', 12, '七年级']
student_info2 = ['刘烨', '男', 14, '九年级']
name = '刘烨'
if name == '张晓晓':
    print(student_info1)
else:
    print(student_info2)

# 三元运算符：value1 if condition else value2
student_info = student_info1 if name == '张晓晓' else student_info2
print(student_info)

# 多分支选择结构
score = 88
level = ''
if score >= 95:
    level = 'A+'
elif score >= 85:
    level = 'A'
elif score >= 75:
    level = 'A-'
elif score >= 60:
    level = 'B'
else:
    level = 'C'
print("Level:", level)

# pass语句-表示程序结构的完整性，占位符
n = 2
if n == 1:
    print('Hello python!')
elif n == 2:
    pass
elif n == 3:
    print('Hello world!')


# 嵌套分支结构
score = 88
level = ''
if score >= 60:
    print("通过考核！")
    if score >= 80:
        level = '优等生'
    else:
        level = '中等生'
else:
    print("未通过考核！")
    if score >= 45:
        level = '不及格'
    else:
        level = '低等生'
print("Level:", level)





