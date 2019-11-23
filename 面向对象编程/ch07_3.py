# -*- coding: utf-8 -*-

# -------------------------------------
# 继承：派生类可以继承父类的公有成员
# -------------------------------------
# 单继承
# 基类：员工
class Staff:
    school = '一中'                  # 类变量，在该类及其子类的实例中共享

    def __init__(self, name='', age=25, sex='男'):
        # 成员变量（实例变量）通常都是在此方法中定义
        self.__name = name          # 姓名
        self.__age = age            # 年龄
        self.__sex = sex            # 性别

        self.set_name(name)         # 调用方法对参数的有效性进行验证,并完成初始化
        self.set_age(age)
        self.set_sex(sex)

    def set_name(self, name):
        print("Staff: mod_name!")
        # isinstance()：测试一个对象是否为str
        if not isinstance(name, str):
            print('Name must be string.')
            # 如果数据不合法，就使用默认值
            self.__name = ''
            return

        self.__name = name

    def set_age(self, age):
        if type(age) != int:
            print('Age must be integer.')
            self.__age = 25
            return

        self.__age = age

    def set_sex(self, sex):
        if sex not in ('男', '女'):
            print("性别必须是：'男'或'女'")
            self.__sex = '男'
            return

        self.__sex = sex


# 派生类：老师（继承父类的公有成员，但不能继承其私有成员）
class Teacher(Staff):
    def __init__(self, name='', age=25, sex='男', phone=None, title=None):
        # 调用基类的构造函数
        # super(Teacher, self).__init__(name, age, sex)
        # 调用父类(基类)方法的形式一
        super().__init__(name,age,sex)     # Python 3.x 中可以使用
        # 调用父类(基类)方法的形式二
        # Staff.__init__(self,name,age,sex)
        # 增加子类特有的属性
        self.phone = phone  # 电话号码
        self.title = title  # 职称

    # 公有方法 设置/修改电话号码
    def set_phone(self, phone):
        self.phone = phone
        print("phone:", self.phone)

    def mod_title(self, title):
        self.title = title
        print("New title is:", self.title)


# 实例化员工类
staff = Staff('张楠')
# 通过对象名访问类变量
print("所属学校：", staff.school)
# 通过公有方法，修改私有变量
staff.set_age(28)
# 打印对象的属性及值
print(staff.__dict__)

# 实例化教师类
teacher = Teacher('李茜')
# 通过类名访问类变量
print("所属学校：", Teacher.school)
# 设置电话号码
teacher.set_phone('13711710932')
# 修改职称
teacher.mod_title('优秀教师')
# 设置性别
teacher.set_sex('女')
# 打印对象的属性及值
print(teacher.__dict__)






