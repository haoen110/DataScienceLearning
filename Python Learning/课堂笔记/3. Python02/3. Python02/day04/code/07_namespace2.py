# 07_namespace.py


# 此示例说明python的作用域
v = 100  # 全局作用域

def fun1():
    v = 200  # 外部嵌套函数的作用域
    print('fun1内的v=', v)
    def fun2():
        v = 300  # 局部作用域
        print("fun2内的v=", v)
    fun2()

fun1()

print("v =", v)

