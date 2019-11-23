#函数应用
# 1.语法
"""
def 函数名(参数):
    函数体
"""
# 2. 没有参数的函数
# def readbook():
#     print("拿起一本书")
#     print("看书")
#     print("关闭")
# readbook()

# 3. 有参数的函数
# def readbook(name,start,end):
#     print(name + "拿起了一本书")
#     print("从第" + str(start) + "页看到第" + str(end) + "页")
#     print("{}-->看完了".format(name))
#     print("ending")
# readbook("Tom",1,10)

# 4.默认参数 不能放在正常参数的前面
# start=1 报错:SyntaxError: non-default argument follows default argument
# def readbook(name,start,end=10): #end 形参
#     print(name + "拿起了一本书")
#     print("从第" + str(start) + "页看到第" + str(end) + "页")
#     print("{}-->看完了".format(name))
#     print("ending")
# readbook("Tom",1,50) #实参 end同时存在优先使用实参
# print("\n")
# readbook("Tom",1) #end有形参 end=10

# 5.关键字参数 形参=实参
# def readbook(name,start,end): #end 形参
#     print(name + "拿起了一本书")
#     print("从第" + str(start) + "页看到第" + str(end) + "页")
#     print("{}-->看完了".format(name))
#     print("ending")
#形参=实参
# readbook(name="Tom",start=1,end=50) #实参 end同时存在优先使用实参

# 6. return 关键字
# 接口测试实例
# def Login_order():
#     # 服务器返回的session值
#     return "wqeiqwmdqwmddfqrfgtq"
#
# def Myorder(session):
#     #查询我的订单
#     if session == "wqeiqwmdqwmddfqrfgtq":
#         print("Login success!")
#         print("你可以查询我的订单了")
#         return True  #return后面不跟代码,跟了也不执行
#         # print("wqeiqwmdqwmddfqrfgtq")
#     else:
#         print("Login failed")
#         return False
#
# if __name__ == '__main__':
#     Myorder(Login_order())

# 7. 可变参数
# * 接收的是一个元组/列表，参数是不固定的
# def speak(name,*list):
#     print("输出" + str(name) + "个人信息\n")
#     print(list)
# list = ("name:tang","age:18","address:jx")
# speak("tang",*list)

# ** 接收的是一个字典，参数是不固定的
# def speak(name,**list1):
#     print("输出" + str(name) + "个人信息\n")
#     print(list1)
# list1 = {"name1":"糖","age":"18","address":"深圳"}
# speak("tang",**list1)
# key 不能重名 报错:TypeError: speak() got multiple values for argument 'name'

# 8.lambda 匿名函数(表达式)
# F1 = lambda x,y:print(x+y)
# F1(1,5)
#6

# F2 = lambda name:print("你好:",name)
# F2("Jack")
#你好: Jack

#函数实例
#需求,实现不同版本打招呼的方式

# def Chinese(name):
#     print("您好:" + str(name))
#     print("欢迎您使用中文版的手册")
#
# def English(name):
#     print("Hello:" + str(name))
#     print("Welcome to use english book")
#
# while True:
#     name = input("请输入您的姓名")
#     print("请开始你的选择")
#     language = int(input("请输入您要选择打招呼的方式:\n"
#                      "1.选择中文版\n"
#                      "2.选择英文版\n"
#                      "3.选择日文版\n"
#                      "4.选择4 自动退出"))
#     if language == 1:
#         Chinese(name)
#     elif language == 2:
#         English(name)
#     elif language == 3:
#         (lambda name:print("こんにちは:",name))(name)
#     elif language == 4:
#         break
#     else:
#         print("输入有误")

#或者
# def Chinese(name):
#     print("您好:" + str(name))
#     print("欢迎您使用中文版的手册")
#
# def English(name):
#     print("Hello:" + str(name))
#     print("Welcome to use english book")
#
# while True:
#     name = input("请输入您的姓名")
#     print("请开始你的选择")
#     if name == "stop":
#         break
#     language = int(input("请输入您要选择打招呼的方式:\n"
#                      "1.选择中文版\n"
#                      "2.选择英文版\n"
#                      "3.选择日文版\n"
#                      "4.选择4 自动退出"))
#     if language == 1:
#         action = Chinese
#     elif language == 2:
#         action = English
#     elif language == 3:
#         action = lambda name:print("こんにちは:",name)
#     elif language == 4:
#         break
#     else:
#         print("输入有误")
#     action(name)


"""
需求: 一个用户登录成功后显示用户的账号
1.注册，就是把注册的账号和密码写入到记事本中
2.登录，从记事本中读取出账号和密码
3.登录成功后，打印登录后的账号信息:xxx,欢迎你,登录系统
4.优化.....
5.增加.....
"""

# def resiger(username,password):
#     #注册功能
#     # username = input("请输入注册的用户名:")
#     # password = input("请输入注册的密码:")
#     temp = username + "|" + password
#     with open("login.txt","w") as file:
#         file.write(temp)
#
# def login(username,password):
#     #登录功能
#     # username = input("请输入登录的用户名:")
#     # password = input("请输入登录的密码:")
#     List1 = open("login.txt","r").read().split("|")
#     # print(List1,type(List1))
#     if username == List1[0] and password == List1[1]:
#         # print("Login is ok!")
#         return True
#     else:
#         # print("Login is error")
#         return False
#
# def getinfo(bool):
#     #获取登录后的用户信息
#     fp = open("login.txt", "r")
#     list2 = fp.read().split("|")
#     if bool:
#         print("恭喜您!{}登录成功,请开始你的操作".format(list2[0]))
#     else:
#         print("登录失败")
#
# def exit():
#     #退出系统
#     import sys
#     sys.exit(1)
#
# def getUsername():
#     #用户名账号封装
#     username = input("请输入账号:")
#     return  username
#
# def getPassword():
#     #密码封装
#     password = input("请输入密码:")
#     return password
#
# def Main():
#     #主函数的入口
#     while True:
#         choice = int(input("1.注册 2.登录 3.退出"))
#         if choice == 1:
#             resiger(getUsername(),getPassword())
#         elif choice == 2:
#             #login()
#             s = login(getUsername(),getPassword())
#             if s:
#                 getinfo(True)
#             else:
#                 print("登录失败")
#         elif choice == 3:
#             exit()
#         else:
#             break
#
# if __name__ == '__main__':
#     Main()

# 函数实现 写一个创建xx下面的文件的方法 用os+函数的默认参数是实战

import os
def dirname(filename=None,datafile=None):
    """
    创建某个目录下的文件
    :param filename:目录名字
    :param datafile:文件名字
    :return:
    """
    return os.path.join(os.path.dirname(__file__),filename,datafile)
#D:/Test/Python基础入门/练习\data\token
# print(dirname("data","token"))

with open(dirname(filename="data",datafile="token"),"w") as file:
    #文件的写入
    file.write("hdiadknkxasdhabkjndkudadasfdada")



#作业
"""
1. 写一个计算器工具 +-*/ (选择-->输入参数-->代码自动执行)
2. 写一个文本过滤器，结合IO编写
    1)创建文件
    2)写入内容，对写入的内容进行敏感词判断
    3)调用函数入参
"""
