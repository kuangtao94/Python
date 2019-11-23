# -*- coding: utf-8 -*-

# -----------------------------------------
# 自定义异常
# -----------------------------------------
class ExitLoop(Exception):
    pass


try:
    x = 1
    while x < 5:
        for y in range(1, 5):
            print(x, y)

            if (x == 3) and (y == 3):
                # 通过抛出一个异常，直接跳出多层嵌套循环
                raise ExitLoop

            x += 1
except ExitLoop:
    print("当x = 3, y = 3时跳出嵌套循环")


class CustomError(Exception):
    def __init__(self, err='自定义错误'):
        Exception.__init__(self, err)


raise CustomError




