# 04_break.py

i = 1
while i <= 6:
    print("本次循环开始时:", i)
    if i == 3:
        break  # break将打破包含它的while语句
    print("本次循环结束时:", i)
    i += 1
else:
    print("我是while 里的else子句")


print("这是程序最后一条语句, i=", i)

