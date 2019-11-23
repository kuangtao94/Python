"""调用执行所有用例"""
from time import sleep  #导入代码休眠
from interface_test.test_data.excel_data import data
from interface_test.interface.common import method #导入接口访问方法
ex = data()  #创建对象
m = method()  #创建对象
count = 0  #设定变量，用来统计用例通过的次数
for i in range(2,ex.rows()+1):
    if ex.method(i) == 'get':
        r = m.get(ex.path(i),ex.param(i))  #调用get，访问第二行的用例
    elif ex.method(i) == "post":
        r = m.post(ex.path(i),ex.param(i)) #调用post
    if r['message']==ex.result(i): #如果用例执行通过
        ex.write_status(i,"通过")  #在excel中记录执行状态
        count = count+1  #用例通过一次，计数加1
    else: #如果测试失败
        ex.write_status(i,'不通过') #记录执行状态
        sleep(2)
        ex.write_result(i,r["message"]) #将接口实际的返回写入到Excel中

num = count/(ex.rows()-1)*100 #通过用例的数量除以用例总数量
ex.write(2,10,"%d%s"%(num,'%'))

