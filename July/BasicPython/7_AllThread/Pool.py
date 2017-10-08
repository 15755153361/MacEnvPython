from multiprocessing import Pool
import time

def f(x):
    print(x * x)
    time.sleep(2)
    return pow(x,2)

if __name__ == '__main__':
    pool = Pool(processes = 5)
    res_list = []

    for i in range(10):
        res = pool.apply(f,[i,])
        print('-------:',i)
        res_list.append(res)
    pool.close()
    pool.join()
    for r in res_list:
        print("result = ",r.get(timeout=5))





