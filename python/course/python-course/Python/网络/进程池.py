# 进程池对应 Pool 模块
from multiprocessing import Process,Lock,Pool
import  time
import os


def A(i):

    time.sleep(1)
    print("hello word! count=%d"%i)

    '''
    :return 回去的信息可以被callback函数引用
    
    '''
    return "AAAA"

def bar(info):
    '''
    :param  info  表示接收到pool内进程返回的数据
    :return:
    '''
    print("调用了callback, %s"%info)
    print(os.getpid())

if __name__ == '__main__':

    n = []
    '''
    :argument
    默认Pool 进程启动数量取决与系统核心数量
    processes=10  启动10个进程

    '''
    pool = Pool(processes=10,maxtasksperchild=5)
    print(os.getpid())
    time.sleep(10)
    for c in range(100):

        '''
        :argument
        pool.apply_async() 异步进程
        pool.apply()  顺序执行
        callback: 回调函数，当func执行成功后调用一个函数，主进程调用
        err_callback: 错误回调函数
        '''
        pool.apply_async(func=A,args=(c,), callback=bar)

    '''
    :argument 
    必须要加然后书写格式是固定的不能变
    pool.close()
    pool.join()
    '''
    pool.close()
    pool.join()





