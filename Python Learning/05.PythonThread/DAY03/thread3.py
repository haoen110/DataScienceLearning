#daemon属性
from threading import Thread
from time import sleep 

def fun():
    sleep(3)
    print("Daemon 测试")

t = Thread(target = fun)

t.setDaemon(True) 
print(t.isDaemon())  

t.start()

print("=====主线程结束=====")