# 11_nonlocal.py

# 1. nonlocal语句只能在被嵌套函数内部进行使用
def f1():
    # nonlocal x  # 这是错的，因为没有外部嵌套函数
    x = 100
f1() 

# 3. 当有两层或两层以上的函数嵌套时，访问nonlocal变
# 　　　量只对最近一层的变量进行操作

def f1():
    v = 100
    def f2():
        v = 200
        def f3():
            nonlocal v  # 只对f2里的v进行操作
            v += 1
        f3()
        print("f2最后的v=", v)
    f2()
    print('f1最后的v=', v)

f1()

# 4. nonlocal语句的变量列表里的变量名，不能出现在此函
#    数的参数列表中

def f1():
    v = 100
    def f2(v):
        # nonlocal v  # 出错，v已在形参列表中...
        v += 1
    f2(20)
f1()
