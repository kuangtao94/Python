# -*- coding: utf-8 -*-


# -----------------------------------------
# 生成器(generator)：使用了yield的函数
# -----------------------------------------
# 偶数生成器
def even():
    print('2')
    yield 2
    print('4')
    yield 4
    print('6')
    yield 6
    print('8')
    yield 8

    return 'OK'


# 生成一个生成器对象
e = even()
# 用while语句+next()方法遍历生成器
while True:
    try:
        # 使用next生成并取出一个元素
        print('while:', next(e))
    except StopIteration as e:
        print('迭代结束！')
        # 生成器的返回值包含在StopIteration实例的value中
        print(e.value)
        break

# 用for...in语句遍历生成器
for e in even():
    print('for:', e)
print()


# 自定义一个生成器
def my_yield(n):
    num = 0
    while n > 0:
        num += 1
        yield n * 2
        n -= 1
    return '生成了%d个值' % num


# 用for...in语句遍历生成器
for i in my_yield(5):
    print("for遍历值：", i)
print()

# 用while语句+next()方法遍历生成器
yy = my_yield(5)
while True:
    try:
        print("while遍历值：", next(yy))
    except StopIteration as e:
        print(e.value)
        break




