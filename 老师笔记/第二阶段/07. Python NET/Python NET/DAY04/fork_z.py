import os 
from time import sleep 

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    print("Child Process:",os.getpid())
    print("Child process exit")
else:
    print("parent process")
    while True:
        pass 