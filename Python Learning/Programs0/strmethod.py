#strmethod.py
#1、判断您输入的字符串有几个空格
s = input("请输入字符串")
print("您输入的字符串有", s.count(' '), '个空格')
#2、将原字符串的左右空白字符去掉，输出有效字符个数
s2 = s.strip()
print("有效字符个数是：", len(s2))
#3、判断输入的是否为数字
if s2.isdigit():
	print("您输入的是数字")
else:
	print("您输入的不是数字")
