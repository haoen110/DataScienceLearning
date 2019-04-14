# mulcpy.py
import multiprocessing as mp
from time import sleep

f = open('mulcpy1')
count = len(f.readlines()) // 2
print(count)
f.close()

def copy():
	f = open('mulcpy1')
	w = open('mulcpy2', 'w')
	w.writelines(f.readlines()[:count])
	f.close()
	w.close()

p = mp.Process(target = copy)
p.start()

sleep(2)
f = open('mulcpy1')
w = open('mulcpy2', 'a')
w.writelines(f.readlines()[count:])
f.close()
w.close()

p.join()



