# 14_built_house.py

# 此示例以建房子为例说明在什么情况下使用异常处理机制
def f1():
    print("开始建给房子打地基")
    # return ValueError("地下出现文物")
    print('地基建完')
    return 0

def f2():
    print('开始建地面以上部分')
    return ValueError("地上要修高压线")
    print('高楼建完')
    return 0


def f3():
    r = f1()
    if r != 0:
        return r
    r = f2()
    if r != 0:
        return r

def built_house():
    r = f3()
    if r != 0:
        return r

r = built_house()  # 开始建房子
if r == 0:
    print("房子建完了")
else:
    print("房子没建完", r)