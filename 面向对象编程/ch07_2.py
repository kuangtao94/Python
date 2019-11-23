# -*- coding: utf-8 -*-

# ---------------------------
# 属性和方法
# ---------------------------
# 定义类
class ProjectGroup:
    """这是一个项目组的类"""
    group_number = 0          # 类的属性（类变量）

    # 类的构造方法，创建实例时会被调用
    def __init__(self, project_name=None, members=None, dev_time=None):
        self.project_name = project_name        # 对象的属性（实例变量）
        self.members = members                  # 公有属性，在类的外部可以通过对象进行访问 -- 项目成员
        self.__dev_time = dev_time              # 私有属性，在类的外部不能直接访问 -- 项目周期
        ProjectGroup.group_number += 1

    # 析构方法，删除类对象（使用del语句删除类实例）时自动执行
    def __del__(self):
        ProjectGroup.group_number -= 1
        print("Destroy!")

    def __str__(self):                # 内置函数，用来设置对象以字符串类型出现时如何显示
        return self.project_name

    def print_members(self):
        print(self.members)

    def get_dev_time(self):
        return self.__dev_time                  # 通过公有成员方法访问私有成员变量

    def set_dev_time(self, dev_time):
        self.__dev_time = dev_time

    def __mod_budget(self, budget):             # 私有方法，只能在类内访问
        self.budget = budget
        print("设置项目预算：", self.budget)

    def set_budget(self, budget):
        self.__mod_budget(budget)               # 调用私有方法

    @classmethod                    # 修饰器，声明类方法
    def class_get_number(cls):      # 类方法，不能访问实例变量
        print("class method:", cls.group_number)     # cls表示该类自身，在外部调用时不需要传值

    @staticmethod                   # 修饰器，声明静态方法
    def static_get_number():        # 静态方法
        print("static method:", ProjectGroup.group_number)    # 同样不能访问实例变量
        # print("static method方法:", ProjectGroup.project_name) #打印出错,不能访问实例变量(类方法成员的变量)


# 实例化生成一个对象
project_group1 = ProjectGroup("RFID项目组")
# 在类的外部，访问对象的公有属性
project_group1.members = ['周小军', '张文静', '陈涛', '孙翔']
# 访问类的属性(通过类名或对象名访问)
print("当前项目组的数量：", ProjectGroup.group_number)
print("使用对象访问时的数量：",project_group1.group_number)

print("当前项目组的名称：",project_group1)

# 通过公有成员方法设置私有成员变量的值
project_group1.set_dev_time(90)
print("项目的开发周期为：{}天".format(project_group1._ProjectGroup__dev_time))

# 通过公有方法调用私有方法，设置项目预算为20万
project_group1.set_budget(200000)

# 通过类名/对象调用类方法
ProjectGroup.class_get_number()
# 通过对象/类名调用静态方法
project_group1.static_get_number()

# 再实例化一个对象
project_group2 = ProjectGroup("数据交换项目组", ['刘晓', '卢茜', '耿超'], 120)
print("group_number2数量:", ProjectGroup.group_number)

# 删除对象，自动执行析构方法
project_group3 = ProjectGroup()
print("group_number:", ProjectGroup.group_number)
project_group4 = ProjectGroup() #每创建一个实例化的对象,group_number都会加1
print("group_number数量:", ProjectGroup.group_number)
del project_group3
print("group_number:", ProjectGroup.group_number)

# 类的内置属性
# 返回该类的文档字符串
print("ProjectGroup.__doc__:", ProjectGroup.__doc__)

# 返回创建此对象所用的类名称
print(project_group1.__class__)
print(project_group2.__class__)

# 以字典的形式返回对象的属性和属性值(不包括类的属性)
print(project_group1.__dict__)
print(project_group2.__dict__)

# 返回包含此类的模块名称
print(ProjectGroup.__module__)

# 返回该类的所有父类名称（只返回上一级父类）也叫基类
print(ProjectGroup.__bases__)

# 返回当前模块的名字
print("当前模块的名字：", __name__)
