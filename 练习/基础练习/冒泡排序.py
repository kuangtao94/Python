#方法一

# a = [23,32,12,54,18,1]

# for i in range(len(a)):
#     for j in range(0,len(a)-i-1):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)

#方法二
a = [23,32,12,54,18,1]
num = len(a)
while num > 0:
    for i in range(num-1):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
    num -=1
print(a)

