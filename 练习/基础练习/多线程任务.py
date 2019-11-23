# 多线程实例

# 例1.单线程
from time import sleep,ctime
def task1(taskName):
    for i in range(2):
        print("正在执行 %s %s"%(taskName,ctime()))
        sleep(2)

def task2(taskName):
    for i in range(2):
        print("正在执行 %s %s"%(taskName,ctime()))
        sleep(1)

if __name__ == '__main__':
    task1("任务一")
    task2("任务二")


# 例2
from time import sleep,ctime
def task(taskName,time):
    for i in range(2):
        print("正在执行 %s %s"%(taskName,ctime()))
        sleep(time)

if __name__ == '__main__':
    task("任务一",2)
    task("任务二",1)

if __name__ == '__main__':
    task("任务一",2)
    task("任务二",1)

# 例3 引入线程
from time import sleep,ctime
import threading #引入线程模块
def task(taskName,time):
    for i in range(2):
        print("正在执行 %s %s"%(taskName,ctime()))
        sleep(time)

#将所有线程组装到threads中
threads = []

#将任务存放置线程中
t1 = threading.Thread(target=task,args=("任务一",2))
t2 = threading.Thread(target=task,args=("任务二",1))
threads.append(t1)
threads.append(t2)

if __name__ == '__main__':
    #启动线程 start()
    for i in threads:
        i.start()
    #结束主线程
    print("结束主线程%s"%ctime())


# 4.多线程 --守护线程join()
from time import sleep,ctime
import threading #引入线程模块
def task(taskName,time):
    for i in range(2):
        print("正在执行 %s %s"%(taskName,ctime()))
        sleep(time)

#将所有线程组装到threads中
threads = []
#将任务存放置线程中
t1 = threading.Thread(target=task,args=("任务一",2))
t2 = threading.Thread(target=task,args=("任务二",1))
threads.append(t1)
threads.append(t2)

if __name__ == '__main__':
    #启动线程 start()
    for i in threads:
        i.start()
    #守护进程 join()
    for i in threads:
        i.join()
    #结束主线程
    print("结束主线程%s"%ctime())

# 例5 优化线程的创建 批量生成线程
from time import sleep,ctime
import threading #引入线程模块
def task(taskName,time):
    for i in range(2):
        print("正在执行 %s %s"%(taskName,ctime()))
        sleep(time)
#定义存储所有任务的列表
tasks = [("任务一",2),("任务二",1)]
#将所有线程组装到threads中
threads = []

#批量生成线程
def createThread():
    for taskName,time in tasks:
        t1 = threading.Thread(target=task,args=(taskName,time))
        threads.append(t1)

if __name__ == '__main__':
    #批量生成线程
    createThread()
    #启动线程 start()
    for i in threads:
        i.start()
    #守护进程 join()
    for i in threads:
        i.join()
    #结束主线程
    print("结束主线程%s"%ctime())


# 例6 根据用户输入的任务和时间,批量生成线程
from time import sleep,ctime
import threading #引入线程模块
def task(taskName,time):
    for i in range(2):
        print("正在执行 %s %s"%(taskName,ctime()))
        sleep(time)

#定义存储所有任务的列表
# tasks = [("任务一",2),("任务二",1)]
tasks = []
#接收用户输入的任务名和时长,追加到tasks中
def rectask(taskName,time):
    tasks.append((taskName,time))

#将所有线程组装到threads中
threads = []

#创建批量生成线程
def createThread():
    for taskName,time in tasks:
        t1 = threading.Thread(target=task,args=(taskName,time))
        threads.append(t1)

if __name__ == '__main__':
    nums = int(input('请输入你要执行的任务次数:'))
    for i in range(nums): #range(2) 0,1
        taskName = input("请输入第%s任务名称"%(i+1))
        time = int(input("请输入第%s任务执行的时长"%(i+1)))
        #将任务和时长组装到tasks列表中
        rectask(taskName,time)
    #批量生成线程
    createThread()
    #启动线程 start()
    for i in threads:
        i.start()
    #守护进程 join()
    for i in threads:
        i.join()
    #结束主线程
    print("结束主线程%s"%ctime())