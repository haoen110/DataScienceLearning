# 1. 写一个函数mysum(n),要求给出一个数n,求 
#    1 + 2 +3 + 4 + ..... + n 的和
#   如:
#     print(mysum(100))  # 5050
#     print(mysum(10))  # 55

def mysum(n):
    # s = 0
    # for x in range(1, n + 1):
    #     s += x
    # return s
    return sum(range(1, n + 1))

print(mysum(100))  # 5050
print(mysum(10))  # 55
