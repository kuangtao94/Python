"""设计方法，读取excel中的数据"""
import xlrd,ast  #读取excel数据,将字符串转换为字典
from xlutils.copy import copy #操作excel 可以通过pip install xlutils来安装
class data():
    def __init__(self):
        """初始化excel文件/打开文件"""
        self.file = r'D:\Test\Python基础入门\interface_test\test_data\接口测试用例.xls'
        self.wb = xlrd.open_workbook(self.file)
    def get_data(self,n):
        """获取指定行的数据"""
        table = self.wb.sheet_by_index(0)  #获取第一个页签
        values = table.row_values(n-1)  #通过索引获取行
        return values  #返回一行数据
    def method(self,n):
        """获取用例中的请求方法"""
        value = self.get_data(n)  #调用get_data方法，获取一行
        return value[3]  #返回该行的第4格
    def path(self,n):
        """获取用例的请求路径"""
        value = self.get_data(n)  #调用get_data方法，获取一行
        return value[4]  #返回该行的第5格
    def param(self,n):
        """获取用例中的传入参数"""
        value = self.get_data(n)  #调用get_data方法，获取一行
        v = ast.literal_eval(value[5])  #将excel中的字符串转换为字典
        return  v #返回该行的第6格
    def result(self,n):
        """获取用例中的预期结果"""
        value = self.get_data(n)  #调用get_data方法，获取一行
        return value[6]  #返回该行的第七格
    def rows(self):
        """获取当前excel表有多少行"""
        table = self.wb.sheet_by_index(0)  #获取第一个页签
        return table.nrows #获取当前页签的行数
    def write(self,r,c,message):
        """向excel中写入数据,r:行号 c:列号 message代表写入的内容"""
        rb = xlrd.open_workbook(self.file,formatting_info=True)
        wb = copy(rb)  #获取备份
        wb.get_sheet(0).write(r-1,c-1,message)  #往单元格中写入
        wb.save(self.file)  #保存修改好的文件
    def write_status(self,n,status):
        """写入用例执行的状态,是否通过 n:行号
         status:用例执行的状态"""
        self.write(n,8,status)  #将用例执行的状态写入到第8列
    def write_result(self,n,result):
        """写入用例执行的实际结果 n:行号 result:接口实际返回结果"""
        self.write(n,9,result)  #将用例执行的结果写入到第9列
if __name__ == '__main__':
    ex = data()  #创建对象
    print(ex.path(3))
    print(ex.param(2))
    print(ex.rows())
    ex.write_status(8,"通过") #往第8行写 通过