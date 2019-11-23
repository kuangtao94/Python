import pymysql
import datetime

#安装 pip install pymysql
"""
1、连接本地数据库
2、建立游标
3、创建表
4、插入表数据、查询表数据、更新表数据、删除表数据
"""
#连接本地数据库
db = pymysql.connect(
    host = "localhost", #数据库的主机地址
    user = "root",      #数据库登录的用户名
    passwd = "123456",  #数据库登录的密码
    database = "test"   #数据库名字
)

#创建游标
cursor = db.cursor()

def create_table():
    #如果存在student表，则删除
    cursor.execute("DROP TABLE IF EXISTS student")

    #创建student表 --元组
    sql = """
        create table student(
        id int not null,
        name char(10),
        age int,
        address char(20),
        create_time datetime)
    """

    try:
        # 执行SQL语句
        cursor.execute(sql)
        print("创建数据库成功")
    except Exception as e:
        print("创建数据库失败：case%s"%e)
    finally:
        pass
        #关闭游标连接
        # cursor.close()
        # 关闭数据库连接
        # db.close()


def insert_into():
    #批量插入数据
    sql = "INSERT INTO  student VALUES(%s,%s,%s,%s,%s)"
    params = [
        (1,"小王",23,"深圳",datetime.datetime.now()),
        (2,"小刘",24,"深圳",datetime.datetime.now()),
        (3,"小宋",25,"深圳",datetime.datetime.now())
    ]

    try:
        # 执行SQL语句 批量插入用executemany
        cursor.executemany(sql,params)
        # 提交到数据库执行
        db.commit()
        print("有",cursor.rowcount,"插入数据成功")
    except Exception as e:
        print("插入数据失败：case%s"%e)
        # 如果发生错误则回滚
        db.rollback()
    finally:
        pass
        # 关闭游标连接
        # cursor.close()
        # 关闭数据库连接
        # db.close()

def update_Set():
    #SQL语句更新数据
    sql = """UPDATE student SET address = '东莞' WHERE ID = %s"""%(2)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("有",cursor.rowcount,"更新数据成功")

    except Exception as e:
        print("数据更新出错：case%s"%e)
        #发生错误是回滚
        db.rollback()

    finally:
        pass
        # 关闭游标连接
        # cursor.close()
        # 关闭数据库连接
        # db.close()


def select_form():
    # SQL 查询语句 --条件查询
    sql = "SELECT * FROM student WHERE ID = %s"%(2)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表 fetchall
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            age = row[2]
            address = row[3]
            create_time = row[4]
            print("id=%s,name=%s,age=%s,address=%s,create_time=%s"%\
                  (id,name,age,address,create_time))

    except Exception as e:
        print("查询出错：case%s"%e)

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def exit():
    """退出系统"""
    import sys
    sys.exit()
    print("退出系统")

def main():
    while True:
        choice = int(input("请选择下面的数字:\n"
                           "1.创建表\n"
                           "2.插入数据\n"
                           "3.更新数据\n"
                           "4.查询数据\n"
                           "5.退出系统\n"
                           ))
        if choice == 1:
            create_table()
        elif choice == 2:
            insert_into()
        elif choice == 3:
            update_Set()
        elif choice == 4:
            select_form()
        else:
            exit()

if __name__ == "__main__":
    main()
