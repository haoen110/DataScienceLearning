# 033.py
n = int(input("请输入一个整数，代表树干的高度"))
for i in range(1, n+1):
	s = '*' * (i * 2 - 1)
	print(s.center(n * 2 - 1))
root = "*".center(n * 2 - 1)
print(root)
print(root)

for i in range(ord('A'), ord('Z') + 1):
	print(chr(i), end=' ')
print()

m = ord('a') - ord('A')
for i in range(ord('A'), ord('Z') + 1):
	print(chr(i), chr(i + m), sep='', end=' ')
print()

for i in range(100, 1000):
	b = (i // 100)
	s = (i - b * 100) // 10
	g = (i - b * 100 - s * 10)
	if b ** 3 + s ** 3 + g ** 3 == i:
		print(i,"是水仙花数")

for bai in range(1, 10):
	for shi in range(10):
		for ge in range(10):
			x = bai * 100 + shi * 10 +ge
			if x == bai *** 3 + shi ** 3 + ge ** 3
				print(x)


