# -*- coding: utf-8 -*-



# --------------------------------
# 读取文件
# --------------------------------
# open() 打开文件，并返回一个文件对象
f = open('ch13_test.txt', 'r+')
# f = open(r'D:\PycharmProjects\Python零基础快速入门\ch13_文件处理\ch13_test.txt')
print("文件名为：", f.name)

# read() 从文件读取指定的字符数，若未给定或为负，则读取所有
# 从文件头开始读取5个字符
print(f.read(5))

# 继续读取8个字符
print(f.read(8))

# readline() 从文件中读取整行
print(f.readline())     # 从当前位置到行尾（包括换行符）
print(f.readline(25))   # 读取指定数量的字符（如果当前行剩余字符数不够，遇换行符结束）
print(f.readline())

# 负数，读取整个文件的内容(从当前光标位置到文件末尾)
print(f.read(-1))

# 获取当前文件位置
post = f.tell()
print("当前文件位置为：", post)

# seek(offset[, whence]) 移动文件读取指针到指定位置
# 重新设置文件读取指针到开头
f.seek(0, 0)        # whence 0:文件头；1：当前位置；2：文件尾

post = f.tell()
print("当前文件位置为：", post)

# readlines() 读取所有行并返回列表
i = 1
for line in f.readlines():
    print("{}.{}".format(i, line), end="")
    i += 1

# close() 关闭一个已打开的文件
f.close()






