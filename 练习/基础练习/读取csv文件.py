import csv

"""
与excel文件不同，csv文件中：
1.数据都没有数据类型，值都是‘字符串’
2.没有颜色和样式，不能指定单元格测的宽高，不能合并单元格
3.没有对个工作表
4.不能嵌入图像图表
"""

# data = []
# csvFile = open('readcsv.csv','r')
# reader = csv.reader(csvFile)
# for item in reader:
#     # print(item)
#     data.append(item)
# print(data)
#
# #关闭csv文件
# csvFile.close()

#
#读取本地csv文件
# with open('readcsv.csv','r') as csvfile:
#     reader1 = csv.reader(csvfile)
#     for line in reader1:
#         print(line)

#从列表中写入csv文件 -->从data中读取列表(一)
# csvFile2 = open('csvFile2.csv','w',newline='',encoding='utf-8')
# writer = csv.writer(csvFile2)
# m = len(data)
# for i in range(m):
#     writer.writerow(data[i])
# csvFile2.close()

#从列表中写入csv文件 -->从data中读取列表(二)
data1 = [['a1',123],['a2',234],['a3',345],['a4',456]]
csvFile2 = open('csvFile2.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csvFile2)
m = len(data1)
for i in range(m):
    writer.writerow(data1[i])
csvFile2.close()

#从字典中写入
data2 = {'b1':123,'b2':234,'b3':345,'b4':456}
csvFile2 = open('csvFile2.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csvFile2)
for key in data2:
    writer.writerow([key,data2[key]])
csvFile2.close()


