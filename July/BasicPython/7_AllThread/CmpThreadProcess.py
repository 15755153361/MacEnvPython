from multiprocessing import Process,Queue
import threading
import time
lock = threading.Lock()

def run(info_list,n):
    lock.acquire()
    info_list.append(n)
    lock.release()
    print('%s'%info_list)

def run_all(queue,n):
    lock.acquire()
    queue.put(n)
    lock.release()
    while not queue.empty():
        print('%s'%queue.get())
if __name__ == '__main__':
    info = []
    queue = Queue()
    print('----------------------Process------------------')
    for i in range(10):    
        p = Process(target=run_all,args=[queue,i])
        p.start()
        p.join()

    time.sleep(1)
    print('----------------------threading------------------')
    for i in range(10):
        p = threading.Thread(target=run,args=[info,i])
        p.start()
        p.join()

