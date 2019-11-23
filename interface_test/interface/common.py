"""将get/post封装为单独的方法"""
import requests,json
class method():
    def __init__(self):
        """在初始化方法中定义项目路径
            在其他方法中则可以直接使用
        """
        self.base_url = 'http://192.168.0.112/wuye/public/index.php/index/index/'
    def get(self,path,params):
        """
        定义方法，调用requests中的get请求
        path:接口的请求路径
        params:接口传入的参数
        """
        try:
            r = requests.get(self.base_url+path,params)
            #将接口的返回数据转换为字典
            re = json.loads(r.text)
            return re   #返回转换好的字典
        except:
            return {"message":path+"访问失败！"}
    def post(self,path,params):
        """
        定义方法，调用requests中的post请求
        path:接口的请求路径
        params:接口传入的参数
        """
        try:
            r = requests.post(self.base_url+path,data=params)
            #将接口的返回数据转换为字典
            re = json.loads(r.text)
            return re   #返回转换好的字典
        except:
            return {"message":path+"访问失败！"}
if __name__ == '__main__':
    m = method()  #创建对象
    p = {
    "username":13388888888,   #将参数定义到字典中
    "password":123456
    }
    info = m.get('login?',p)  #调用封装好的get请求
    print(info)