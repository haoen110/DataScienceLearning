# 练习:
#   写一个函数 mymax, 实现返回两个数的最大值:
#      如:
#         def mymax(a, b):
#            ... 此处自己填写
#         print(mymax(100, 200))  # 200
#         print(mymax(50, 10))    # 50
#         print(mymax('ABC', 'ABCD')) # ABCD


# # 方法1
# def mymax(a, b):
#     if a > b:
#         s = a
#         # print(a)
#     else:
#         s = b
#         # print(b)
#     return s


# 方法2
# def mymax(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# 方法3
def mymax(a, b):
    if a > b:
        return a
    return b

print(mymax(100, 200))  # 200
print(mymax(50, 10))    # 50
print(mymax('ABC', 'ABCD')) # ABCD
