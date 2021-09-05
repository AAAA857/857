from flask import Flask,request
import requests
import json
from multiprocessing import Process,Lock
import time
import os
from shell import Command
from  logger import  Logger
from functools import wraps

# 创建一个flask对象
# print(__name__)
# 路由地址
# path 对应的路径
# @app.route('/user/<path:path>/<b>')
# any 表示符合元祖内是所有内容

dir = os.path.dirname(os.path.realpath(__file__))
IP = ""
Clietn_IP = ""
def get_directory_env(function):

    @wraps(function)
    def bar(self,*args,**kwargs):
        Ping_IP = os.getenv("Ping_Host")
        Check_Directory = os.getenv("Check_Directory")
        fun = function(self ,Ping_IP,Check_Directory)
        return fun
    return bar


def Action_env(function):
    @wraps(function)
    def bar(self,*args,**kwargs):
        '''
        :param IP = 'http://10.125.128.196:31928/post/'
        '''
        global IP
        IP = os.getenv("Web_Server")
        # IP = 'http://127.0.0.1:8082/post/'
        fun = function(self,IP)
        return fun
    return bar


def case_env(function,*args,**kwargs):
    @wraps(function)
    def bar(self,*args,**kwargs):

        Port = os.getenv("Scp_Port")
        Password = os.getenv("Scp_Pass")
        Scp_User = os.getenv("Scp_User")
        Scp_Host = os.getenv("Scp_Host")

        res = function(self ,*args, Port, Password, Scp_User, Scp_Host)
        return res
    return bar

class Client(object):


    '''
    发送到server字典
    保存数据信息
    '''
    heard_dict = {

        "directory": "None",
        "directory_name": "None",
        "permissions": "None",
        "client_ip": "None",
        "ping": "None"

    }


    '''
    1. 客户端获取当前环境信息，注册到server端
    2. 接收server 发送过来的命令进行工作
    '''
    def __init__(self):

        '''
        实例化一个class
        用于命令行执行
        '''
        self.command_file = os.path.join(dir, "log", "command.log")
        self.command = Command(self.command_file)
        self.agent_file = os.path.join(dir, "log", "agent.log")
        self.log = Logger(self.agent_file, "INFO")

    '''
    获取环境信息
    '''
    @get_directory_env
    def get_directory(self,Ping_IP,Check_Directory):
        # global Clietn_IP
        self.heard_dict["ping"] = self.command.Check("ping -c 1 %s"%Ping_IP)
        self.heard_dict["directory"] = self.command.Check("ls %s"%Check_Directory)
        self.heard_dict["permissions"] = str(self.command.shell_command("stat -c %a " + Check_Directory),encoding="UTF-8").strip()
        self.heard_dict["client_ip"] = str(self.command.shell_command("hostname -i"),encoding="UTF-8").strip()
        self.heard_dict["directory_name"] = Check_Directory

        # self.heard_dict["ping"] = "True"
        # self.heard_dict["directory"] = "True"
        # self.heard_dict["permissions"] = "755"
        # global  Clietn_IP
        # self.heard_dict["client_ip"] = "127.0.0.1"
        # Clietn_IP = self.heard_dict["client_ip"]
        # self.heard_dict["directory_name"] = "/"
        # Clietn_IP = self.heard_dict["client_ip"]
        return self.heard_dict

    @Action_env
    def Action(self,IP):

        # render_template 返回一个index页面
        # 可以使用jina2模板进行传参
        # return render_template("index.xhtml",k1="root")

        res = self.get_directory()

        requests.post(IP,json.dumps(res))

        return True
    def post_scp_delete(self,info):

        s_localtime = time.asctime(time.localtime(time.time()))
        print("1")
        dic = {
            "Client": str(self.command.shell_command("hostname -i"),encoding="UTF-8").strip(),
            "File": info['remote_file'],
            "Status": "successful",
            "Action": "pull"
        }
        print("2")
        e_localtime = time.asctime(time.localtime(time.time()))

        requests.post(url=os.getenv("Web_Server_Action") ,data=json.dumps(dic))


    def case(self,data):

        info = data
        '''
        {
        'ID': '0', 
        'CLIENT': '127.0.0.1', 
        'directory': 'True', 
        'info': '/tmp', 
        'user': 'root', 
        'password': 'baidu@123', 
        'action': 'case', 
        'remote_file': '/a/b.txt', 
        'remote_ip': '192.168.1.1'
        }
        '''
        com = "/usr/bin/sshpass -p %(Password)s scp -o StrictHostKeyChecking=no -P %(Port)s -r %(Scp_User)s@%(Scp_Host)s:%(File)s %(dir)s"%{
        'Password': info['password'],
        'Scp_User': info['user'],
        'Scp_Host': info['remote_ip'],
        'File': info['remote_file'],
        'dir': info['info'],
        "Port": 65522
        }

        self.command.shell_command(com)

        self.post_scp_delete(info)

        return "true"

    # 反射
    def Post_Action(self,info):

        data = info

        '''反射'''
        if hasattr(self, "{}".format(data["action"])):
            '''获取方法'''
            getattr(self, "{}".format(data["action"]))(data)

    # 健康状态检测
    def health(self):

        return "200"

obj = Client()

if __name__ == '__main__':

    app = Flask(__name__)


    @app.route('/health')
    def h():
        return obj.health()

    @app.route('/',methods=["GET","POST"])
    def run():

        if request.method == "GET":

            return obj.Action()

        elif request.method == "POST":

            # 接收到请求
            get_json = request.data

            get_json = json.loads(get_json)
            obj.Post_Action(get_json)
            return "200"
        else:
            return "501"

    def abc():

        obj = app.run(host='0.0.0.0', port=os.getenv("client_port"), debug=True)

        return obj

    def test_process():
        while 1:
            time.sleep(10)
            obj.Action()
    # 多进程模型
    p = Process(target=abc,args="")
    p1 = Process(target=test_process,args="")
    p.start()
    lock = Lock()
    p1.start()