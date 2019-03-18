# 018str.py
s1 = input("请输入第一行文字")
s2 = input("请输入第二行文字")
s3 = input("请输入第三行文字")
print("%20s" % s1)
print("%20s" % s2)
print("%20s" % s3)

print("以最长的字符串为长度进行右对齐显示")
m = len(s1)
if len(s2) > m:
	m = len(s2)
if len(s3) > m:
	m = len(s3)
# 或 m = max(len(s1),len(s2),len(s3))
fmt = "%%%ds" % m
print(fmt % s1)
print(fmt % s2)
print(fmt % s3)