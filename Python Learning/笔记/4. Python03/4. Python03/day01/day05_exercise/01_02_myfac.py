# 1. 编写函数求阶乘 myfac(x), 用什么方法都可以

def myfac(x):
    s = 1
    for i in range(2, x + 1):
        s *= i
    return s

# 2. 写程序算出1~20的阶乘的和
#   1!+2!+3!+.....+20!
print(sum(map(myfac, range(1, 21))))

