# wt.py
import time
import os

while True:
	time.sleep(1)
	print(time.ctime(), os.getpid())