from xlwt import Workbook

#实例化Workbook对象
book = Workbook()
#新建sheet1工作表,创建sheet1对象
sheet1 = book.add_sheet("sheet1") #添加一个sheet
book.add_sheet("sheet2")
sheet1.write(0,0,r"F:\test1.xlsx") #通过sheet添加cell值
sheet1.write(0,1,r"F:\test2.xlsx")

row1 = sheet1.row(1)
row1.write(0,r"F:\test1.xlsx") #也可以通过row属性添加cell的值
row1.write(1,r"F:\test2.xlsx")

sheet1.col(0).width=10000
book.save(r"F:\test2.xls")