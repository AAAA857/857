import  queue
import threading
import time

l = ['1','2','3','4']

'''
        下面的案例将会启动3个线程进行清空最后一个列表元素，
        但是没有加锁的，会出现一个资源已经被消费掉，
        从而导致另外一个进程没有进行正常的消费
'''
# def s1():
#     while l:
#         a = l[-1]
#         print(a)
#         time.sleep(2)
#         # try:
#         l.remove(a)
#         # except Exception as e:
#         #     print(a)
#
# # t1 = threading.Thread(target=s1,args="")
# for i in  range(3):
#
#     i=threading.Thread(target=s1,args="")
#     i.start()



'''

import queue 是导入一个线程队列

队列主要面向于线程内的安全,用于线程与线程之间用于通信。

队列启动后默认卡在get位置，等待队列中有新的元素进来

队列模式:
    1. 先进先出     默认模式
        put(A) --> get() = A
        
    2. 先进后出
        put(A)
        put(B) --> get() = B
        
'''
def Test_Queue():

    # 创建一个线程队列
    q = queue.Queue()

    # 往队列中新增元素
    q.put(123)
    q.put({"a":123})

    while q:

        d = q.get()

        print(d)

Test_Queue()
