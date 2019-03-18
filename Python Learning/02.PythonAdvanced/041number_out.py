# 041number_out.py
def read():
	f = open('041number.txt')
	s = f.readline()
	L = list(int(i) for i in s.split(','))
	f.close()
	print(L, max(L), sum(L))

read()