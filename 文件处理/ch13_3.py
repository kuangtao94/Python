# -*- coding: utf-8 -*-


import os


# --------------------------------
# 使用os模块操作目录和文件
# --------------------------------
# getcwd() 获取当前目录路径
cwd = os.getcwd()
print("当前目录：", cwd)

# mkdir() 创建单级目录，如果目录已存在会报错
os.mkdir('./temp')

# rename() 重命名目录或文件
os.rename('./temp', './ch13')

# abspath() 将相对路径转换为绝对路径
abs_path = os.path.abspath('./ch13')
print("绝对路径是：", abs_path)

# 解决方法一(目录已存在)
if not os.path.exists('./ch13'):
    # 先确定目录不存在，再创建
    os.mkdir('./ch13')

# 解决方法二(目录已存在)
# 进行异常捕获
try:
    os.mkdir('./ch13')
except FileExistsError:
    print("目录已存在！")

# rmdir() 删除单级空目录，若不为空无法删除
try:
    os.rmdir('ch13')
except OSError as oe:
    print(oe.strerror)


# 解决方法(删除的目录不为空)
dir_name = 'ch13'
# 获得目录下的文件列表
file_list = os.listdir('./{}'.format(dir_name))
# 如果列表不为空
if file_list:
    print(file_list)
    for f in file_list:
        # 循环列表，逐个删除文件，清空目录
        os.remove('./{}/{}'.format(dir_name, f))
# 最后删除空目录
os.rmdir(dir_name)


# makedirs() 创建多级目录
os.makedirs('./dir1/dir2/dir3')

# removeddirs() 删除多级空目录
os.removedirs('./dir1/dir2/dir3')


file_path = r'D:\PycharmProjects\Python零基础快速入门\test.txt'
# split() 将路径分解为文件夹和文件名
print("分解路径：", os.path.split(file_path))

# dirname() 获取路径中的文件夹部分
dir_name = os.path.dirname(file_path)
print("文件夹：", dir_name)

# basename() 获取路径中的文件名
file_name = os.path.basename(file_path)
print("文件名：", file_name)

# join() 将目录名和文件名进行拼接
path_name = os.path.join(dir_name, file_name)
print("文件完整路径：", path_name)

