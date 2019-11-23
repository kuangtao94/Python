#类(面向对象)  PageObject设计模式  unittest 知识体系

#函数式编程
import datetime
book_info = {
    "title":"Python",
    "price":"33.1",
    "auther":"毛桃",
    "publisher":"北京大学",
    "pubdate":datetime.datetime.today()
}

def seacher_book(book):
    print("这本书的主题是:{}".format(book_info["title"]))
    print("这本书的价格是:{}".format(book_info["price"]))
    print("这本书的作者是:{}".format(book_info["auther"]))
    print("这本书的出本社是:{}".format(book_info.get("publisher")))
    print("这本书的出版时间是:{}".format(book_info.get("pubdate")))
#
# if __name__ == '__main__':
#     seacher_book(book_info)

#构造方法
# class Book:
#     def __init__(self,title,author,price,publisher,pubdate):
#         self.title = title
#         self.author = author
#         self.price = price
#         self.publisher = publisher
#         self.pubdate = pubdate
#
# book = Book("Selenium",'Teacher',"43.33","清华大学",datetime.datetime.today())
# print(book.title)
# print(book.author)
# print(book.price)
# print(book.publisher)
# print(book.pubdate)

#类构造函数
# class Book:
#     def __init__(self,title,author,price,publisher,pubdate):
#         self.title = title
#         self.author = author
#         self.price = price
#         self.publisher = publisher
#         self.pubdate = pubdate
#
#     def seacher_book(self):
#         print("这本书的主题是:{}".format(self.title))
#         print("这本书的价格是:{}".format(self.price))
#         print("这本书的作者是:{}".format(self.author))
#         print("这本书的出本社是:{}".format(self.publisher))
#         print("这本书的出版时间是:{}".format(self.pubdate))
#
# if __name__ == '__main__':
#     book = Book("Selenium",'Teacher',"43.33","清华大学",datetime.datetime.today())
#     book.seacher_book()

#默认值的写法
# class Book:
#     def __init__(self,
#                  title = "Appium测试",
#                  author = "",
#                  price = 0.0,
#                  publisher = None,
#                  pubdate = datetime.datetime.now()):
#         self.title = title
#         self.author = author
#         self.price = price
#         self.publisher = publisher
#         self.pubdate = pubdate
#
#     def seacher_book(self):
#         print("这本书的主题是:{}".format(self.title))
#         print("这本书的价格是:{}".format(self.price))
#         print("这本书的作者是:{}".format(self.author))
#         print("这本书的出本社是:{}".format(self.publisher))
#         print("这本书的出版时间是:{}".format(self.pubdate))
#
# if __name__ == '__main__':
#     book = Book("Selenium")
#     book.seacher_book()


# #类的继承
# #父类
# class Book:
#     def __init__(self,title,author,price):
#         self.title = title
#         self.author = author
#         self.price = price
#
#     def seacher_book(self):
#         print("这本书的主题是:{}".format(self.title))
#         print("这本书的作者是:{}".format(self.author))
#         print("这本书的价格是:{}".format(self.price))
#
# #子类
# class ReadBook(Book):
#     def readbook(self):
#         print("该书正在读中...")
#
#
# #实例化子类
# book = ReadBook("Python经典","Tao","11.42")
# book.seacher_book()
# book.readbook()


#类的重写
#父类
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def seacher_book(self):
        print("这本书的主题是:{}".format(self.title))
        print("这本书的作者是:{}".format(self.author))
        print("这本书的价格是:{}".format(self.price))

#子类
class ReadBook(Book):
    #构造方法 --初始化方法 (放的是公共的东西)
    def __init__(self,title,author,price,publisher,pubdate):
        Book.__init__(self,title,author,price)
        self.publisher = publisher
        self.pubdate = pubdate

    def readbook(self):
        print("该书正在读中...")

    def seacher_book(self):
        print("这本书的主题是:{}".format(self.title))
        print("这本书的价格是:{}".format(self.price))
        print("这本书的作者是:{}".format(self.author))
        print("这本书的出本社是:{}".format(self.publisher))
        print("这本书的出版时间是:{}".format(self.pubdate))

#实例化子类
book = ReadBook("Python经典","Tao","11.42","清华大学出版社",datetime.datetime.now())
book.readbook()
book.seacher_book()
