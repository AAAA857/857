from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.template import  Template,Context
import  json
# 爬虫模块
import urllib.request
import urllib3
import requests
import time



# Create your views here.
def index(request):

  return HttpResponse('Hello Django')

def book(request,i,D):

  return HttpResponse('Boox info %s,%s'%(i,D))



# Django Template Context 使用
def query(request):

    # 创建模板
    C_Template = Template("<h1>hello {{ name }}</h1>")

    # 实例化Context 生成模板
    C_Context = Context({"name": 123})

    C_Context = C_Template.render(C_Context)

    # Django 的render 就是实例化好 templates 静态文件，然后实例化Context 从而生成了最终的 浏览器能识别的内容调用HttpResponse返回

    print(C_Context)
    return  HttpResponse(C_Context)





# urlib 初始

def Curl(request):
    # urllib
    # 打开指定的爬取网页
    # response = urllib.request.urlopen("http://www.baidu.com")
    # # 获取打开网页的内容
    # html = response.read()
    # print(html)

    '''
    # urllib3
    # 特性
    线程安全
    连接池
    ssl/tls 验证
    '''

    # 创建PoolManager对象，用于处理线程池的链接于安全的所有细节
    http = urllib3.PoolManager()

    # 爬取网页
    # response = http.request('GET','http://www.baidu.com')
    # html = response.data


    # 获取指定数据
    P_response = http.request(
        'POST',
        'http://127.0.0.1:8000/app/registered/',
        fields={'word': 'hello'}
    )

    print(P_response)

    return HttpResponse("curl")


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
    #
    # Book_list = []
    #

    # 获取所有书籍信息
    Book_List = Book.objects.all()
    #
    # for i in Book_List:
    #
    #     Book_list.append(i)
    # print(Book_List)

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


def registered(request):

    if request.method == "GET":


        # locals()   // 获取局部变量信息
        return  render(request,"registered.html")


    else:
        # 获取URL 路径
        print("POST")
        print(request.path)

        print(request.POST.get('word'))
        # 获取URL 路径，如果有参数信息会显示
        # print(request.get_full_path())
        #
        # print(request.GET.get('word'))

        return  redirect("/app/")
        # return  HttpResponse("ok")

'''
template 自定义filter方法
'''
def Add(request):

    c = "A"
    sum = 100

    return  render(request,'test.html',locals())



def reg(request):


    return render(request,'ajax.html')


def check(request):

    status = {"status": True}

    return HttpResponse(json.dumps(status))


def calculate(request):

    status = json.dumps({ "sum": None})
    data1 = int(request.POST.get('number1'))
    data2 = int(request.POST.get('number2'))

    sum = data2 + data1
    #
    # print(data)

    return  HttpResponse(sum)



def auth(request):


    '''
    GET 请求返回登录页面

    :param request:
    :return:
    '''
    if request.method == "GET":

        '''
        添加session 属性
        '''



        d = request.session.get('time')

        print(d)

        return render(request,'auth.html',{'time': d})

    else:

        '''
        获取账号密码
        '''
        user = request.POST.get('user')
        passwrod = request.POST.get('password')

        print(user,passwrod)
        if user == "yin" and passwrod == "123":

            '''
            session 方式验证
            '''

            a_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(a_time)
            request.session['username'] = user
            request.session['password'] = passwrod
            request.session['time'] = a_time



            rep = redirect('/app/')

            # '''
            # cookie 方式验证登录
            # '''
            # rep.set_signed_cookie("is_login", "1", salt="ban", max_age=100)







            return rep

          # return rep
        else:

            return redirect('/auth/')
