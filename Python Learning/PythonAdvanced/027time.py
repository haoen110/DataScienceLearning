# 027time.py
import time
a = time.time()
h = time.gmtime(a)[3]
m = time.gmtime(a)[4]
s = time.gmtime(a)[5]
print("现在时间是：", h, ':', m, ':', s)

h1 = int(input("请输入小时"))
m1 = int(input("请输入分钟"))
s1 = int(input("请输入秒钟"))
while True:
	a = time.time()
	h = time.gmtime(a)[3]
	m = time.gmtime(a)[4]
	s = time.gmtime(a)[5]
	if h1 == h and m1 == m and s1 == s:
		print("时间到啦！！") 
		break
	