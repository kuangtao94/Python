# -*- coding: utf-8 -*-

import logging
# logging.basicConfig(level=logging.DEBUG)    # 配置日志的显示级别
# 通过格式化字符串指定输出信息的格式
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')


# -----------------------------------------
# 使用assert语句检测程序代码中的错误
# -----------------------------------------
# 如果参数类型不是字符串，则抛出AssertionError异常
def check_type(arg):
    assert type(arg) == str, "参数类型不是字符串"


check_type("10")

# 如果父亲的年龄小于儿子的年龄，就抛出AssertionError异常
f_age = 50      # 父亲的年龄
s_age = 22      # 儿子的年龄
assert f_age > s_age, "错误的父子年龄信息！"

# -----------------------------------------
# 使用日志模块logging打印跟踪信息，调试程序
# -----------------------------------------
x = 1
while x < 5:
    for y in range(1, 5):
        # 打印跟踪信息
        logging.info("x={}, y={}".format(x, y))

        # do something
        x += 1

# logging记录信息的级别有debug、info、warning、error和critical
logging.debug("logging debug")
logging.info("logging info")
logging.warning("logging warning")
logging.error("logging error")
logging.critical("logging critical")
