# for i in range(1,10):
#     for j in range(1,i+1):
#         # s = i * j
#         # print("%s*%s=%s"%(i,j,s),end=" ")
#         print("%d*%d=%-3d"%(j,i,i*j),end="")
#     print(" ")

#for语句嵌套
# for i in range(1,10):
#     print("-----------------",i)
#     for j in range(1,10):
#         print("+++++++++++++++++++++",j)


for i in range(1,10):
    print("-----------------",i)
    for j in range(1,i+1):
        print("+++++++++++++++++++++",j)
