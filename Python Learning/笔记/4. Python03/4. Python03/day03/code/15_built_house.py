# 14_built_house.py

# 此示例以建房子为例说明在什么情况下使用异常处理机制
def f1():
    print("开始建给房子打地基")
    # raise ValueError("地下出现文物")
    print('地基建完')

def f2():
    print('开始建地面以上部分')
    raise ValueError("地上要修高压线")
    print('高楼建完')


def f3():
    f1()
    f2()

def built_house():
    f3()

try:
    built_house()  # 开始建房子
except ValueError as err:
    print("房子没建完", err)
else:
    print("房子建完了")

# r = built_house()  # 开始建房子
# if r == 0:
#     print("房子建完了")
# else:
#     print("房子没建完", r)