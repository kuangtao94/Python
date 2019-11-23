#列表推导式 ---> 返回的是列表  for语句 效率更高
# 1*1 2*2 3*3 4*4 5*5 6*6 7*7 8*8 9*9
# import time
# to = time.clock() #时间戳
# Li = []
#
# for i in range(1,10):
#     Li.append(i)
#     # print(str(i) + "*" + str(i),end=" ")
# print("for循环消耗的时间是:{a}".format(a = time.clock() -to)) # 8.55257868800022e-06
# print("\n")

#列表推导式
# List = [str(index) + "*" + str(index) for index in range(1,10)]
# print(List)
# print("列表推导式消耗的时间是:{a}".format(a = time.clock() -to)) # 6.613994185386836e-05

#for 求1-100以内的偶数
# List = []
# for i in range(1,101):
#     if i % 2 == 0:
#         List.append(i)
# print("1-100以内的偶数:",List)

#列表推导式
# List = [i for i in range(1,101) if i % 2 == 0]
# print("1-100以内的偶数:",List)

#for + 字典
# List = []
# d = {"course":"Python","price":"66"}
# for index,value in d.items():
#     # print(index,"-->",value)
#     List.append(index + "-->" + value)
# print(List)


#列表生成式 全排列
# List = [m + "--->" + n for m in ["Python","Selenium","Jenkins","Appium"] for n in ["11","33","55","77"]]
# print(List)

#把所有的字母转换成大写  --for循环
# newList = []
# List = ["python","java","selenium"]
# for index in List:
#     newList.append(index.upper()) #srt.upper() 用于字符串小写转成大写
# print(newList)

#列表推导式
# List = ["python","java","selenium"]
# res = [index.upper() for index in List ]
# print(res)


# os模块  目录相关内置库

import  os
# print(os.listdir())
# res = [dirname for dirname in os.listdir("..")]
# print(res)

# res = [dirname for dirname in os.listdir(".") if dirname.endswith("*函数.py")]
# print(res)


#列表推导式:取出名字长度大于3的人员
# nameList = ["body","jim","jerry","tom","python"]
# newList = [index for index in nameList if len(index)>3]
# print(newList)

#列表推导式: M = [[1,2,3],[4,5,6],[7,8,9]],求3,6,9组成的列表
#方法一:
# M = [[1,2,3],[4,5,6],[7,8,9]]
# List = []
# for index in M:
#     List.append(index[2])
# print(List)

#方法二:
# M = [[1,2,3],[4,5,6],[7,8,9]]
# List = [index[2] for index in M ]
# print(List)

#列表推导式: M = [[1,2,3],[4,5,6],[7,8,9]],求1,5,9组成的列表
# M = [[1,2,3],[4,5,6],[7,8,9]]
# List = [M[index][index] for index in range(len(M))]
# print(List)

#列表推导式:求(x, y)，其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
# List = [(x,y) for x in range(6) if x%2==0 for y in range(6) if y%2!=0]
# print(List)

#列表推导式:生成间隔5分钟的时间列表序列
List = ["%02d:%02d"%(h,m) for h in range(25) for m in range(1,61,5)]
print(List)
