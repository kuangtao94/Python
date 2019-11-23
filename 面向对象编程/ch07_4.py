# -*- coding: utf-8 -*-


# ---------------------------------------------
# 继承：子类不能直接访问父类的私有属性或私有方法
# ---------------------------------------------
# 多继承
# 基类1：员工
class Staff:
    school = '一中'                  # 类变量，在该类及其子类的实例中共享

    def __init__(self, age=25, sex='男'):
        print("Staff__init__!")

        self.__age = age            # 成员变量（实例变量）通常都是在此方法中定义
        self.__sex = sex

        self.set_age(age)           # 调用方法对参数的有效性进行验证,并完成初始化
        self.set_sex(sex)

    def modify_info(self):
        print("Staff: modify_info! school:", self.school)

    def set_age(self, age):
        self.__age = age

    def set_sex(self, sex):
        self.__sex = sex


# 基类2：教师
class Teacher:
    def __init__(self, name, subject=''):
        print("Teacher__init__!")

        self.__name = name
        self.subject = subject          # 科目

    def modify_info(self):
        print("Teacher: modify_info! name:", self.__name)

    def set_subject(self, *subject):
        self.subject = subject


# 派生类：高级教师（同时继承员工类和教师类）
class SeniorTeacher(Staff, Teacher):
    def __init__(self, name='', age=25, sex='男', subject='', level=''):
        # 调用基类构造方法初始化基类的私有数据成员
        Staff.__init__(self, age, sex)
        Teacher.__init__(self, name, subject)

        self.level = level              # 考核等级

    def set_level(self, level):
        self.level = level
        print("New level is:", self.level)


# 实例化
s_teacher = SeniorTeacher('张默', age=28, sex='男', subject='物理', level='优秀')

# 设置年齡（继承于第一个基类）
s_teacher.set_age(30)

# 设置科目（继承于第二个基类）
s_teacher.set_subject('化学')

# 调用基类公有方法（两个基类都有此方法）
s_teacher.modify_info()




