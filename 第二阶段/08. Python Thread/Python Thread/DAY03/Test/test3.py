from test import * 
import multiprocessing 
import time 

# def io():
#     write()
#     read()

counts = []
t = time.time()
for x in range(10):
    p = multiprocessing.Process(target = count,args = (1,1))
    counts.append(p)
    p.start()

for i in counts:
    i.join()
print("Process  cpu:",time.time() - t)