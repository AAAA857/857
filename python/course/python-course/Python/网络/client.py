import socket






def Client(obj):



    info = input("请输入内容:")


    obj.send(info.encode("utf-8"))

    data = obj.recv(1024).decode()

    print("来着server消息:%s"%data)


if __name__ == '__main__':


    sk = socket.socket()

    sk.connect(("127.0.0.1",8080))
    while True:

         Client(sk)