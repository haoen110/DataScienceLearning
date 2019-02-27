# 012.py
d = int(input("请输入行驶的公里数："))
if d <= 3:
	print("收费13元")
elif 3 < d <= 15:
	print("收费", 13 + (d - 3) * 2.3, "元")
else:
	print("收费", 13 + 12 * 2.3 + (d - 15) * 3.45, "元")

a = int(input("请输入第1门成绩"))
b = int(input("请输入第2门成绩"))
c = int(input("请输入第3门成绩"))
max = a
if a < b:
	max = b if b > c else c
elif a < c:
	max = c if c > b else b
min = a
if a > b:
	min = b if b < c else c
elif a > c:
	min = c if c < b else b
ave = (a + b + c)/3
print("最高分、最低分、平均分，分别为", max, min, ave)

y = int(input("请输入年份："))
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
	print("为闰年")
else: print("不是闰年")

h = int(input("请输入您的身高"))
w = int(input("请输入您的体重"))
BMI = w/h**2
print("您的BMI为", BMI)
if BMI < 18.5:
	print("过轻")
elif 18.5 <= BMI <= 24:
	print("正常")
else:
	print("超重")
