# -*- coding: utf-8 -*-


# --------------------------------
# 写入文件
# --------------------------------
# 打开一个文件进行读写（文件存在，打开；不存在，新建）
f = open('ch13_test2.txt', 'w+')
print("文件名为：", f.name)

# 定位到文件的末尾
# f.seek(0, 2)

str1 = "If you want to get something!\nYou have to give!\nYou have to learn, to insist!\n"
# 写入一个字符串
f.write(str1)

# 向文件写入一个序列字符串列表
str_list = ["If you really think it’s hard for you.\n", "Then you quit.\n",
            "Once you quit.\n", "Never complain.\n"]
f.writelines(str_list)

# 重新定位到文件的开始位置
f.seek(0, 0)

# 读取全部内容
print(f.read())

# 刷新缓冲区
f.flush()
# 关闭文件
f.close()

# 再次打开文件进行追加
f = open('ch13_test2.txt', 'a+')
f.write("Bye!")

f.seek(0, 0)
print(f.read())
f.close()








