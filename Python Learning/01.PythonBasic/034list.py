# 034list.py
L = [3, 5]
L[:0] = [1, 2]
L[2:2] = [4]
L[len(L):len(L)] = [6]
L[:] = L[::-1]
print(L)

L = []
while True:
	n = int(input("请输入整数，输入-1结束"))
	if n == -1:
		break
	L += [n]
print(max(L), min(L), sum(L)/len(L))