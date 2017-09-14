from multiprocessing import Process,Queue
import time

def write(q):
    for i in ['A','B','C','D','E']:
        print('Put %s to queue' % i)
        q.put(i)
        time.sleep(0.5)

def read(q):
    while True:
        v = q.get(True)
        print('get %s from queue' % v)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    print('write process = ',pw)
    print('read  process = ',pr)
    pw.start()
    pr.start()
    pr.join()
    pr.terminate()
    pw.terminate()
