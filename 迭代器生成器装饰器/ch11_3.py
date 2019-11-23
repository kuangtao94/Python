# -*- coding: utf-8 -*-

from datetime import date


# -------------------------------------------
# 装饰器(Decorator)：给已设计好的函数增加额外的功能
# -------------------------------------------
# func：被装饰的函数名
# inner：装饰完的函数名
def prefix(func):
    # 装饰器函数
    def inner():    #这里是装饰器新定义的函数，原来的功能
        print("今天的日期是：")
        return func()  #返回的是today()函数的内容
    return inner


@prefix #添加新的功能，保持原有的函数名不变，today是在原有装饰器上被装饰的函数
def today():
    print(date.today())


# today = prefix(today)
today() # 由于有装饰器，执行debug后，单个执行会跳转到innner()函数中；与函数today()名相同，调用today函数


# -----------------------------------
# 给多个函数添加相同的装饰器
# -----------------------------------
def add_confirm(func):
    def confirm():
        print("您确认要执行下面的操作吗：")
        return func()
    return confirm


@add_confirm
def f1():
    print('新增记录')


@add_confirm
def f2():
    print('删除记录')


@add_confirm
def f3():
    print('修改记录')


f1()
f2()
f3()

print()


# --------------------------------
# 被装饰函数具有相同的参数个数
# --------------------------------
def add_confirm1(func):
    # 传入相应长度的参数列表
    def confirm(arg):
        print("您确认要执行下面的操作吗：")
        return func(arg)
    return confirm


@add_confirm1
def fun1(arg1):
    print('新增记录:', arg1)


@add_confirm1
def fun2(arg1):
    print('删除记录:', arg1)


@add_confirm1
def fun3(arg1):
    print('修改记录:', arg1)


fun1(1005)
fun2(1003)
fun3(1002)
print()


# --------------------------------
# 被装饰函数具有不同的参数个数
# --------------------------------
def add_confirm2(func):
    # 传入不定长参数
    def confirm(*args, **kwargs):
        print("您确认要执行下面的操作吗：")
        return func(*args, **kwargs)
    return confirm


@add_confirm2
def func1(arg1):
    print('新增记录:{}'.format(arg1))


@add_confirm2
def func2(arg1, arg2):
    print('删除记录:{}、{}'.format(arg1, arg2))


@add_confirm2
def func3(arg1, arg2, arg3):
    print('修改记录:{}、{}、{}'.format(arg1, arg2, arg3))


func1(1009)
func2(1005, 1006)
func3(1001, 1002, 1003)
print()


# --------------------------------
# 给一个函数增加多个装饰器
# --------------------------------
def confirm_operate(func):
    def confirm(*args, **kwargs):
        print("您确认要执行下面的操作吗?")
        return func(*args, **kwargs)

    return confirm


def confirm_data(func):
    def confirm(*args, **kwargs):
        print("您确认数据是正确的吗?")
        return func(*args, **kwargs)

    return confirm


@confirm_operate
@confirm_data
def modify(arg1):
    print("修改数据：", arg1)


modify(1006)



