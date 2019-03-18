# 005print.py
a = 20 * 365
week = a // 7
day = a % 7
print("他过了", week, "星期", day, "天")

h = int(input("请输入小时"))
m = int(input("请输入分钟"))
s = int(input("请输入小时秒数"))
print("距离凌晨已经过去了", h * 3600 + m * 60 + s)