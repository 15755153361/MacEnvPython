import os
from multiprocessing import Process
import time

def f(n):
    time.sleep(1)
    print(n*n)

if __name__ == '__main__':
    start_time = time.time()
    for i in range(10):
        p = Process(target=f,args=[i,])
        p.start()
    end_time = time.time()
    print('Total Time = {}'.format(end_time-start_time))
    time.sleep(3)
    print('--------------------Complete Process---------------- ')
    begin_time = time.time()
    for i in range(10):
        f(i)
    last_time = time.time()
    print('Total Time = {}'.format(last_time-begin_time))
