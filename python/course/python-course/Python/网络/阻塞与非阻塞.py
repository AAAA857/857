'''
阻塞I/O 与 非阻塞I/O
'''
import socket
import  time

def Server(obj):

    while True:

        print("server 等待客户端链接")
        # accept 属于阻塞住进程
        conn,addr = obj.accept()

        while 1:

            try:
                data = conn.recv(1024)

                print("数据:%s"%data)

                # 发送数据
                rs = conn.send(data)
            except Exception as es:

                break


if __name__ == '__main__':

    sk = socket.socket()
    sk.bind(("127.0.0.1", 8080))
    sk.listen(5)

    while True:

        Server(sk)