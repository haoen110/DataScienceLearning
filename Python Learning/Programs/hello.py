print("hello world!")
s = input("请输入字符串:")
print("您输入的字符串是:", s)
i = int(s)
if i % 2 == 0:
	print("您输入的是偶数")
else:
	print("您输入的是奇数")

s = input("请再输入字符串:")
j = int(s)
if j > 100:
	print("Bigger than 100")
elif 0 < j < 20:
	print("Between 0 and 20")
else:
	print("Other")

