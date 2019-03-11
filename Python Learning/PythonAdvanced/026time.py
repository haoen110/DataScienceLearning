# 026time.py
import time
while True:
	a = time.time()
	h = time.gmtime(a)[3]
	m = time.gmtime(a)[4]
	s = time.gmtime(a)[5]
	print(h, ':', m, ':', s)
	time.sleep(1)