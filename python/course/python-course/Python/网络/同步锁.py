from multiprocessing import Process,Lock
import time



def f(l,i):

    # 加锁
    l.acquire()

    try:
        print("Hello word %s time %s"%(i,time.time()))

    finally:
        # 释放锁
        l.release()

if __name__ == '__main__':


    lock = Lock()

    for i in range(10):

        p = Process(target=f,args=(lock,i))
        p.start()

