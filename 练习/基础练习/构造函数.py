"""构造函数"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


if __name__=="__main__":
    zh = Person('张三',"18")
    print(zh.name,zh.age)