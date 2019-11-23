
#方法一：for嵌套
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            # str1 = str(i) + str(j) + str(k)
            str1 = i*100 + j*10 + k
            agk = pow(i,3)+pow(j,3)+pow(k,3)
            if int(str1) == agk:
                print(print("水仙花数:{}".format(str1)))


#方法二：将数字转化为字符串，在通过索引去百位十位个位数字
# for i in range(100,1000):
#     a = int(str(i)[0])
#     b = int(str(i)[1])
#     c = int(str(i)[2])
#     if i == a*a*a + b*b*b + c*c*c:
#         print("水仙花数:{}".format(i))

#方法三：用数字运算获取百位十位个位数字
# for i in range(100,1000):
#     bai = i//100
#     shi = i%100//10
#     ge = i%10
#     if i == bai**3+shi**3+ge**3:
#         print("水仙花数:{}".format(i))



