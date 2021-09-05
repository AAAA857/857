from bottle import template, Bottle, request, redirect, static_file, response
import bottle
import json
import requests
from multiprocessing import Process
import time
import queue

# 静态文件位置
bottle.TEMPLATE_PATH.append('./templates/')
root = Bottle()
p_quere = queue.Queue()

# 静态文件位置
@root.route("/static/<filename>")
def static(filename):
    return static_file(filename, root="./static")


@root.route("/", method=["GET", "POST"])
def login():
    if request.method == "GET":

        '''
        1 获取请求首部cookie信息
        2 当获取到cookie后证明用户已经登录过，直接返回业务界面
        '''
        user_cookie = request.get_cookie("user")

        if user_cookie:

            return (Read_Database())

        else:

            return template("login1.html")



    else:
        v = request.forms
        k = request.query
        # GET 发送过来的请求
        l = request.body
        # POST 发送过来的body请求
        # request.headers #请求头部信息
        # request.files   #上传文件信息
        # request.GET
        # request.POST
        # request.cookies
        # request.params  # POST GET 发送过来的信息
        # request.environ # 环境相关信息

        # 获取用户名
        user = v.get("user")
        # 获取密码
        pwd = v.get("pwd")

        return Check_User(user, pwd)


'''
    1. 读取client端本地磁盘信息
    2. 用于前端展示

'''


def Read_Database():
    # 打开数据库
    with open(file='file/databases.txt', mode='r', encoding='utf-8') as r:
        # 反序列化数据类型
        info = json.load(r)

    with open(file='file/info.txt', mode='r', encoding='utf-8') as r2:
        r3 = json.load(r2)
    #     r3 = [{"name": "127.0.0.1", "file": "/root/yin", "status": "ongoing"},{"name": "127.0.0.1", "file": "/root/yin", "status": "ongoing"}]
    return template("ok.html", new_li=info, data=r3)


def Select_Database(data):
    with open(file='file/databases.txt', mode='r', encoding='utf-8') as r:

        info = json.load(r)
        for i in info:

            client = i
            if client['client'] == data:
                d_json = json.dumps(i)

                return d_json

        return "false"


'''
    1.校验前段页面登录账号密码
'''


def Get_User(user, pwd):
    status = False
    with open(file='file/user.txt', mode='r', encoding='utf-8') as r:

        for i in r.readlines():

            username = i.split(":")[0].strip()
            password = i.split(":")[1].strip()

            if user == username and pwd == password:

                status = True

            else:
                continue

        return status


def Check_User(user, pwd):
    # 获取验证返回状态
    respon = Get_User(user, pwd)

    if respon:
        '''
            1. 校验成功后进入业务界面
        '''
        # 在响应首部添加cookie
        response.set_cookie("user", user, max_age=800)
        # response.set_cookie( user, max_age=10)

        return Read_Database()

    else:

        return template("false.xhtml")


'''
    1. 注册函数
'''


@root.route("/Registered/", method=["GET", "POST"])
def Registered():
    if request.method == "GET":

        return template("registered.xhtml")

    else:

        # 获取到form表单中的信息
        info = request.POST

        user = info.get('user')
        pwd = info.get('pwd')

        User_Create(user, pwd)
        # 跳转页面
        return redirect("/")


@root.route("/d/", method=["POST"])
def post_d():
    info = request.params.keys()

    for i in info:
        data = json.loads(i)

    c_c = data['Client']
    c_f = data['File']
    new_li = []
    with open(file="file/info.txt", mode="r", encoding="utf-8") as r:

        j_data = json.loads(r.read())

        for i in j_data:

            i_c = i['name']
            i_f = i['file']

            if i_c == c_c and i_f == c_f:

                f1 = {
                    "name": i['name'],
                    "file": i['file'],
                    "status": "successful"
                }
                new_li.append(f1)
            else:

                new_li.append(i)

    with open(file='file/info.txt', mode='w', encoding='utf-8') as w:

        d_json = json.dumps(new_li)
        # print(d_json)
        w.write(d_json)

    return "200"


@root.route("/delete_file_info/", method=["POST"])
def delete_file_info():
    with open(file='file/info.txt', mode="w", encoding="utf-8") as w:
        w.write("[]")

    return True



def wirte_database(data):


    with open(file="file/databases.txt", mode="w", encoding="utf-8") as w_f:


        w_f.write(json.dumps(data))

    return True

def add_database(data):
    print("开始操作了:%s" % data)
    print("type: %s" % type(data))
    # 数据库临时空列表
    new_li = []
    # 获取读文件句柄
    flag = ""
    with open(file="file/databases.txt", mode="r", encoding="utf-8") as r_f:

        # 获取数据库信息 list类型
        database_info = json.loads(r_f.read())
        print(database_info)

        info = data

        directory = info.get("directory")
        permissions = info.get("permissions")
        client = info.get("client_ip")
        ping = info.get("ping")

        database_dict = {

            "directory": directory,
            "permissions": permissions,
            "client": client,
            "ping": ping

        }

        for n in range(len(database_info)):

            print(n)
            print(database_info[n])
            if "client" in database_info[n] and "client" in database_dict:

                if database_info[n]["client"] == database_dict["client"]:

                    print("get True")

                    flag = 2

                else:
                    print("get True")
                    flag = 1

            new_li.append(database_info[n])

        if not database_info or flag == 1:

            print("flag: 写入 %s"%flag)

            database_dict["id"] = (len(new_li) + 1) - 1

            new_li.append(database_dict)

            wirte_database(new_li)


        print("列表 %s" %database_info)
        print("长度 %s"%bool(database_info))
        print("flag: 不写入 %s" % flag)

        return "200"

def consumer():
    consumer_data = p_quere.get()

    print("消息来了:%s" % consumer_data)

    add_database(consumer_data)

    p_quere.join()


@root.route("/post/", method=["POST"])
def post_test():
    b = request.params.keys()

    for i in b:

        info = json.loads(i)

    p_quere.put(info)

    p_quere.task_done()

    consumer()

    return "200"


# 健康状态检测
def health():
    l = []
    with open(file='file/databases.txt', mode='r', encoding='utf-8') as r:
        r.write()

        a = json.loads(r.read())
        for i in range(len(a)):

            b = a[i]

            try:
                cli = b['client']
                requests.get("http://%(ip)s:8811/health" % {'ip': cli}, timeout=2).text
                print("监控检测通过")
            except requests.exceptions.RequestException:
                print("监控检测不通过")
                with open(file='file/databases.txt', mode='w', encoding='utf-8') as w:
                    s = a.pop(i)
                    print("删除%s"%s)
                    k = json.dumps(a)
                    w.write(k)

def h():
    while True:
        health()
        time.sleep(10)


def status_info(a, b):
    with open(file='file/info.txt', mode='r', encoding='utf-8') as r:
        ac = json.loads(r.read())

        dict_tempalte = {

            'name': a,
            'file': b,
            'status': 'ongoing'

        }

        ac.append(dict_tempalte)

        with open(file='file/info.txt', mode='w', encoding='utf-8') as w:

            w.write(json.dumps(ac))


# 新增函数调用
def Action_Add(info):
    # 获取字典信息
    ID = info.get('ID')
    Client = info.get('CLIENT')
    directory = info.get('directory')
    u = info.get('url')

    URL = "http://" + Client + ':' + '8811' + "/"
    A = json.dumps(info)

    a_client = info["CLIENT"]
    a_file = info["remote_file"]

    r = status_info(a_client, a_file)

    try:
        requests.post(URL, data=A, timeout=1)
    except:
        pass


@root.route("/select/", method="POST")
def select():
    info = request.POST.get("info").strip()
    info = str(info).split(" ")
    '''
    1.获取到前段需要查询的IP地址
    2.查询本地数据库返回前端
    '''

    IP = info[0]
    Data = Select_Database(IP)
    return Data


@root.route("/case/", method="POST")
def Case():
    info = request.POST.get('info')

    info = json.loads(info)

    new_dict = {
        "ID": info['id'],
        "CLIENT": info['client'],
        "directory": info['directory'],
        "info": info['directory_path'],
        "user": info['Directory_user'],
        "password": info['Directory_password'],
        "action": info['action'],
        "remote_file": info['Directory_file'],
        "remote_ip": info['remote_ip']
    }

    return Action_Add(new_dict)


@root.route("/text2pcm.html")
def show():
    return template("text2pcm.html")


# 注册函数
def User_Create(user, pwd):
    with open(file='file/user.txt', mode='a', encoding='utf-8') as w:
        a = user + ":" + pwd

        w.write(a + "\n")


def server():
    obj = root.run(host='0.0.0.0', port=8082)

    return obj


if __name__ == '__main__':
    p1 = Process(target=server, args="")
    p2 = Process(target=h, args="")
    p1.start()
    p2.start()