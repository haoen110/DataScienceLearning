# 09_flush.py

import time

f = open('infos.txt', 'w')
f.write('hello')
f.flush()  # 强制清空缓冲区

# for i in range(10000):
#     f.write('helloooooo')
#     time.sleep(0.01)

print("程序开始睡觉...zzz")
time.sleep(15)
print("程序睡醒了,继续执行")

f.close()