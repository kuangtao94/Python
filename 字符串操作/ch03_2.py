# -*- coding: utf-8 -*-



# ----------------------------------------
# 字符串的截取：[]、[:]
# ----------------------------------------
string = "字符串的截取操作!"

# str[i] 表示截取第几个字符，字符索引值从0开始
print("string[1]:", string[1])

# str[x:y] x表示开始截取的索引值，y表示停止截取的索引值（包含x，但不包含y）
print('string[2:5]:', string[2:5])

# 如果省略开始索引值，就从第一个字符到结尾索引值
print('string[:5]:', string[:5])

# 如果省略结尾索引值，就从开始索引值到最后一个字符
print('string[2:]:', string[2:])

# 更新字符串
# string[3] = "被"
string = string[:3] + "被" + string[4:]
print(string)

# 使用in和not in判断某个字符或字符串是否存在于另一个字符串中
sub_string = "截取"
if sub_string in string:
    print("in")
else:
    print("not in")

sub_string = "是"
if sub_string not in string:
    print("not in")
else:
    print("in")

# ----------------------------------------
# 字符串的常用函数
# ----------------------------------------
# count() 用于统计字符串里某个字符出现的次数
string = "Hello python!"
sub_str = 'o'
print("字符o出现的次数为：", string.count(sub_str))
# len()返回字符串的长度
print("字符o出现的次数为：", string.count(sub_str, 5, len(string)))

# find() 检测字符串中是否包含子字符串。如果包含，返回开始的索引值；否则返回-1。
sub_str1 = "py"
sub_str2 = "pn"
print("查找子串py，返回索引值：", string.find(sub_str1))
print("查找子串pn，返回索引值：", string.find(sub_str2, 2))
print("查找子串py，返回索引值：", string.find(sub_str1, 3, 8))

# index()与find()函数的用法相同，只是当字符串中没有包含指定的子串时，会报一个异常，而不是返回-1。

# replace() 把字符串中的旧字符串替换为新字符串
print(string.replace("python", "word"))     # 默认是进行全部替换
print(string.replace("o", "w", 1))          # 也可以指定替换的最大次数

# swapcase() 对字符串中的大小写字母进行相互转换
print("swapcase:", string.swapcase())

# lower() 转换字符串中所有大写字符为小写
print("lower:", string.lower())

# upper() 转换字符串中所有小写字母为大写
print("upper:", string.upper())

# strip() 删除字符串左右两侧的空格或指定的字符
string2 = "------ch02_基础语法--------"
print("strip:", string2.strip('-'))

string1 = "Python3"
# isalnum() 如果字符串至少有一个字符，并且所有字符都是字母或数字则返回True，否则返回False。
print("isalnum:", string1.isalnum())
# isalpha() 如果字符串至少有一个字符，并且所有字符都是字母则返回True，否则返回False。
print("isalpha:", string1.isalpha())
# isdigit() 如果字符串只包含数字则返回True，否则返回False。
print("isdigit:", string1.isdigit())

# title() 返回一个标题化的字符串（即所有单词以大写开头，其余字母均为小写）
print(string.title())

# center() 返回一个指定宽度并且居中显示的字符串，并在左右两侧填充指定的字符，默认为空格
print("center:", string.center(40, '-'))
