# -*- coding: utf-8 -*-

# ---------------------------
# 重写
# ---------------------------
# 定义父类
class Father:
    def __init__(self, name):
        self.name = name
        print("name: %s" % self.name)

    def get_name(self):
        return "Father's name:" + self.name


# 定义子类，继承父类
class Son(Father):
    # 继承父类构造方法，并进行改写
    def __init__(self, name):
        # 调用父类方法的形式一
        super(Son, self).__init__(name)
        # super().__init__(name)            # Python 3.x 中可以使用

        # 调用父类方法的形式二
        # Father.__init__(self, name)

        # 然后再执行子类自己的一部分操作
        self.name = name
        print("Hello! Subclass's initialize function.")

    # 重写get_name方法
    def get_name(self):
        return "Son's name:" + self.name


# 如果直接运行脚本，执行下面的代码
#如你叫小明.py，你在朋友眼中是叫小明,name,而在你自己眼中是name==mian,即小明.py
if __name__ == '__main__':
    # 实例化子类
    son = Son('Danny')
    # 调用子类对象的方法
    print(son.get_name())

