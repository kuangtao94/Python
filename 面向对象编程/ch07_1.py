# -*- coding: utf-8 -*-

# ---------------------------
# 面向对象编程
# ---------------------------
# 定义类
# Python 2.x
# class FirstClass(object):
# Python 3.x
class FirstClass:
    """第一个简单的类"""           # 类的帮助信息，可以通过ClassName.__doc__查看
    name = "FirstClass"         # 类属性（类变量）
    intro = "This is my first class!"

    def first(self):
        return self.intro  #函数里面是类的成员

#查看类的注释信息
print(FirstClass.__doc__)
# 类实例化生成一个对象
first_one = FirstClass()
# 获取对象的识别码
print("对象识别码:", id(first_one))
# 获取对象的类型
print("对象类型：", type(first_one))

# 访问类属性--变量
print("类属性的访问FirstClass.name：", FirstClass.name)
print("类属性的访问first_one.name：", first_one.name)

# 调用成员方法
print("调用方法输出：", first_one.first())

# isinstance()：测试一个对象是否为某个类的实例
print(isinstance(first_one, FirstClass)) #返回的是bool值






