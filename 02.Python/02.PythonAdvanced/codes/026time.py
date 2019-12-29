# 026time.py
import time
def clock():
	while True:
		cur_time = time.localtime() # 元组
		t_hms = cur_time[3:6] # 得到时分秒元组
		print("%02d:%02d:%02d" % t_hms, end='\r')
		time.sleep(1)
clock()