# 09_global.py


# 3. 不能先声明局部的变量，再用global声明为全局
# 变量，此做法不附合规则
def f1():
    # x = 100  # 此处会出现语法警告
    global x
    x = 100

f1()
print(x)


# 4. global 变量列表里的变量不能出现在此作用域内的
# 形参列表里
v = 100
def f2(v):
    # global v  # 此处必然会出错
    v = 300

f2(200)
print(v)
