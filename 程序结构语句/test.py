gess = -1
source = 100
num = 8
print("一起来玩猜猜猜游戏")
while gess != num:
    gess = int(input("请输入一个数字(输入0退出):"))
    if gess == 0:
        break  #退出循环体

    if gess < 0:
        continue  #退出当前循环，再次进入循环体

    if  gess > num :
        print("数字猜大了")
        source -= 10

    if gess == num:
        print("恭喜猜中了")
        source += 100

    if gess < num:
        print("数字猜小了")
        source -= 10
    print("当前积分为:",source)
#当while语句False时，执行else语句，如在循环体中执行break语句是不会执行else语句
else:
    print("顺利过关")
print("游戏结束")


cities = ['北京', '天津', '上海', '广州', '深圳', '珠海']
n = 0
for city in cities:
    print(n,city)
    n += 1
    # 遍历循环结束，退出循环体
print("遍历城市列表结束")