# 10_nonlocal.py


# 此示例示意nonlocal语句的用法:

var = 100
def f1():
    var = 200
    print("f1里的var=", var)

    def f2():
        nonlocal var
        var = 300  # 此处要想修改f1里的var变量怎么办？
        print("f2里的var=", var)
    f2()

    print("f2调用结束后f1里的var值为", var)

f1()
print('全局的var =', var)

