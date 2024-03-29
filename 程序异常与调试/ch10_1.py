# -*- coding: utf-8 -*-

# -----------------------------------------
# 编程中的一些常见错误
# -----------------------------------------
# import pandas

# 除数为0
x = 100
y = 10
z = x / y

# 索引值超出范围
score = (100, 200, 300, 400)
print(score[3])

# 修改不可变对象 - 字符串为不可变对象
city = "Guangzhou"
print(city[2])
# city[2] = 'b'
city = city[0:2] + "b" + city[3:]
print(city)


# 将字符串和非字符串进行连接
a = "Python"
b = "3"
print(a + b)

# 代码块缩进错误
level = 2
if level == 2:
    print("基础班")
else:
    print("继续强化！")
    print("培优班")

# 赋值运算符错用为比较运算符
level = 3

# 变量未赋初始值
i = 0
i += 1

# 文件找不到
file = open("ch10_test.txt", "r")

# 在字典中找不到相应的键
dic = {'a': 1, 'b': 2, 'c': 3}
value = dic['c']

# 用户按下Ctrl+C组合键时抛出键盘中断异常
pwd = 888           # 用户密码
num = -1            # 输入密码
times = 0           # 密码输入的错误次数
while num != pwd:
    input_num = input("请输入三位数字的密码：")

    num = int(input_num)
    if num != pwd:
        print("密码错误！")
        times += 1
        if times >= 3:
            print("密码错误超过3次，请明天再试！")
            break
        else:
            continue
    else:
        print("密码正确！")
else:
    print("登录成功！")






