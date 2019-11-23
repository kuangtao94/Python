import xlrd,xlwt

#xlrd 是读取excel数据 xlwt 是写入excel数据
#python自带的标准库是不能读取数据的,需要用到扩展包xlrd
#打开excel
data = xlrd.open_workbook(r"F:\test.xlsx") #注意workbook是小写字母

#查看文件中包含sheet的名称
data.sheet_names()
#得到第一个工作表,可以通过索引顺序或者工作表名称
table = data.sheet_by_index(0)
table = data.sheet_by_name(u"Sheet1")
table = data.sheets()[0]
#获取行数和列数
nrows = table.nrows
ncols = table.ncols
#获取整行和整列的值(数组)
table.row_values()
table.col_values()

