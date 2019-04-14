# 03_function_args_give.py


# 此示例示意函数作为参数传入另一个函数
def f1():
    print("hello")
def f2():
    print('world')

def fx(fn):
    print(fn)
    fn()  # 调用谁?
fx(f1)  # 此语句在做什么？
fx(f2)