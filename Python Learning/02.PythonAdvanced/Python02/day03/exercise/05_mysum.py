# 练习:
#   写一个函数，mysum , 可以传入任意个实参的数字，返回所有实参的和
#     def mysum(.....):
#         ......
#     print(mysum(1, 2, 3, 4))  # 10
#     print(mysum(2,4,6))  # 12

# 方法1, 用系统内建的sum函数函数求和:
# def mysum(*args):
#     return sum(args)

# 方法2, 用自己的算法来求和
def mysum(*args):
    s = 0
    for x in args:
        s += x
    return s


print(mysum(1, 2, 3, 4))  # 10
print(mysum(2,4,6))  # 12

