import os 
from time import sleep,ctime 

while True:
    sleep(3)
    print(ctime(),os.getpid())