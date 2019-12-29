# 030continue.py
begin = int(input("请输入开始"))
end = int(input("请输入结束"))
for i in range(begin, end + 1):
	if i % 2 != 0:
		continue
	else:
		print(i, end=' ')
print()

i = 0
while i <= 10:
	if i % 2 != 0:
		i += 1
		continue
	print(i, end=' ')
	i += 1

