from threading import Thread,currentThread 
from time import sleep 

#线程函数
def fun(sec):
    print("线程属性测试")
    sleep(sec)
    #线程对象的getName()属性获取名称
    print("%s 线程结束"%currentThread().getName())

#创建线程
thread = []
for i in range(3):
    t = Thread(name = 'tedu%d'%i,\
        target = fun,args = (2,))
    thread.append(t)
    t.start()

print("is alive :",t.is_alive())  #查看线程状态
thread[1].setName("Tarena")  #设置线程名称
print(thread[1].name)

#回收线程
for i in thread:
    i.join()
