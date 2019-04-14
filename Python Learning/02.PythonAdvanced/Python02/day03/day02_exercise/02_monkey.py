# 2 猴子吃桃
#   有一只小猴子，摘了很多桃
#     第1天吃了全部桃子的一半，感觉不饱又吃了一个
#     第2天吃了剩下的一半，感觉不饱又吃了一个
#     ... 以此类推
#     到第10天，发现只剩一个了
#   请问第一天摘了多少桃?

def get_lastday(y):
    # 根据今天的桃子数y，计算昨天的桃子数x
    x = (y + 1) * 2
    return x

p = 1  # 第十天的桃子数
day = 10  # 用来表示当前是第几天
while day >1:
    day -= 1
    p = get_lastday(p)
    print("第", day, "天的桃子数是:", p)

    


# day9 = get_lastday(1)
# day8 = get_lastday(day9)