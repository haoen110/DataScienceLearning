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

    f.seek(size//2,0)
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