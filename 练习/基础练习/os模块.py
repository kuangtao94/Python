# os模块  目录相关内置库
import os
# . 当前目录 .. 返回上一级目录
# 1. os.path.abspath() --获取当前文件的绝对路径(不包含os模块.py) pwd
# path = os.path.abspath(".")
# print(path)  #D:\Test\Python基础入门\练习

# 2. os.path.realpath(__file__) --获取当前文件的完整路径
# print(os.path.realpath(__file__))  #D:\Test\Python基础入门\练习\os模块.py

# 3. os.path.dirname() --获取当前文件的绝对路径 pwd
# print(os.path.dirname(os.path.realpath(__file__))) #D:\Test\Python基础入门\练习

# 4. os.path.dirname(os.path.dirname(os.path.realpath(__file__))) --获取绝对路径的上一级路径
# print(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))) #D:\Test\Python基础入门

# 5. os.path.join(a,b) 把两个目录路径进行拼接
# print(os.path.join(os.path.dirname(os.path.realpath(__file__)),"os模块.py"))
# pwdpath = os.path.dirname(os.path.realpath(__file__))
# pjpath = os.path.join(pwdpath,"os模块.py")
# print("拼接后的完整路径:",pjpath)
# print("拼接后的完整路径:",os.path.realpath(__file__))
# 拼接后的完整路径: D:\Test\Python基础入门\练习\os模块.py
# 拼接后的完整路径: D:\Test\Python基础入门\练习\os模块.py

# 6. os.path.splitext() 把文件和文件的后缀名分隔出来
# filepath = os.path.realpath(__file__)
# print("获取文件的完整路径:",filepath)
# fileParh = os.path.splitext(filepath)
# print("获取分隔后的文件:",fileParh) #返回的是元组格式
# print("获取分隔后文件的后缀名:",fileParh[-1])
# 获取文件的完整路径: D:\Test\Python基础入门\练习\os模块.py
# 获取分隔后的文件: ('D:\\Test\\Python基础入门\\练习\\os模块', '.py')
# 获取分隔后文件的后缀名: .py

# 7. os.path.normpath() --将不规范的路径变成规范的路径
# str1 = "E:\Program Files (x86)\360\360Safe\Config\///advtools\WenJianFenSuiJi.xml"
# print("规范的路径:",os.path.normpath(str1))

# 8.其他方法
"""
os.chdir(path="path") 切换路径
os.getcwd() 获取当前目录--绝对路径
os.mkdir() 创建目录
os.listdir() 列出当前目录下的所有文件和目录
"""

# 9. 文件和目录的判断
"""
os.path.isdir("目录路径") -->存在返回True，反则False
os.path.isfile("文件的路径") -->存在返回True，反则False
"""

# os模块实战
# 打印出C:\Program Files\Internet Explorer目录下的所有.dll文件
os.chdir("C:\Program Files\Internet Explorer")
# print("当前目录:",os.getcwd())
# print("当前目录下的所有文件和目录:",os.listdir())
List = os.listdir()
for index in List:
    if ".dll" in index:
        print("以.dll结尾的文件:",index)
