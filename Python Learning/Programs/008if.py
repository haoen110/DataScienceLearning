# 008if.py
s = int(input("请输入1~4个季度"))
if s == 1:
	print("第一季度有1、2、3个月")
elif s == 2:
	print("第二季度有4、5、6个月")
elif s == 3:
	print("第三季度有7、8、9个月")
elif s == 4:
	print("第四季度有10、11、12个月")
else:
	print("您输入的季度不合法")

m = int(input("请输入1~12月份"))
if 1 <= m <= 3:
	print("第一季度")
elif 4 <= m <= 6:
	print("第二季度")
elif 7 <= m <= 9:
	print("第三季度")
elif 10 <= n <= 12:
	print("第四季度")
else:
	print("您输入的月份不合法")