#list.py
L = [3, 5]
L[:0] = [1, 2]
L[3:3] = [4]
L += [6]
L2 = L[::-1]
del L2[-1]
print(L2)

n = []
while True:
	i = int(input("请输入列表中的数，-1为结束"))
	if i != -1:
		n += [i]
	else:break
ave = sum(n)/len(n)
print("您输入了%d个数" % len(n))
print("您输入的最大值为%d" % max(n))
print("您输入的最小值为%d" % min(n))
print("您输入的平均值为%d" % ave)
