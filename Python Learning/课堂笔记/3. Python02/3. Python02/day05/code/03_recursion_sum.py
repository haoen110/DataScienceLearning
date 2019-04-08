# 03_recursion_sum.py


# 求和 1 + 2 + 3 + ..... + 98 + 99 +100 的和

def mysum(x):
    if x <= 1:  # 设置递归的终止点
        return 1
    return x + mysum(x-1)


v = mysum(100)
print(v)
