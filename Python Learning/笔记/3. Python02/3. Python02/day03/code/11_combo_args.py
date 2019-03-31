

# 此程序示意函数的综合传参
def f1(a, b, *args, c, **kwargs):
    print(args)
    print(kwargs)

# f1(1, 2, 3, 4, d=6, c=5, e=7)

f1(*"hello", d=6, **{'c':5, 'e':7})

