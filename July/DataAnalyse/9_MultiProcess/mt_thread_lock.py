import multiprocessing
import threading
import time

lock = threading.Lock()

balance = 0
def change_it(n,name):
    global balance    
    print('Enter Thread %s'%name)
    for i in range(10):
        lock.acquire()
        balance += n
        time.sleep(1)
        balance -= n
        lock.release()
        print('balance = %d name = %s'%(balance,name))


if __name__ == '__main__':
    name1 = 'thread_1'
    name2 = 'thread_2'
    thread_1 = threading.Thread(target=change_it , args=(5,name1))
    thread_2 = threading.Thread(target=change_it , args=(8,name2))
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    print('balance = %d'%balance)
