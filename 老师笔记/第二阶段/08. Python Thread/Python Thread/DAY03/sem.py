from multiprocessing import Semaphore,Process
from time import sleep 
import os 

#创建信号量
sem = Semaphore(3)

def fun():
    print("进程%d等待信号量"%os.getpid())
    #消耗一个信号量
    sem.acquire()
    print("进程%d消耗信号量"%os.getpid())
    sleep(3)
    sem.release()
    print("进程%d添加信号量"%os.getpid())

jobs = []
for i in range(4):
    p = Process(target = fun)
    jobs.append(p)
    p.start() 

for i in jobs:
    i.join()

print(sem.get_value())

