# 3. 完全数:
#   1 + 2 + 3 = 6 (6为完全数)
#   1, 2, 3 都为 6的因数(能被一个数x整数的数为y,则y为x的因数)
#   1 x 6 = 6
#   2 x 3 = 6
#   完全数是指除自身以外，所有的因数相加之和等于自身的数
#   求 4 ~ 5个完全数并打印
#   答案:
#     6
#     28
#     496
#     ....

# 方法1
# i = 1  # 完全数的开始值
# while True:
#     # 判断是否是完全数,如果是则打印 
#     L = []  # 每次循环开始都创建一个新列表，用来存因数
#     for x in range(1, i):
#         if i % x == 0:  # 如果x是i的因数
#             L.append(x)  # 放在列表中
#     # 此时L列表是中i所有的因数
#     if sum(L) == i:
#         print(i, "是完全数")

#     i += 1

# 方法2 用函数来求完全数，增加程序的可读性 

def is_perfect_number(i):
    L = []  # 每次循环开始都创建一个新列表，用来存因数
    for x in range(1, i):
        if i % x == 0:  # 如果x是i的因数
            L.append(x)  # 放在列表中
    # 此时L列表是中i所有的因数
    if sum(L) == i:
        return True
    return False


def main():
    # 此函数用来计算所有的完全数
    i = 1  # 完全数的开始值
    while True:
        # 判断是否是完全数,如果是则打印 
        if is_perfect_number(i):
            print(i, "是完全数")

        i += 1

main()