# 02_alarm.py

# 2. 编写一个闹钟程序，启动时设置定时时间，到时候
# 后打印出一句语，然后程序退出

import time

def alarm(hour, minute):
    '''hour 代表定时的小时
    minute 代表定时的分钟'''
    while True:
        cur_time = time.localtime()
        tuple_hm = cur_time[3:5]  # 得到(小时，分钟)元组
        print("%02d:%02d:%02d" % cur_time[3:6], end='\r')
        if (hour, minute) == tuple_hm:
            break

def main():
    h = int(input('请输入小时: '))
    m = int(input('请输入分钟: '))
    alarm(h, m)  # 用函数来计时，函数返回则时间到!
    print("时间到....")

main()