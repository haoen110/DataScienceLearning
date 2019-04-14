# 01_clock.py

# 1. 写一个程序，以电子时钟格式打印时间:
#     时间格式为:
#         HH:MM:SS
#     时间每隔一秒刷新一次

import time

def clock():
    while True:
        # 在此处先获取当前时间
        cur_time = time.localtime()  # 元组
        t_hms = cur_time[3:6]  # 得到时分秒元组
        # hour, minute, second = t_hms
        # 打印时间
        print("%02d:%02d:%02d" % t_hms, end='\r')
        time.sleep(1)



clock()

