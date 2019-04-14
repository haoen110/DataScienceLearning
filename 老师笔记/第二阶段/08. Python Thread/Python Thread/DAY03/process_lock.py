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