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
