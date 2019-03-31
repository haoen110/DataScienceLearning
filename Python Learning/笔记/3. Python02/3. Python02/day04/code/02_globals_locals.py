# 02_globals_locals.py

# 此示例示意 globals() 和locals()函数的用法
a = 1
b = 2
c = 3

def f1(c, d):
    e = 300
    print("locals()返回: ", locals())
    print("--------------------------")
    print('globals()返回', globals())
    for k, v in globals().items():
        print(k, '-->', v)
    print(c)  # 100
    print(globals()['c'])  # 得到了全局变量c的值　3


f1(100, 200)
