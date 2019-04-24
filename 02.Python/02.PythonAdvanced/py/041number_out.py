# 041number_out.py
def read():
	try:
		f = open('041number.txt')
		s = f.readline()
		L = list(int(i) for i in s.split(','))
	finally:
		f.close()
	print(L, max(L), sum(L))

read()