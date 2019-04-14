

# 此示例示意闭包的创建和调用过程

def make_power(y):
    def fx(arg):
        return arg ** y
    return fx

pow2 = make_power(2)
print('3的平方是: ', pow2(3))
pow3 = make_power(3)
print('3的立方是: ', pow3(3))
