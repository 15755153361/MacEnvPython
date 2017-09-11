from threading import Thread
import time

def my_counter():
    print('Go Into my_counter...')
    i = 0
    for _ in range(100000000):
        i = i+1
    return True

def main():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t =Thread(target = my_counter)
        print('t = ',t)
        t.start()
        t.join()
    end_time = time.time()
    print('Total Time:{}'.format(end_time - start_time))

if __name__ == '__main__':
    main()

