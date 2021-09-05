import  threading
import  time

def hi(num):

    print("hello %s"%num)
    # 子线程不执行完sleep不会退出
    time.sleep(3)


# 主线程
if __name__ == '__main__':

    # target = 需要子线程执行的函数任务
    # args =  函数需要传入的参数
    # 子线程1
    T1 = threading.Thread(target=hi,args=(1,))
    T1.start()
    # 子线程2
    T2 = threading.Thread(target=hi, args=(2,))
    T2.start()

    # join 等待子线程结束后，在执行主进程
    # 如果不加join 会按顺序执行代码，主进程执行完退出，子线程继续执行
    T1.join()
    T2.join()
    # 执行到这里，表示主进程已经结束
    print("ending...")

