# -*- coding: utf-8 -*-


import re


# --------------------------------
# 用正则表达式切分字符串
# --------------------------------
# 自动识别一个或多个空格进行切分
# \s匹配任意空白字符串
str1 = 'ab c  d'
p1 = r'\s+'
print("split1:", re.split(p1, str1))

# 在分割符中加入逗号和分号
str2 = 'a bc,d;; efg, ;h'
p2 = r'[\s\,\;]+'
print("split2:", re.split(p2, str2))

# --------------------------------
# 分组
# --------------------------------
# groups()返回一个包含所有小组字符串的元组（从1到n组，不包含第0组）
# group(0)匹配整个表达式的字符串，其余为每个组匹配的字符串
# \d匹配任意数字，等价于[0-9]
phone = '020-34500886'
p3 = r'^(\d{3,4})-(\d{6,8})$'
match_obj = re.match(p3, phone)
if match_obj:
    print("groups:", match_obj.groups())
    print("group(0):", match_obj.group(0))
    print("group(1):", match_obj.group(1))
    print("group(2):", match_obj.group(2))


str4 = "Frank and James are good friends."
p4 = r'(.*) and (.*?) .*'
match_obj4 = re.match(p4, str4)
if match_obj4:
    print("groups:", match_obj4.groups())
    print("group(0):", match_obj4.group(0))
    print("group(1):", match_obj4.group(1))
    print("group(2):", match_obj4.group(2))
else:
    print("无匹配！")

# --------------------------------
# 检索
# --------------------------------
# search()扫描整个字符串并返回第一个成功的匹配对象
str5 = "在Python中，使用re模块处理正则表达式。请熟练掌握该模块的应用。"
p5 = "模块"
match_obj5 = re.search(p5, str5)
if match_obj5:
    print("start:", match_obj5.start())
    print("end:", match_obj5.end())
    print("span:", match_obj5.span())
    print("group0:", match_obj5.group(0))
else:
    print("无匹配！")

# compile：将正则表达式编译为正则表达式对象
str6 = "将正则表达式编译成正则表达式对象可以提高执行效率。"
pattern = re.compile('正则表达式')
match = pattern.search(str6)
if match:
    print(match.group())
    print("span:", match.span())

# finditer：以迭代器的方式返回所有匹配的对象
str7 = "将正则表达式编译成正则表达式对象可以提高执行效率。"
p7 = "正则表达式(对象)?"
match7 = re.finditer(p7, str7)
for i in match7:
    print(i.group())
    print(i.span())

# --------------------------------
# 替换
# --------------------------------
card = "招商银行卡号：3442 3521 8970 5664"
# 删除卡号前面的文字
# \w匹配字母、数字、下划线、汉字等
p8 = r'^\w+\：'
card_no = re.sub(p8, "", card)
print("卡号:{}".format(card_no))

# 删除所有非数字内容
# \D匹配任意非数字
p9 = r'\D+'
card_no = re.sub(p9, "", card)
print("卡号:{}".format(card_no))
