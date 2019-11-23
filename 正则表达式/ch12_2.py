# -*- coding: utf-8 -*-

import re

# --------------------------------
# 常用字符表达式的校验
# --------------------------------
# 汉字的编码范围为：\u4e00-\u9fa5
# 匹配1~3个汉字
str1 = re.findall('[\u4e00-\u9fa5]{1,3}', "My name is 淇文！")
print("str1:", str1)

intro = "我的英文名叫Maggie，我的学号是8_001。"
# 匹配一个或多个英文和数字
str2 = re.findall('[A-Za-z0-9]+', intro)
print("str2:", str2)

# 匹配大写字母和数字
str3 = re.findall('[A-Z0-9]+', intro)
print("str3:", str3)

# 匹配字母、数字、下划线、汉字等
str4 = re.findall('[\w]+', intro)
print("str4:", str4)

# match：从字符串的起始位置开始匹配一个表达式。
# 如果匹配成功，返回一个match对象，否则返回None
match_obj = re.match("[Aa]+", "Aaaabcaaa")
if match_obj:
    print("str5:", match_obj.group())
    # print("str5:", match_obj.group(0))
else:
    print("str5:无匹配")

str6 = re.findall("[Aa]+", "bAaaabcaaa")
print("str6:", str6)

# 提取出HTML中的标题
html = r"<html><body><h1>Hello python!<h1></body></html>"
p1 = r"<h1>.+<h1>"              # 定义正则表达式
pattern1 = re.compile(p1)       # 编译正则表达式
print(pattern1.findall(html))
# print(re.compile(p1).findall(html))

key = r"abbc and abc and abbbc"
p2 = r"ab{1,2}c"
pattern2 = re.compile(p2)
print(pattern2.findall(key))

