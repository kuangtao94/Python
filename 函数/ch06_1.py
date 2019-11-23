# -*- coding: utf-8 -*-

# -----------------------------------------
# 函数：一组定义好的，可以重复使用的代码。
# -----------------------------------------
# 定义一个简单的函数，没有参数，也没有返回值
def hello():
    print("Hello python!")


# 传入一个参数
def welcome(name):
    print("Welcome, %s !" % name)


# 传入参数列表，并返回一个值
# width, height称为形参
def area(width, height):
    return width * height


w = 20
h = 30
# w, h称为实参
rect_area = area(w, h)
print("rect_area:", rect_area)


# 可以返回多个值
def return_xy(arg1, arg2):
    return arg1, arg2


a, b = return_xy(20, 30)
print(a, b)


# 返回None
def print_str(str_to_print):
    print(str_to_print)
    return


# 通过判断语句决定要返回哪个值
def get_level(score):
    if score >= 80:
        return 'A'
    elif score >= 60:
        return 'B'
    else:
        return 'C'


print("等级为：", get_level(75))


# 录入成绩，并且打印出相应的等级(函数的嵌套)
def input_score():
    my_score = int(input("请输入成绩："))
    level = get_level(my_score)
    print("分数：{} 等级：{}".format(my_score, level))


# 不可变对象（数字、字符串、元组）
a = 5
print(id(a))
a = 10   #更新变量值，抛弃之前的变量
print(id(a))

# 可变对象（列表、字典、集合）
b = [1, 2, 3]
print(id(b))  #打印出的id都是一样的
b[1] = 10
print(id(b))


def add_one(x):
    x += 1
    print("函数内的值：", x)


# 给函数传递一个不可变对象
y = 5
add_one(y)
print("函数外的值：", y)


def reorder(score_list):
    score_list.sort()
    print("函数内的值：", score_list)


# 给函数传递一个可变对象
scores = [98, 90, 76, 89, 85]
reorder(scores)
print("函数外的值：", scores)


# 定义了一个必需参数和两个默认参数
def print_info(name, age=12, school='明德'):
    print("姓名：{}  年龄：{}  学校：{}".format(name, age, school))


print_info('李佳欣')
print_info('李佳欣', 15)
print_info('李佳欣', 15, '执信')
print_info('李佳欣', school='二中')
print_info(age=13, name='张宇')


# 定义不定长参数
# 加了一个星号的参数（以元组的形式导入）
def print_list(group, *members):
    print("小组：{}\n成员：{}".format(group, members))


print_list('成长组', '张磊', '李静', '陈晓', '肖亮')


# 加了两个星号的参数（以字典的形式导入）
def print_dict(name, **infos):
    print("姓名：{}\n信息：{}".format(name, infos))


print_dict('张雨婷', sex='女', age=12, grade='初一')


# 匿名函数
# lambda [arg1 [,arg2,.....argn]]:expression
sumfun = lambda arg1, arg2: arg1 + arg2


print("两数之和为：", sumfun(100, 200))


def reorder1():
    # 在函数内部使用全局变量
    scores1.sort()
    print("函数内的值：", scores1)


# 全局变量
scores1 = [98, 90, 76, 89, 85]
reorder1(scores1)
print("函数外的值：", scores1)


# 如果要在函数内改变全局变量的值，必须使用global关键字
def double():
    global g
    g = g * 2
    print("函数内的值：", g)


g = 5
double()
print("函数外的值：", g)

