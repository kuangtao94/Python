#文件名 txt文件的读取

#文件的读取 open("文件","读写方法")  with open("文件","读写方法") as 句柄:
#创建文件或者写入内容到文件中
# file = open("userinfo.txt","w",encoding="utf-8")
# file.write("人生苦短,\n没事得多挣钱,\n及时行乐.")
#怎么判断文件是否被关闭呢？file.closed 返回True则关闭，反则False
# print("检查文件是否被正常的关闭:",file.closed)
#文件的关闭
# file.close()
# print("检查文件是否被正常的关闭:",file.closed)

# r+ 表示可读可写，文件存在就覆盖
# file = open("userinfo.txt","r+",encoding="utf-8")
# file.write("中国你好")
# 文件的关闭
# file.close()


#读取文件内容
#read(字节) 读取所有内容 或者某个字节
# file = open("userinfo.txt","r",encoding="utf-8")
# print(file.read())
# print(file.read(1))
#readline 读取首行内容
# print(file.readline())
#radelines 读取所有内容,且所有内容存储在列表中,包含换行符\n
# print(file.readlines())

#去掉\n
#列表转换成字符串 "".join(list) --> str.strip() 过滤掉特殊字符
# n1 = file.readlines() #列表
# # n2 = "".join(n1)
# # print(n2.strip())
# # print(type(n2.strip()))

#文件的追加 a & a+
# file = open("userinfo.txt","a",encoding="utf-8")
# file.write("Hello,World")
#文件的关闭
# file.close()


# r 读取文件，文件不存在读取就报错 ，r+ 可读写文件，覆盖原有文件内容
# file = open("testinfo","r",encoding="utf-8")
# print(file.readlines())
#FileNotFoundError: [Errno 2] No such file or directory: 'testinfo'

# w  写文件内容，清除文件原有内容； w+ 读写文件内容，清除文件原有内容
# file = open("userinfo.txt","w+",encoding="utf-8")
# file.write("人生苦短,\n没事得多挣钱,\n及时行乐.Hello")
#文件的关闭
# file.close()


#通过上下文进行管理 with open as

# with open("userinfo.txt","w",encoding="utf-8") as f:
#     f.write("上下文进行写入内容")

# with open("userinfo.txt","r",encoding="utf-8") as f:
    # print(f.readlines())
# print("检查文件是否被正常的关闭:",f.closed)


#写入班级的考试成绩,记录到score.txt中
"""
小明,55
小花,56
小华,77
小王,84
小刘,65
小习,
"""
import re
#计算score.txt文件中的所有人考试成绩的平均分
#写入内容至score.txt 文件中
# with open("score.txt","w",encoding="utf-8") as file:
#     file.write("小明,55\n小花,56\n小华,77\n小王,84\n小刘,65\n小习,")
#读取内容,计算平均值
with open("score.txt","r",encoding="utf-8") as file:
    List = file.readlines()
str1 = "".join(List)
str2 = str1.strip()
# print(str2,type(str2))
List1 = re.findall(",(.+)",str2) #使用正则表达式提取数字,返回的是列表
# print(List1,type(List1))
num = 0
for index in range(len(List1)):
    # print(index)
    num += int(List1[index])
print(num/len(List1))
