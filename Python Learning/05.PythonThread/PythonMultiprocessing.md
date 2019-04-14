
# multiprocessing 模块创建进程

1. 需要将要执行的事情封装为函数
2. 使用multiprocessing模块中Process类创建进程对象
3. 通过对象属性设置和Process的初始化函数对进程进行设置，绑定要执行的函数
4. 启动进程，会自动执行进程绑定的函数
5. 完成进程的回收


`mp.Process()`
- 功能：创建进程对象
- 参数：
    - name  进程名称  Process-1
    - target  绑定函数 
	- args  元组  给target函数按照位置传参
    - kwargs  字典  给target函数按照键值对传参

`p.start()`
- 功能：启动进程
    * target函数会自动执行，此时进程真正被创建

`p.join([timeout])`
- 功能：阻塞等待回收子进程
- 参数：超时时间


1. 使用multiprocessing创建子进程，同样子进程复制父进程的全部代码段，父子进程各自执行互不影响，父子进程有各自的运行空间
2. 如果不使用join回收子进程则子进程退出后会成为僵尸进程
3. 使用multiprocessing创建子进程往往父进程只是用来创建进程回收进程


```python
import multiprocessing as mp 
from time import sleep 

a = 1
def fun():
    sleep(3)
    global a
    print("a = ",a)
    a = 10000
    print("子进程事件")
    print("**********")

#创建进程对象
p = mp.Process(target = fun) # 相当于之前pid==0的部分



#启动子进程
p.start() # 由于sleep3秒，所以父进程先执行

sleep(2)
print("这是父进程")

#回收进程
p.join()

print("parent a = ",a)
print("**********")
```

    这是父进程
    a =  1
    子进程事件
    **********
    parent a =  1
    **********



```python
from  multiprocessing import Process 
from time import sleep 
import os 

def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(),'----',os.getpid()) # 获取父进程的pid和自己的pid
def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(),'----',os.getpid())
def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(),'----',os.getpid())

things = [th1,th2,th3] 
process = [] # 为了后面可以循环回收

for th in things:
    p = Process(target = th)
    process.append(p)
    p.start()

#循环回收进程
for i in process:
    i.join()
```

    睡觉
    934 ---- 2198
    吃饭
    934 ---- 2197
    打豆豆
    934 ---- 2199


练习：创建父子进程，分别将一个文件的上半部分和下半部分复制到一个新的文件中。
- 注意
    1. 如果子进程从父进程拷贝对象，对象和网络或者文件相关联，那么父子进程会使用同一套对象属性，相互有一定的关联性
    2. 如果在子进程中单独创建对象，则和父进程完全没有关联


```python
import os 
from multiprocessing import Process 

filename = "./byte.png"
#获取文件大小
size = os.path.getsize(filename)

#如果子进程使用父进程的对象,那么相互之间有偏移量的影响
# f = open(filename,'rb')

#复制前半部分
def copy1():
    f = open(filename,'rb')
    n = size // 2
    fw = open('file1.png','wb') 

    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()

#复制下半部分
def copy2():
    f = open(filename,'rb')
    fw = open('file2.png','wb')

    f.seek(size//2,0) # 从0开始数到size//2的位置
    while True:
        data = f.read(1024)
        if not data:
            break 
        fw.write(data)
    fw.close()
    f.close()

p1 = Process(target = copy1)
p2 = Process(target = copy2)
p1.start()
p2.start()
p1.join()
p2.join()
```

## Process进程对象属性

`p.start()`  
`p.join()`

`p.is_alive()`  
- 判断进程生命周期状态，处于生命周期得到True否则返回False

`p.name`
- 进程名称 默认为Process-1

`p.pid`  
- 进程的PID号


```python
from multiprocessing import Process 
from time import sleep 

#带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

p = Process(target = worker,args = (2,),\
    kwargs = {'name':'Daivl'},name = "Worker") # name将进程名称改为Worker，否则默认为process1
p.start()

print("Process name:",p.name) #进程名称
print("Process PID:",p.pid) #获取进程PID

#进程alive情况
print("Process is alive:",p.is_alive())

p.join(3)
print("==================")
```

    Process name: Worker
    Process PID: 2715
    Process is alive: True
    I'm Daivl
    I'm working...
    ==================
    I'm Daivl
    I'm working...
    I'm Daivl
    I'm working...


`p.daemon `
- 默认状态False  主进程退出不会影响子进程执行
- 如果设置为True 则子进程会随着主进程结束而结束

* 要在start前设置
* 一般不和join一起使用


```python
from multiprocessing import Process 
from time import sleep,ctime 

def tm():
    while True:
        sleep(2)
        print(ctime())

p = Process(target = tm)

p.daemon = True
p.start()
sleep(5)
print("main process exit")
```

# 创建自定义进程类

1. 继承Process
2. 编写自己的\_\_init\_\_ ,同时加载父类init方法
3. 重写run方法，可以通过生成的对象调用start自动运行



```python
from multiprocessing import Process 
import time 

class ClockProcess(Process):
    def __init__(self,value):
        self.value = value 
        super().__init__()

    #重写run方法
    def run(self):
        for i in range(5):
            print("The time is {}".\
                format(time.ctime()))
            time.sleep(self.value)

#创建自定义进程类的对象
p = ClockProcess(2)

#自动调用run
p.start()
p.join()
```

    The time is Wed Apr 10 11:40:52 2019
    The time is Wed Apr 10 11:40:54 2019
    The time is Wed Apr 10 11:40:56 2019
    The time is Wed Apr 10 11:40:58 2019
    The time is Wed Apr 10 11:41:00 2019


## 多进程优缺点
- 优点：
    - 可以使用计算机多核，进行任务的并发执行，提高执行效率
    - 空间独立，数据安全
	- 运行不受其他进程影响，创建方便
- 缺点：
    - 进程的创建和删除消耗的系统资源较多

# 进程池技术
- 产生原因：
    - 如果有大量任务需要多进程完成，则可能需要频繁的创建删除进程，给进算计带来较多的资源消耗。

- 原理：
    - 创建适当的进程放入进程池，用来处理待处理事件，处理完毕后进程不销毁，仍然在进程池中等待处理其他事件。
    - 进程的复用降低了资源的消耗。


- 使用方法
    1. 创建进程池，在池内放入适当的进程
    2. 将事件加入到进程池等待队列
    3. 不断取进程执行事件，直到所有事件执行完毕
    4. 关闭进程池，回收进程

`from multipeocessing import  Pool`

`Pool(processes)`
- 功能：创建进程池对象
- 参数：表示进程池中有多少进程

`pool.apply_async(func,args,kwds)`
- 功能：将事件放入到进程池队列
- 参数：
    - func 事件函数
    - args 以元组形式给func传参
	- kwds 以字典形式给func传参
- 返回值：返回一个代表进程池事件的对象

`pool.apply(func,args,kwds)`
- 功能：将事件放入到进程池队列
- 参数：
    - func 事件函数
    - args 以元组形式给func传参
	- kwds 以字典形式给func传参

`pool.close()`
- 功能：关闭进程池

`pool.join()`
- 功能：回收进程池


```python
from multiprocessing import Pool 
from time import sleep,ctime 

def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

#创建进程池
pool = Pool(processes = 4)

result = []
for i in range(10):
    msg = "hello %d"%i
    #将事件放入进程池队列,等待执行
    r = pool.apply_async(func = worker,args = (msg,))
    result.append(r)

#关闭进程池
pool.close()

#回收
pool.join()

for i in result:
    print(i.get())  #获取事件函数的返回值
```

    hello 3
    hello 2
    hello 1
    hello 0
    hello 6
    hello 7
    hello 5
    hello 4
    hello 9
    hello 8
    Wed Apr 10 11:57:07 2019
    Wed Apr 10 11:57:07 2019
    Wed Apr 10 11:57:07 2019
    Wed Apr 10 11:57:07 2019
    Wed Apr 10 11:57:09 2019
    Wed Apr 10 11:57:09 2019
    Wed Apr 10 11:57:09 2019
    Wed Apr 10 11:57:09 2019
    Wed Apr 10 11:57:11 2019
    Wed Apr 10 11:57:11 2019


`pool.map(func,iter)`
- 功能：将要做的时间放入进程池
- 参数： 
    - func  要执行的函数
    - iter  迭代对象
- 返回值 ： 返回事件函数的返回值列表


```python
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
```

    执行 pool map事件
    执行 pool map事件
    执行 pool map事件
    执行 pool map事件
    执行 pool map事件
    执行 pool map事件
    执行 pool map事件
    执行 pool map事件
    执行 pool map事件
    执行 pool map事件
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 进程间通信（IPC）

- 原因：
    - 进程空间相对独立，资源无法相互获取，此时在不同进程间通信需要专门方法。
- 进程间通信方法：
    - 管道、消息队列、共享内存、信号、信号量、套接字

## 1、管道通信  Pipe

- 通信原理：
    - 在内存中开辟管道空间，生成管道操作对象，多个进程使用**"同一个"**管道对象进行操作即可实现通信

`from multiprocessing import Process,Pipe`

`fd1,fd2 = Pipe(duplex = True)`
- 功能：创建管道
- 参数：
    - 默认表示双向管道
    - 如果设置为False则为单向管道
- 返回值：
    - 表示管道的两端
    - 如果是双向管道，都可以读写
	- 如果是单向管道，则fd1只读，fd2只写

`fd.recv()`
- 功能：从管道读取信息
- 返回值：读取到的内容  
**如果管道为空则阻塞**

`fd.send(data)`
- 功能：向管道写入内容
- 参数：要写入的内容  
**可以发送python数据类型**


```python
from multiprocessing import Process,Pipe 
import os,time 

#创建管道对象
fd1,fd2 = Pipe(False) 

def fun():
    time.sleep(3)
    #向管道写入内容
    fd2.send([1,2,3,4,5])

jobs = []
for i in range(5):
    p = Process(target=fun)
    jobs.append(p)
    p.start()

for i in range(5):
    #读取管道
    data = fd1.recv()
    print(data)

for i in jobs:
    i.join()
```

    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]


## 2、消息队列

- 队列：先进先出
- 通信原理：
    - 在内存中建立队列数据结构模型。多个进程都可以通过队列存入内容，取出内容的顺序和存入顺序保持一致

### 创建队列
`q = Queue(maxsize = 0)`
- 功能：创建消息队列
- 参数：表示最多存放多少消息。默认表示根据内存分配存储
- 返回值：队列对象

`q.put(data,[block,timeout])`
- 功能：向队列存储消息
- 参数：
    - data 要存的内容
    - block 默认队列满时会阻塞，设置为False则非阻塞
    - imeout 超时时间

`data = q.get([block,timeout])`
- 功能：获取队列消息
- 参数：
    - block 默认队列空时会阻塞，设置为False则非阻塞
    - timeout 超时时间
- 返回值：返回取出的内容

`q.full()`   判断队列是否为满  
`q.empty()`  判断队列是否为空  
`q.qsize()`  判断队列中消息数量  
`q.close()`  关闭队列  


```python
from multiprocessing import Queue 
from time  import sleep 

#创建队列
q = Queue(3)

q.put(1)
sleep(0.5)
print(q.empty())
q.put(2)
print(q.full())
q.close() #关闭队列
```


```python
from multiprocessing import Process,Queue 
import time  

#创建消息队列
q = Queue()

def fun1():
    time.sleep(1)
    q.put({'a':1,'b':2})

def fun2():
    time.sleep(2)
    print("收到消息:",q.get())

p1 = Process(target = fun1)
p2 = Process(target = fun2)
p1.start()
p2.start()
p1.join()
p2.join()
```

    收到消息: {'a': 1, 'b': 2}


## 3、共享内存 

- 通信原理：在内存空开辟一块空间，对多个进程可见，进程可以写入输入，但是每次写入的内容会覆盖之前的内容。

`obj = Value(ctype,obj)`
- 功能：开辟共享内存空间
- 参数：
    - ctype  要存储的数据类型
    - obj  共享内存的初始化数据
- 返回值：共享内存对象

`obj.value` 即为共享内存值，对其修改即修改共享内存


```python
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
```

    余额: 2532


`obj = Array(ctype,obj)`
- 功能：开辟共享内存空间
- 参数：
    - ctype  要存储的数据格式
    - obj  初始化存入的内容 比如列表，字符串，如果是整数则表示开辟空间的个数
- 返回值：返回共享内存对象
    - 可以通过遍历过户每个元素的值
           e.g.  [1,2,3]  ---> obj[1] == 2
           如果存入的是字符串
           obj.value 表示字符串的首地址


               管道         消息队列       共享内存
    开辟空间   内存         内存           内存

    读写方式   两端读写     先进先出       覆盖之前内容
               双向/单向

    效率       一般          一般          较高

    应用       多用于父     广泛灵活       需要注意
               子进程                      进行互斥操作


```python
from multiprocessing import Process,Array 
import time 

#创建共享内存,初始放入列表
# shm = Array('i',[1,2,3,4,5])

#创建共享内存,开辟5个整形空间
# shm = Array('i',5)

#存入字符串,要求bytes格式
shm = Array('c',b'Hello')

def fun():
    for i in shm:
        print(i)
    shm[0] = b'h'

p = Process(target = fun)
p.start()
p.join()

for i in shm:
    print(i)
print(shm.value) #打印字符串
```

    b'H'
    b'e'
    b'l'
    b'l'
    b'o'
    b'h'
    b'e'
    b'l'
    b'l'
    b'o'
    b'hello'


## 信号通信

- 一个进程向另一个进程发送一个信号来传递某种讯息，接受者根据接收到的信号进行相应的行为  

- 终端：`kill -l`   
    - 查看系统信号    
- 终端：`kill  -sig  PID`
    - 向一个进程发送信号

- 关于信号
    - 信号名称  信号含义   默认处理方法

            SIGHUP  连接断开
            SIGINT  CTRU-C
            SIGQUIT CTRU-\
            SIGTSTP CTRL-Z
            SIGKILL 终止一个进程
            SIGSTOP 暂停一个进程
            SIGALRM 时钟信号
            SIGCHLD 子进程状态改变时给父进程发出
            python 发送信号
            signal  
            
            1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL
            5) SIGTRAP	 6) SIGABRT	 7) SIGEMT	 8) SIGFPE
            9) SIGKILL	10) SIGBUS	11) SIGSEGV	12) SIGSYS
            13) SIGPIPE	14) SIGALRM	15) SIGTERM	16) SIGURG
            17) SIGSTOP	18) SIGTSTP	19) SIGCONT	20) SIGCHLD
            21) SIGTTIN	22) SIGTTOU	23) SIGIO	24) SIGXCPU
            25) SIGXFSZ	26) SIGVTALRM	27) SIGPROF	28) SIGWINCH
            29) SIGINFO	30) SIGUSR1	31) SIGUSR2
            
- `os.kill(pid,sig)`
    - 功能： 发送信号
    - 参数： 
        - pid 目标进程
        - sig 要发送的信号



```python
import os 
import signal 

#向20959发送信号
os.kill(20959,signal.SIGKILL)
```

`import signal`

`signal.alarm(sec)`
- 功能：向自身发送时钟信号 --> SIGALRM
- 参数：sec  时钟时间

**进程中只能有一个时钟，第二个会覆盖第一个时间**

- 同步执行：按照顺序逐句执行，一步完成再做下一步
- 异步执行：在执行过程中利用内核记录延迟发生或者准备处理的事件。这样不影响应用层的持续执行。当事件发生时再由内核告知应用层处理

**信号是唯一的异步通信方法**


```python
import signal
import time
signal.alarm(3)

while True:
    time.sleep(0.8)
    print("等待时钟信号")
```

`signal.pause()`
- 功能：阻塞等待接收一个信号


```python
import signal
import time 

signal.alarm(3)
time.sleep(2)
signal.alarm(5) # 进程中只能有一个时钟，若第一个未触法，第二个会将第一个覆盖

signal.pause() #阻塞等待信号

while True:
    time.sleep(1)
    print("等待时钟信号.....")
```

`signal.signal(signum,handler)`
- 功能：处理信号
- 参数： 
    - signum  要处理的信号
    - handler 信号的处理方法 
        - SIG_DFL  表示使用默认的方法处理
        - SIG_IGN  表示忽略这个信号
        - func     传入一个函数表示用指定函数处理
            - def func(sig,frame)
                - sig：捕获到的信号
                - frame：信号对象


```python
import signal 
from time import sleep 

signal.alarm(5)

#使用默认方法处理信号
# signal.signal(signal.SIGALRM,signal.SIG_DFL)

#忽略信号
signal.signal(signal.SIGALRM,signal.SIG_IGN)
signal.signal(signal.SIGINT,signal.SIG_IGN)

while True:
    sleep(2)
    print("press ctrl-c !")
    print("等待时钟....")
```


```python
from signal import * 
import time 

#信号处理函数
def handler(sig,frame):
    if sig == SIGALRM:
        print("接收到时钟信号")
    elif sig == SIGINT:
        print("就不结束")

alarm(5)

signal(SIGALRM,handler)
signal(SIGINT,handler)

while True:
    print("Waiting for a signal")
    time.sleep(2)
```

## 信号量（信号灯）

- 原理：给定一个数量，对多个进程可见，且多个进程都可以操作。进程通过对数量多少的判断执行各自的行为。

multiprocessing --> Semaphore()

`sem = Semaphore(num)`
- 功能：创建信号量
- 参数：信号量初始值
- 返回：信号量对象

`sem.get_value()`获取信号量值  
`sem.acquire()`将信号量减1，当信号量为0会阻塞  
`sem.release()`将信号量加1  


```python
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

print(sem.get_value())b
```

# 进程的同步互斥

- 临界资源：多个进程或者线程都能够操作的共享资源
- 临界区：操作临界资源的代码段


- **同步**：同步是一种合作关系，为完成某个任务，多进程或者多线程之间形成一种协调，按照约定或条件执行操作临界资源。
- **互斥**：互斥是一种制约关系，当一个进程或者线程使用临界资源时进行上锁处理，当另一个进程使用时会阻塞等待，直到解锁后才能继续使用。

## Event  事件
multiprocessing  --> Event

`e = Event()`创建事件对象  
`e.wait([timeout])`设置事件阻塞  
`e.set()`事件设置，当事件被设置后e.wait()不再阻塞  
`e.clear()`清除设置 当事件设置被clear后 e.wait又会阻塞  
`e.is_set()`事件状态判断  


```python
from multiprocessing import Event 

#创建事件对象
e = Event()

e.set()  #设置事件

print(e.is_set())

e.wait(3)

e.clear()
e.wait()
```


```python
from multiprocessing import Process,Event 
from time import sleep 

def wait_event():
    print("想操作临界区")
    e.wait() 
    print("开始操作临界区资源",e.is_set())
    with open("file") as f:
        print(f.read())

def wait_event_timeout():
    print("也想操作临界区")
    e.wait(2) 
    if e.is_set():
        with open("file") as f:
            print(f.read())
    else:
        print("不能读取文件")

#事件对象
e = Event()
p1 = Process(target = wait_event)
p1.start()
p2 = Process(target = wait_event_timeout)
p2.start()

print("主进程操作")
with open('file','w') as f:
    sleep(3)
    f.write("I love China")
e.set()
print('释放临界区')

p1.join()
```

## Lock 锁

`lock = Lock()` 创建对象  
`lock.acquire()` 上锁，如果锁已经是上锁状态调用此函数会阻塞  
`lock.release()` 解锁  

    with lock：   上锁
       ....
       ....
                  解锁


```python
from multiprocessing import Process,Lock 
import sys 
from time import sleep 

def writer1():
    lock.acquire()
    for i in range(20):
        sys.stdout.write("writer1想先向终端写入\n")
    lock.release()

def writer2():
    lock.acquire()
    for i in range(20):
        sys.stdout.write("writer2想先向终端写入\n")
    lock.release()

lock = Lock()

w1 = Process(target = writer1)
w2 = Process(target = writer2)

w1.start()
w2.start()
w1.join()
w2.join()
```
