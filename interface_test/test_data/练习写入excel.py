"""
xlrd:读取excel工具
xlutils : 写入excel的方法
需要使用pip install xlutils来安装工具
"""
import xlrd  #导入读取excel工具
from xlutils.copy import copy  #复制方法
#打开文件，保持excel中的格式
wb = xlrd.open_workbook(r'D:\Test\Python基础入门\interface_test\test_data\接口测试用例.xls',formatting_info=True)
wb1 = copy(wb)  #备份打开的文件
wb1.get_sheet(1).write(1,1,'hello world')  #向指定单元格写数据
wb1.save(r'D:\Test\Python基础入门\interface_test\test_data\接口测试用例.xls')  #保存修改
