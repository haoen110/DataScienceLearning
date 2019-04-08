# 04_function_args_give2.py


# 看懂下面的函数在做什么：
def fx(a, fn):
    return fn(a)

L = [5, 9, 4, 6]
print('最大值是:', fx(L, max))
print('最小值是:', fx(L, min))
print('和是:', fx(L, sum))

