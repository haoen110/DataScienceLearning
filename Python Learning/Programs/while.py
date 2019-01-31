#while.py
i = 1
while i < 5:
	print("Hello World!")
	i += 1
else:
	print("条件不足，此时变量i=%d，循环结束"%i)
#方法一
i = 1
n = int(input("请输入要循环的次数"))
while i <= n:
	print("Hello World!")
	i += 1
else:
	print("条件不足，此时变量i=%d，循环结束"%i)
#方法2
n = int(input("请输入要循环的次数"))
while 1 <= n:
	print("Hello World!")
	n -= 1
else:
	print("条件不足，此时变量n=%d，循环结束"%n)
