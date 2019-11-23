# i = 0
# while (i < 9):
#     print("i ----> ",i)
#     i = i + 1
# print(i,"i即将大于或者等于9,while不在执行")

#执行1-100的数字

# a1 = 1
# while a1 <= 100:
#     print(a1,end=" ")
#     a1 = a1 + 1

#执行100 -1 的数字
# a1 = 100
# while a1 >= 0:
#     print(a1,end=" ")
#     a1 = a1 - 1

#执行0+1+2+3+4+.....+100 的sum
# count = 0
# sum = 1
# while sum <= 100:
#     count = count + sum #0+1+2+3
#     sum += 1
# print(count)


#while 循环遍历列表内的值
# List = [1,2,3,4,5,6,7]
# items = len(List)
# count = 0 #表示索引的值
# while count < items:
#     print("列表内的值------>：",List[count]) #每次打印索引值
#     print("列表的索引的值------>",count)
#     count += 1


#猜数字游戏
#1.猜无限次

# res = 999
# while True:
#     guess_number = int(input("请输入要猜入的数字:"))
#     if res == guess_number:
#         print("猜对了,666")
#         break #跳出循环，中止
#     else:
#         if guess_number > res:
#             print("猜大了")
#         else:
#             print("猜小了")

#2.只能猜三次，自动停止程序
# res = 999
# times = 3
# while times > 0:
#     guess_number = int(input("请输入要猜入的数字:"))
#     if res == guess_number:
#         print("猜对了,666")
#         # break #跳出循环，中止
#         continue #跳出当前循环
#     else:
#         if guess_number > res:
#             print("猜大了")
#         else:
#             print("猜小了")
#     times -= 1  # time = time -1

#3.猜三次，每次提示剩余的次数
# res = 999
# times = 3
# while times > 0:
#     guess_number = int(input("请输入要猜入的数字:"))
#     if res == guess_number:
#         print("猜对了,666")
#         if times != 0:
#             print("您还剩" + str(times - 1) + "次机会")
#         else:
#             pass
#     else:
#         if guess_number > res:
#             print("猜大了")
#             if times != 0:
#                 print("您还剩" + str(times - 1) + "次机会")
#             else:
#                 pass
#         else:
#             print("猜小了")
#             if times != 0:
#                 print("您还剩" + str(times - 1) + "次机会")
#             else:
#                 pass
#     times -= 1  # time = time -1


#while 实现1-100以内的奇数,把结果存储在一个list中
# List = []
# i = 1
# while i < 100:
#     if i % 2 != 0:
#         List.append(i)
#     i += 1
# print("新的列表:",List)

#while 语句，用户连续输入10个数字，求10个数字的平均值
List = []
times = 0
while times < 10:
    num = int(input("请输入数字:"))
    List.append(num)
    print("您输入第" + str(times + 1)+"次数字")
    times += 1
    num1 = 0
    for i in range(len(List)):
        num1 += List[i]
print(num1/len(List))

#while计算偶数的和
n = 1
sum = 0
while n <= 100:
    if n %2 == 0:
        n += 1
        continue
    sum = sum + n
    n += 1
print(sum)

#while 的break的实例
while True:
    name = input("请输入：")
    if name == "stop":
        break
    else:
        print(name)