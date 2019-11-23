
nums = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k ) and (j != k):
                num = i*100 + j*10 + k
                if num not in nums:
                    nums.append(num)
                # print("三位不重复的数字{},{},{}".format(i,j,k))
print(len(nums))
print("三位不重复的数字:%s个"%len(nums))