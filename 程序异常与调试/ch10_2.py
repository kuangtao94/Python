# -*- coding: utf-8 -*-

# -----------------------------------------
# 异常捕获
# -----------------------------------------
# 在except语句中使用pass语句，忽略发生的异常
list1 = ['100', '200', '三百', '四百', '500']
total = 0
for e in list1:
    try:
        total = total + int(e)
    except:
        pass
print(total)

# 文件不存在
try:
    file = open("config.txt", "r")
except FileNotFoundError:
    print("文件不存在！")


# 用户按下Ctrl+C组合键时抛出键盘中断异常
pwd = 888           # 用户密码
num = -1            # 输入密码
times = 0           # 密码输入的错误次数
while num != pwd:
    try:
        num = int(input("请输入三位数字的密码："))
    except ValueError:
        print("请确认输入的是数字！")
        continue
    except:             # 万能异常捕获
        print("退出")
        break

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


# 使用raise主动抛出异常
def zero_div():
    x = 100
    y = 0
    if y == 0:
        # 一旦抛出异常，且未做相应的异常捕获，程序会就此退出。
        raise ZeroDivisionError("除数不能为0！")
    z = x / y
    print(z)


# zero_div()
try:
    zero_div()
except ZeroDivisionError:
    print("捕获到一个ZeroDivisionError异常！")
else:    #只有try为正常情况，才会执行else语句
    print("test1")
finally:  #不管是正常还是异常都会执行该语句
    print("test2")

# 如果抛出一个SystemExit异常会强制结束Python解释器的运行
raise SystemExit






