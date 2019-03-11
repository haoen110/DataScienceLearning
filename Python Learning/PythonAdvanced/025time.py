# 025time.py
import time
year = int(input("请输入年"))
month = int(input("请输入月"))
day = int(input("请输入日"))

birthday = (year, month, day, 0, 0, 0, 0, 0, 0)
s = time.mktime(birthday) 
t = time.localtime(s)
weekday = {
	0:"星期一",
	1:"星期二",
	2:"星期三",
	3:"星期四",
	4:"星期五",
	5:"星期六",
	6:"星期日"
}

print("您出生的那天是：", weekday[t[6]])