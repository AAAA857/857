'''
python 因为又GIL锁 不能真正实现多线程工作，
python适合用于I/O密集多线程，
对于计算密集型的任务，python多线程不推荐。

抢占CPU类型:
    1.进程
    2.线程


协程:

    属于协作式，非抢占模式
    属于线程执行


'''
import  time

def c(name):


    print("生产包子")
    while True:

        new_baozi = yield
        print(new_baozi)
        print("[%s] is eating baozi %s"%(name,new_baozi))


def p():

    r = con1.__next__()
    r = con2.__next__()
    n = 0

    while True:

        time.sleep(1)

        print("\033[32m;1m[p]\033[0m is makeing baozi %s and %s"%(n,n + 1))
        con1.send(n)
        con2.send(n+1)
        n += 2

if __name__ == '__main__':

    # 创建俩个生成器，生成俩个对象
    con1 = c("con1")
    con2 = c("con2")
    # 创建一个消费者
    p()