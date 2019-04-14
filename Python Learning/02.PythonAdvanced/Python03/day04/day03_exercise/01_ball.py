# 1. 一个球100米高空落下,每次落下后反弹高度是原高度的一半,再落下,
# 写程序
#   1) 算出皮球在第10次落地后反弹高度是多少,
#   2) 打印出球共经过了多少米的路程

def ball(height, times):
    """根据给定的原始高度，和次数，返回最终反弹的高度"""
    for _ in range(times):
        height = height / 2  # height /= 2
    return height

def ball_distance(height, times):
    s = 0  # 用来累加所有路程
    for _ in range(times):
        s += height  # 把下落过程累加到s
        height /= 2
        s += height  # 把返弹高度累到加s
    return s

print("球从100高度返弹10次后的高度是:", ball(100, 10))
print("球从100米高度反弹10次后的经历的路程是",
       ball_distance(100, 10))

