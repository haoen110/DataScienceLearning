# 027time.py
import time
cur_time = time.localtime() # 元组
t_hms = cur_time[3:6] # 得到时分秒元组
print("现在时间是：%02d:%02d:%02d" % t_hms)


def alarm(hour, minute, second):
	while True:
		cur_time = time.localtime() # 元组
		t_hms = cur_time[3:6] # 得到时分秒元
		print("%02d:%02d:%02d" % t_hms, end='\r')
		time.sleep(1)
		if (hour, minute, second) == t_hms:
			print()
			break

def main():
	h = int(input("请输入小时"))
	m = int(input("请输入分钟"))
	s = int(input("请输入秒钟"))
	alarm(h, m, s)
	print("时间到！！")

main()
	