from threading import Thread
import time

def my_counter():
    print('Go Into my_counter...')
    i = 0
    for _ in range(100000000):
        i += 1
    return True

def main():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target = my_counter)
        t.start()
        thread_array[tid] = t
        print('tid = ',tid,'thread_array[tid] = ',thread_array[tid])
    for i in range(2):
        print('Thread need to join...')
        thread_array[i].join()
    print('Thread Done...')
    end_time = time.time()
    print('Total time: {}'.format(end_time - start_time))
    
if __name__ == '__main__':
    main()
