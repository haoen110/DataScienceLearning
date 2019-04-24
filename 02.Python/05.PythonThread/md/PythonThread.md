
# 线程

- 什么是线程
    - 线程也是一种多任务编程方法，可以利用计算机多核资源完成程序的并发执行。线程又被称为轻量级的进程。


- 线程**特征**
    * 线程计算机**多核分配**的最小单位
    * 一个进程可以包含**多个线程**
    * 线程也是一个运行的过程，消耗计算机资源，多个线程共享进程的资源和空间
    * 线程的创建删除**消耗的资源**都要远远小于进程
    * 多个线程之间执行互不干扰
    * 线程也有自己的特有属性，比如**指令集ID**

## threading 模块创建线程

`threading.Thread()`
- 功能：创建线程对象
- 参数：
    - name    线程名称  默认 Thread-1 
    - target  线程函数 
    - args    元组   给线程函数位置传参
    - kwargs  字典   给线程函数键值传参
 
`t.start()`  启动线程 自动运行线程函数  
`t.join([timeout])`  回收线程


```python
import threading 
from time import sleep 
import os 

a = 1

#线程函数
def music():
    global a
    print("a = ",a)
    a = 10000
    for i in range(5):
        sleep(2)
        print("播放葫芦娃",os.getpid())

#创建线程对象
t = threading.Thread(target = music)
t.start()

for i in range(5):
    sleep(1.5)
    print("想听灌篮高手",os.getpid())

t.join()

print("mian Thread a = ",a)
```

    a =  1
    想听灌篮高手 5507
    播放葫芦娃 5507
    想听灌篮高手 5507
    播放葫芦娃 5507
    想听灌篮高手 5507
    播放葫芦娃想听灌篮高手 5507 5507
    
    想听灌篮高手 5507
    播放葫芦娃 5507
    播放葫芦娃 5507
    mian Thread a =  10000


## 线程对象属性

`t.is_alive()`：查看线程状态  
`t.name`：线程名称  
`t.setName()`：设置线程名称  
`t.getName()`：获取线程名称  
`threading.currentThread()`：获取当前线程对象  


```python
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
    t = Thread(name = 'hhh%d'%i,\
        target = fun,args = (2,))
    thread.append(t)
    t.start()

print("is alive :",t.is_alive())  #查看线程状态
thread[1].setName("HHH")  #设置线程名称
print(thread[1].name)

#回收线程
for i in thread:
    i.join()
```

    线程属性测试
    线程属性测试
    线程属性测试
    is alive : True
    HHH
    hhh0 线程结束hhh2 线程结束
    HHH 线程结束
    


`t.daemon` 属性  
- 默认情况主线程退出不会影响分支线程执行
- 如果设置为True 则分支线程随主线程退出
    - 设置方法：  
        `t.daenon = True`  
        `t.setDaemon(True)`

    - 判断属性值  
        `t.isDaemon()`  

**要在start前设置，不会和join同用**


```python
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
```

    True
    =====主线程结束=====
    Daemon 测试


## 创建自定义线程类
- 步骤：
    1. 继承Thread
    2. 加载Thread中的__init__
    3. 重写run方法


```python
from threading import Thread 
from time import sleep,ctime

class MyThread(Thread):
    def __init__(self,target,name = 'hh',\
        args = (),kwargs = {}):

        super().__init__()
        self.name = name
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args,**self.kwargs)

def player(song,sec):
    for i in range(2):
        print("Playing %s:%s"%(song,ctime()))
        sleep(sec)

t = MyThread(target = player,args = ('凉凉',),\
    kwargs = {'sec':2})
t.start()
t.join()
```

    Playing 凉凉:Thu Apr 11 11:56:17 2019
    Playing 凉凉:Thu Apr 11 11:56:19 2019


## 线程通信
- 通信方法：多个线程共享进程的空间，所以线程间通信使用全局变量完成。
- 注意事项：线程间使用全局变量往往要同步互斥机制，保证通信安全

## 同步互斥方法

### 线程的event
`e = threading.Event()`创建事件对象  
`e.wait([timeout])`如果e为设置状态则不阻塞否则阻塞  
`e.set()`将e变为设置状态  
`e.clear()`清除设置  


```python
import threading 
from time import sleep 

s = None
e = threading.Event() 

def bar():
    print("bar拜山头")
    global s 
    s = "天王盖地虎"

def foo():
    print("说出口令就是自己人")
    sleep(2)
    if s == "天王盖地虎":
        print("我是座山雕,自己人")
    else:
        print("打死他")
    e.set()  #等foo验证完毕其他的再执行

def fun():
    print("呵呵..")
    sleep(1)
    global s
    s = "小鸡炖蘑菇"

b = threading.Thread(target = bar)
f = threading.Thread(target = foo)
b.start()
f.start()
e.wait() #运行b f之后其他内容不许执行

fun()
b.join()
f.join()
```

    bar拜山头
    说出口令就是自己人
    我是座山雕,自己人
    呵呵..


### 线程锁lock
`lock = threading.Lock()`创建锁对象  
`lock.acquire()`上锁  
`lock.release()`解锁  

**也可以通过with上锁，上锁状态调用acquire会阻塞**


```python
import threading 

a = b = 0

lock = threading.Lock()

def value():
    while True:
        lock.acquire()
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release()

t = threading.Thread(target = value)
t.start()

while True:
    #
    with lock:
        a += 1
        b += 1

t.join()
```

## python线程的GIL问题 （全局解释器锁）

*python-->支持多线程-->同步互斥-->加锁-->超级锁，给解释器加锁-->解释器同一时刻只能解释一个线程*

- 后果：
    - 一个解释器同一时刻只能解释执行一个线程，所以导致python线程效率低下。但是当遇到IO阻塞时线程会主动让出解释器，因此**python线程更加适合高延迟的IO程序并发**。


- 解决方法：
    * 尽量用进程完成并发
    * 不使用c解释器  c#  java
    * 尽量使用多种方案组合的方式进行并发操作，线程用作高延迟IO


- 效率测试
        Line cpu: 9.014907121658325
        Line IO: 4.548823118209839

        thread cpu: 9.38966417312622
        thread  IO: 4.6143529415130615

        Process  cpu: 5.466824531555176
        Process  IO: 2.9468178749084473

# 进程线程的区别和联系

1. 两者都是多任务编程方式，都能够使用计算机的多核资源
2. 进程的创建删除消耗的计算机资源比线程要多
3. 进程空间独立，数据相互不干扰，有专门的IPC，线程使用全局变量进行通信
4. 一个进程可以创建多个线程分支，两者之间存在包含关系
5. 多个线程公用进程的资源，在资源操作时往往需要同步互斥
6. 进程线程在系统中都有自己特有的属性，ID，代码段，栈区等资源

## 使用场景
* 需要创建较多并发，同时任务关联性比较强时一般用多线   程
* 不同的任务模块可能更多使用进程
* 使用进程线程需要考虑数据的处理复杂度，比如进程间通   信是否方便，同步互斥是否过于复杂

>### 要求： 
1. 进程线程的区别和联系
2. 进程间通信方式都知道哪些，有什么特点
3. 同步互斥意义是什么，什么情况下用
4. 给一个情形，分析下用进程还是用线程，理由
5. 一些常见概念挖掘 ： 僵尸进程，  进程状态，GIL

司机和售票员的故事
   * 创建父子进程分别代表司机和售票员
   * 当售票员收到SIGINT信号，给司机发送SIGUSR1信号此   时司机打印"老司机开车了"
   - 当售票员收到SIGQUIT信号，给司机发送SIGUSR2信号此时司机打印"车速有点快，系好安全带"
   - 当司机捕捉到SIGTSTP信号，给售票员发送SIGUSR1，售票员打印"到站了，请下车"
   * 到站后 售票员先下车，司机下车 （子进程先退出）

   *说明 ： SIGINT  SIGQUIT SIGTSTP从键盘发出*


```python
from multiprocessing import Process 
import os
from signal import * 
from time import sleep 

def saler_handler(sig,frame):
    if sig == SIGINT:
        os.kill(os.getppid(),SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif sig == SIGUSR1:
        print("到站了,请下车")
        os._exit(0)

def driver_handler(sig,frame):
    if sig == SIGUSR1:
        print("老司机,开车了")
    elif sig == SIGUSR2:
        print("车速有点快,系好安全带")
    elif sig == SIGTSTP:
        os.kill(p.pid,SIGUSR1)

#子进程代表售票员
def saler():
    signal(SIGINT,saler_handler) 
    signal(SIGQUIT,saler_handler)
    signal(SIGUSR1,saler_handler)
    signal(SIGTSTP,SIG_IGN)
    while True:
        sleep(2)
        print("Python带你去远方")


p = Process(target = saler)
p.start()

#父进程
signal(SIGUSR1,driver_handler)
signal(SIGUSR2,driver_handler)
signal(SIGTSTP,driver_handler)
signal(SIGINT,SIG_IGN)
signal(SIGQUIT,SIG_IGN)

p.join()
```
