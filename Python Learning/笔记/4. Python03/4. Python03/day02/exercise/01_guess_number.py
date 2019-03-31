# 练习：
#   猜数字游戏:
#     写程序，随机生成一个0~100之间的数用变量x绑定
#     循环让用户输入一个数用y绑定,
#        输出猜数字的结果
#          1. 如果y等于生成的数x,则提示"您猜对了", 打印出猜测的次数并退出
#          2. 如果y 小于x则提示"您猜小了"，然后继续猜
#          3. 如果y 大于x则提示"您猜大了"，然后继续猜
#     猜对后程序退出并打印次数

import random

x = random.randrange(101)  # 生成[0,100]
# print(x)
times = 0
while True:
    y = int(input("请输入: "))
    times += 1
    if x == y:
        print("您猜对了！")
        break
    elif y < x:
        print("您猜小了！")
    elif y > x:
        print("您猜大了!")

print("您共猜了%d次" % times)
