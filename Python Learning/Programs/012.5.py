# 012.5.py
a = int(input("请输入第1门成绩"))
b = int(input("请输入第2门成绩"))
c = int(input("请输入第3门成绩"))

max = a
if b > max:
	max = b
if c > max:
	max = c
print("max=", max)
