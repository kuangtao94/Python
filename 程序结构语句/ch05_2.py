# -*- coding: utf-8 -*-

# ----------------------------------------------------
# 循环结构：根据代码的逻辑条件来判断是否重复执行某一段程序。
# ----------------------------------------------------
# while循环
# 数字猜猜猜
num = 8
guess = -1
score = 100
print("一起来玩数字猜猜猜！")
while guess != num:
    guess = int(input("请输入一个数字："))

    if guess == 0:
        break  #退出循环体

    if guess < 0:
        continue  #退出当前循环，再次进入循环体
    if guess == num:
        print("恭喜恭喜！猜中了！")
        score += 100
    elif guess < num:
        print("笨笨，猜的数字小了！")
        score -= 10
    elif guess > num:
        print("笨笨，猜的数字大了！")
        score -= 10

    print("你当前的积分是：", score)
#当while语句False时，执行else语句，如在循环体中执行break语句是不会执行else语句
else:
    print("顺利过关")
print("游戏结束！")


# for循环
# range() 生成一个数列
for x in range(10):     # 等价于range(0, 10, 1)
    print(x)

# 也可以指定一个区间
for y in range(5, 10):
    print(y)

# 还可以指定不同的增量
for z in range(20, 100, 10):
    print(z)

# 遍历一个序列的索引
cities = ['北京', '天津', '上海', '广州', '深圳', '珠海']
n = 0
for city in cities:
    print(n, city)
    n += 1
    # 遍历循环结束，退出循环体
print("遍历城市列表结束")

for n in range(len(cities)):
    print(n, cities[n])
print("遍历城市列表结束")

n = 0
while n < len(cities):
    print(n, cities[n])
    n += 1
print("遍历城市列表结束")
