# -*- coding: utf-8 -*-


# 以上是python文件的头部模板
# 在File->Settings->Editor->File and Code Templates->Python script脚本里添加以下代码进行设置
# -*- coding: utf-8 -*-
"""
@File    : ${NAME}.py
@Time    : ${DATE} ${TIME}
@Author  : xxxx
@Email   : 1512500241@qq.com
@WeChat  : 1512500241
"""

# 与其他常见的编程语言不同，Python不使用｛｝来表示代码段，而是用相同的缩进来区分
# 每一层向右缩进4个空格。缩进表示一个代码块的开始，非缩进表示一个代码块的结束。
sex = "男"
subject = 1                     # 科目：1、语文  2、数学
if sex == "女":
    print("她是一位老师。")
    if subject == 1:
        print("她是一位语文老师。")
    elif subject == 2:
        print("她是一位数学老师。")
else:
    print("他是一位老师。")
    if subject == 1:
        print("他是一位语文老师。")
    elif subject == 2:
        print("他是一位数学老师。")
print()

# 可以使用“空行”分隔出逻辑相关的代码
# 变量名全部小写，由下划线连接各个单词
class_id = 1                    # 班级id
student_sex = "女"
if student_sex == "女":
    if class_id == 1:
        print("她是七（1）班学生")
    else:
        print("她是七（2）班学生")
else:
    if class_id == 1:
        print("他是七（1）班学生")
    else:
        print("他是七（2）班学生")
print()

# 字符串换行符'\n'
print("这个班的学生非常团结。\n在这次学校举协的运动会上获得了总分第一名的成绩！\n同学、老师，以及到校的家长都非常开心，一起拍照留念！\n")

# 代码换行符'\'，又称续行符，用来连接当前行与下一行的代码。
# 注意：'\'后面不可以添加注释。
print("这个班的学生非常团结。\
在这次学校举协的运动会上获得了总分第一名的成绩！\
同学、老师，以及到校的家长都非常开心，一起拍照留念！")

# 小括号()、中括号[]、大括号{}包含起来的语句，不需要使用反斜杠\
month_names = ['January', 'February', 'March',
               'April', 'May', 'June',
               'July', 'August', 'September',
               'October', 'November', 'December']

# 一行多条语句（不推荐，程序可读性差）
a = 3; b = 2; c = a + b; print("c =", c, "\n")

# Python中的注释分为单行注释和多行注释
# 这是一个单行注释，下面定义两个常量
UNIT_PRICE_OF_APPLE = 7.9                   # 苹果的单价 常量名所有字母均大写，由下划线连接各个单词
UNIT_PRICE_OF_ORANGE = 6.8                  # 桔子的单价

'''
这是一个多行注释，可以用三个单引号括起来，也可以用三个双引号括起来
input()是python内置的输入函数。它是从标准输入中读入一行文本，默认的标准输入是键盘。
参数为等待用户输入时的提示信息，是可选项。
用户输入的数据全部都是以字符串的形式返回。
此处，需要输入数值，就必须对输入结果进行类型转换
'''
num = input("请输入苹果的销量：")
amount = UNIT_PRICE_OF_APPLE * float(num)
print("苹果的总销售额为：", amount, "元", end='\n\n')

"""
print()函数用于输出格式化的数据。
values：表示可以有多个输出信息
sep：表示多个输出信息之间的分隔符，默认为一个空格
end：表示所有信息输出之后添加的结束符，默认为一个换行符
"""
num = input("请输入桔子的销量：")
amount = UNIT_PRICE_OF_ORANGE * float(num)
print("桔子的总销售额为：", amount, "元", sep="")
input()


# 使用%占位符的形式，格式化字符串
print("桔子的总销售额为：%f元" % amount)
input()
print("桔子的总销售额为：%.2f元" % amount)
input()
print("桔子的销量为：%s斤，总销售额为：%.2f元" % (num, amount))         # 操作符%是一种比较旧的格式化方法
input()
print("桔子的总销售额为：%.2f元", amount)

input()
# 在python3中最为推荐的字符串格式化方法是str.format()
# {}及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换
# 1、按默认的顺序输出对应的参数
print("主流的搜索引擎是：{}和{}\n".format('百度', 'Google'))
# 2、在括号中用数字指定format中参数的位置
print("主流的搜索引擎是：{0}和{1}".format('百度', 'Google'))
print("主流的搜索引擎是：{1}和{0}\n".format('百度', 'Google'))
# 3、给参数定义关键字，并且与其它方式组合使用
print("搜索引擎有：{0}、{1}和{sou_gou}等等".format('百度', 'Google', sou_gou='搜狗'))
