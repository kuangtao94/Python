# -*- coding: utf-8 -*-


import datetime as dt                   # 给模块取个别名
from datetime import date as newdate    # 给模块中的类/方法/变量取别名

import math

print("今天的日期：", dt.date.today())
print("今天的日期：", newdate.today())

today = dt.date.today
print("今天的日期：", today())

new_math = math
print(new_math.pi)

# 模块的内置方法
# __dict__：显示模块的字典
print("__dict__:", dt.__dict__)

# __doc__：显示模块的文件字符串
print("__doc__:", dt.__doc__)

# __name__：显示模块的名称，用来标识命名空间
print("__name__:", dt.__name__)
# 一个模块被另一个程序第一次导入时，其主程序会被执行
print('__name__:', __name__)
if __name__ == '__main__':
    print('该模块自身在运行')
else:
    print('该模块被导入另一个程序时被运行')

# __file__：显示模块的完整文件路径
print("__file__:", dt.__file__)

# del：删除已加载的模块（从内存中清除）
del dt
