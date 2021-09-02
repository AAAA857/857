from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):

  return HttpResponse('Hello Django')

def book(request,i,D):

  return HttpResponse('Boox info %s,%s'%(i,D))


def login(request):

    # class Bookinfo():
    #
    #     def __init__(self,book_name,book_money):
    #
    #         self.name = book_name
    #         self.money = book_money
    #
    # oj1 = Bookinfo("西游记",100)
    # oj2 = Bookinfo("红楼梦",200)
    # oj3 = Bookinfo("水浒传",300)

    # Book_list = [ oj1, oj2, oj3 ]


    # 获取所有书籍信息
    Book_List = Book.objects.all()

    print(Book_List)

    return render(request,'login.html',locals())
    # return HttpResponse("login")


def mysql_add_author(request):

    author_list = ["李白","杜甫","白居易"]
    addr = "17600169910@163.com"

    for author in author_list:

        a1 = Book_Author_Emaill.objects.create(emaill=addr)

        Create_Auyhor = Book_Author_Info.objects.create(author_name=author,author_emaill=a1,author_gender=0)

    info = Book_Author_Info.objects.all()

    for i in info:

        print(i.author_emaill)

    return  HttpResponse("mysql_add_author")




def mysql_add_book(request):


    Book_List = [

        "三国演义",
        "红楼梦",
        "西游记"


    ]
    for i in Book_List:


        Create_Book = Book.objects.create(book_name=i,book_date="2021-08-08",book_publish_id=1)
        # 创建1对1 作者邮箱地址
        Create_Emaill = Book_Author_Emaill.objects.create(emaill="17600169910@163.com")
        # 创建作者信息
        Create_Author_Info = Book_Author_Info.objects.create(author_name="李白",author_emaill=Create_Emaill,author_gender=0)
        Create_Book.book_author.add(Create_Author_Info)


    return HttpResponse("ok")

def mysql_add_publish(request):


    '''创建方式一
    # 创建出版社信息
    publish_info = ["工业出版社","清华出版社","农业出版社"]

    for i in publish_info:

        # 创建出版社信息

        Create_Book_Publish = Book_Publish_Info.objects.create(publish_name=i)

        print(i)
    '''


    '''创建方式二
    
    #创建Book实例化对象
    publish_info = ["工业出版社","清华出版社","农业出版社"]
    
    for i in publish_info:
        
        # 信息
        # 第一次创建不会将数据保存在数据库中
        Create_Book_Publish = Book_Publish_Info(publish_name=i)
        # 调用save方法 将其保存在数据库中
        Create_Book_Publish.save()
    
    '''


    return  HttpResponse('add_sql')





