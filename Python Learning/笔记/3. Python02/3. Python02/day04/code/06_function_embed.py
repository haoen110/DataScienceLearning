def fn_outer():
    print("fn_outer被调用!")

    def fn_inner():
        print("fn_inner被调用")

    fn_inner()
    fn_inner()
    print('fn_outter调用结束')
    return fn_inner


fn_outer()
# fn_inner() # 此处会出错
print('============================')
fx = fn_outer()
fx()  # 调用fn_outer内部创建的函数

