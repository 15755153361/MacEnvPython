from multiprocessing import Process,Value,Array
import os

def f(n,a):
    print('This is child process (%s)' % os.getpid())
    n.value = 3.1415926
    for i in range(len(a)):
        a[i] = -a[i]
if __name__ == '__main__':
    num = Value('d',0.0)
    arr = Array('i',range(10))
    print('This is father Process (%s)' % os.getpid())
    p = Process(target = f,args=(num,arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])



