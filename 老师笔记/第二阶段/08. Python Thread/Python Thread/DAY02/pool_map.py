from  multiprocessing import Pool 
import time 

def fun(n):
    time.sleep(1)
    print("执行 pool map事件")
    return n * n

pool = Pool(4)
#使用map将事件放入进程池
r = pool.map(fun,range(10))
pool.close()
pool.join()
print(r)

