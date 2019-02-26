#huiwen.py
s = input("请输入一串文字判断是否为回文：")
if s == s[::-1]:
	print("是回文")
else:print("不是")