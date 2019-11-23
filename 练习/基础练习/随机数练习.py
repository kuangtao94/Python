from random import Random

#实例化随机数对象
rad = Random()

base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for i in range(1000):
    email = ''
    for j in range(5):
        i = rad.randint(0,len(base)-1)
        email = email + base[i] #字符串拼接
    print('粤B·%s'%email)
