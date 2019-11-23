# -*- coding: utf-8 -*-



# ----------------------------------------
# 字符串的拼接：+、join函数、格式化
# ----------------------------------------
# +(加号) 将两个字符串连接起来，成为一个新的字符串
str1 = "Hello"
str2 = "python"
str3 = "!"
str_new = str1 + " " + str2 + str3
print(str_new)

# 也可以使用加法赋值运算符（+=）进行连接
str_new += "^-^"
print(str_new)

# join函数 'sep'.join(seq)
# sep：分隔符；seq：要连接的字符串序列
sep = " "
str4 = sep.join("Hello")
print(str4)

seq = ['10', '20', '30', '40']
str5 = sep.join(seq)
print(str5)

# 字符串格式化：%、str.format()
# 使用字符串操作符%来格式化字符串
major_version = 3
minor_version = 6.400
str6 = "使用%%格式化输出：%s %s %d.%.1f!" % (str1, str2, major_version, minor_version)
print(str6)

num = 1
str7 = "如果只有%d个参数，可以省略括号" % num
print(str7)
# char = 'A'
char = 65             # 输出ASCII码对应的字符   a:97
str8 = "%%c用来格式化字符及其ASCII码：%c" % char
print(str8)

# 可以用数字指定输出数据的长度
# -，左对齐标志，默认为右对齐
# 0，表示数据长度不够时，用0填充。默认用空格填充
str9 = "%5s的总成绩是%3d\n%-5s的总成绩是%03d" % ("李宇", 99, "刘晓", 96)
print(str9)
# +，表示正负号都要输出，默认只输出负号
str10 = "广州的温度为%+d，哈尔滨的温度为%+d" % (18, -18)
print(str10)

# 使用str.format()格式化字符串
# {}及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换
# 1、按默认的顺序输出对应的参数(自动编号)
print("主流的搜索引擎是：{}和{}\n".format('百度', 'Google'))

# 2、在括号中用数字指定format中参数的位置（手动编号）
print("主流的搜索引擎是：{0}和{1}".format('百度', 'Google'))
print("主流的搜索引擎是：{1}和{0}\n我使用{0}多一些".format('百度', 'Google'))

# 3、给参数定义关键字，并且与其它方式组合使用
# 注意：不能将自动编号和手动编号的方式混合起来使用。并且位置参数不能排在关键字参数的后面。
print("搜索引擎有：{0}、{1}和{sou_gou}等等".format('百度', 'Google', sou_gou='搜狗'))
print("搜索引擎有：{}、{sou_gou}和{}等等".format('百度', 'Google', sou_gou='搜狗'))

# print("搜索引擎有：{0}、{1}和{2}等等".format('百度', 'Google', sou_gou='搜狗'))

format_str1 = "保留小数点后两位数：{:.2f}".format(3.1415926, 8.888, pi=3.1415926)
print(format_str1)
format_str2 = "保留整数，不带小数位，并且保留正负号：{:+.0f}".format(3.1415926)
print(format_str2)

# <，左对齐，右边填充空格；>，右对齐，左边填充空格
format_str3 = "默认左对齐：{:20s} Python!".format("Hello")
print(format_str3)
format_str4 = ">右对齐：{:>20s} Python!".format("Hello")
print(format_str4)
format_str5 = "默认填充空格，改为填充-：{:->20s} Python!".format("Hello")
print(format_str5)

format_str6 = "指定数据长度为3，右对齐，不够时左边填充0：{:0>3d}".format(9)
print(format_str6)
format_str7 = "指定数据长度为3，左对齐，不够时右边填充0：{:0<3d}".format(9)
print(format_str7)


