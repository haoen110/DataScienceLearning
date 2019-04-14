from multiprocessing import Process,Value 
import time 
import random 

#创建共享内存
money = Value('i',2000)

#操作共享内存增加
def deposite():
    for i in range(100):
        time.sleep(0.05)
        #对value属性操作即操作共享内存数据
        money.value += random.randint(1,200)
#取钱
def withdraw():
    for i in range(100):
        time.sleep(0.04)
        money.value -= random.randint(1,180)

d = Process(target = deposite)
w = Process(target = withdraw)
d.start()
w.start()
d.join()
w.join()

print("余额:",money.value)

