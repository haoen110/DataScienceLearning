# 041number_in.py
def read():
	L = []
	while True:
		n = int(input("请输入数字，为负数结束："))
		if n < 0:
			break
		else:
			L.append(n)
	return(L)

def write():
	L = list(str(i) for i in read())
	f = open('041number.txt', mode='w')
	for i in L:
		if i == L[len(L)-1]:
			f.write(i)
		else:
			f.write(i)
			f.write(',')
	f.close()

write()
