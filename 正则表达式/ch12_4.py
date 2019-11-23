# -*- coding: utf-8 -*-

import re


# --------------------------------
# 特殊需求表达式的校验
# --------------------------------
# 提取有效的手机号码(11位，以13、14、15、17、18开头)
phones = "13711710956 18888990656 37117109561 13711710 13900780866"
p2 = r'1[34578]\d{9}'
result = re.findall(p2, phones)
print(result)

# 月份有效性验证(01~09或10~12)
month = input("请输入您的生日所在月份：")
p3 = '^(0?[1-9]|1[0-2])$'
if re.match(p3, month):
    print("您的信息已保存！")
else:
    print("输入信息有误，请重新输入！")
