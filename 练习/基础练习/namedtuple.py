from collections import namedtuple

#定义一个namedtuple类型User，里面包含name，age，sex属性
User = namedtuple('User',['name','age','sex'])

#创建一个User对象 user
user = User(name='Teacher',age=18,sex='M')

#获取所有字段
#_fields:包含这个类所有字段名的元组方法
print(user._fields)
print(user)

#获取用户的属性值
print(user.name)
print(user.age)
print(user.sex)

#将user对象转换为字典，注意要用'_asdict'
print(user._asdict())