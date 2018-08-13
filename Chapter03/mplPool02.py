# -*- coding: utf-8 -*-


from multiprocessing import Pool
import os, time, random

def worker(msg):
    t_start = time.time()
    print("任务 %s开始执⾏,进程号为%d" % (msg, os.getpid()))
    # random.random()随机⽣成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print( "任务 %s， 执⾏完毕， 耗时%0.2f 秒" % (msg, (t_stop - t_start)))

if __name__ == '__main__':
    print('⽗进程 %d.' % os.getpid())
    pool = Pool(3)  # 定义⼀个进程池， 最⼤进程数3
    for i in range(0, 10):
        # Pool.apply(要调⽤的⽬标,(传递给⽬标的参数元祖,))
        #  使⽤阻塞⽅式调⽤worker函数
        pool.apply(worker, (i,))

    pool.close()  # 关闭进程池， 关闭后po不再接收新的请求
    pool.join()  # 等待po中所有⼦进程执⾏完成， 必须放在close语句之后


