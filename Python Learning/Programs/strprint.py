#strprint.py
n = int(input("请输入距离左侧的字节数："))
n = n * '	'
print(n,"   *   ")
print(n,"  ***  ")
print(n," ***** ")
print(n,"*******")

a = input("请输入第一行文字：")
b = input("请输入第二行文字：")
c = input("请输入第三行文字：")
m = max(len(a), len(b), len(c))
line0 = '+' + '-' * m + '+'
line1 = '|' + a.center(m) + '|'
line2 = '|' + b.center(m) + '|'
line3 = '|' + c.center(m) + '|'
print(line0)
print(line1)
print(line2)
print(line3)
print(line0)

