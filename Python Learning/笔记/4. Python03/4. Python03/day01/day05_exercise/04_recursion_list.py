# 4. 已知有列表:
#   L = [[3,5,8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数print_list(lst) 打印出所有元素
#       print_list(L)  # 打印 ....
#     2) 写一个函数 sum_list(lst) 返回这个列表中所有元素的和
#  注:
#    type(x) 可以返回一个变量的类型
#    如:
#        type(20) is int        # 返回True
#        type([1,2,3]) is list  # 返回True



# 1) 写一个函数print_list(lst) 打印出所有元素
def print_list(lst):
    for x in lst:  # x可能绑定列表，也可能绑定整数
        if type(x) is list:
            print_list(x)
        else:
            print(x)


# 2) 写一个函数 sum_list(lst) 返回这个列表中所有元素的和
def sum_list(lst):
    s = 0
    # 在此处累加所有元素，包括列表
    for x in lst:
        if type(x) is list:
            s += sum_list(x)
        else:
            s += x
    return s


L = [[3,5,8], 10, [[13, 14], 15, 18], 20]
print_list(L)  # 打印 ....
print('和是:', sum_list(L))
