# 练习:
#   编写程序用递归求阶乘:
#     def myfac(x):
#         ....

#     print(myfac(5))  # 120
#     print(myfac(4))  # 24


def myfac(x):
    if x == 1:
        return 1
    return x * myfac(x-1)

print(myfac(5))  # 120
print(myfac(4))  # 24


