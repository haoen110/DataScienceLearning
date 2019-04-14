# 练习 ：
#   1. 写一个函数 mysum(), 可以传入两个实参或三个实参.
#      1) 如果传入两个实参，则返回两个实参的和
#      2) 如果传入三个实参，则返回前两个实参的和对第三个实参求余的结果

#     print(mysum(1, 100))    # 101
#     print(mysum(2, 10, 7))  # 5 返回:(2+10) % 5

# 方法1
# def mysum(x, y, z=0):
#     if z == 0:
#         return x + y
#     return (x + y) % z

# 方法2
def mysum(x, y, z=None):
    if z is None:
        return x + y
    return (x + y) % z

print(mysum(1, 100))    # 101
print(mysum(2, 10, 7))  # 5 返回:(2+10) % 5
