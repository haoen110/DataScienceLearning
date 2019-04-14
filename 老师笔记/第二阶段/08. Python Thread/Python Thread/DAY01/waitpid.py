import os
from time import sleep 

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    sleep(3)
    print("Child process exit",os.getpid())
    os._exit(3)
else:
    while True:
        sleep(1)
        #通过非阻塞的形式捕获子进程退出
        pid,status = os.waitpid(-1,os.WNOHANG)
        print(pid,status)
        print(os.WEXITSTATUS(status)) #获取子进程退出状态
    while True:
        pass