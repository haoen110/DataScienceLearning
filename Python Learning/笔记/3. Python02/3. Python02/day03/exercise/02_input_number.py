# 2. 写一个函数 input_number
#     def input_number():
#         ....
#     此函数用来获取用户循环输入的整数，当用户输入负数时结束输入
#     将用户输入数以列表的形式返回，再用内建函数max, min, sum 示出用户输入的最大值，最小值及和:
#     如:
#       L = input_number()
#       print(L)  # 打印此列表
#       print("用户输入的最大数是:", max(L))
#       print("用户输入的最小数是:", min(L))
#       print("用户输入的和是:", sum(L))


def input_number():
    L = []
    while True:
        n = int(input("请输入: "))
        if n < 0:
            return L  # 如果n为负数，把之前输入的值返回
        L.append(n)  # 如果n为大于等于0的数，则加入列表L


L = input_number()
print(L)  # 打印此列表
print("用户输入的最大数是:", max(L))
print("用户输入的最小数是:", min(L))
print("用户输入的和是:", sum(L))
