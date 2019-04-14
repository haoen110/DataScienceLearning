# 03_def2.py

# 此示例示意定义带有参数的函数 及调用传参
def mymax(a, b):
    print('a =', a)
    print('b =', b)
    if a > b:
        print(a, "大于", b)
    else:
        print(a, "小于等于", b)

mymax(20, 30)
mymax(100, 50)
mymax("abc", '123')


