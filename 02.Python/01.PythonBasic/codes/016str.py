# 016str.py
s = int(input("请输入字数，为距离左侧的距离"))
print(" " * s + "   *   ")
print(" " * s + "  ***  ")
print(" " * s + " ***** ")
print(" " * s + "*******")

s1 = input("请输入第一行文字")
s2 = input("请输入第二行文字")
s3 = input("请输入第三行文字")

m = len(s1)
if len(s2) > m:
	m = len(s2)
if len(s3) > m:
	m = len(s3)

line1 = "+" + m * '-' + "+"
line2 = "|" + round((m-len(s1))/2) * " " + s1 + round((m-len(s1))/2) * " "+"|"
line3 = "|" + round((m-len(s2))/2) * " " + s2 + round((m-len(s2))/2) * " "+"|"
line4 = "|" + round((m-len(s3))/2) * " " + s3 + round((m-len(s3))/2) * " "+"|"
print(line1)
print(line2)
print(line3)
print(line4)
print(line1)

