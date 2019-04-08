# 12_raise_get_age.py


# 此示例示意用raise发出错误通知给调用者
# 甲写了函数 get_age
def get_age():
    a = int(input("请输入年龄(0~140): "))
    if 0 <= a <= 140:
        return a
    if a > 140:
        raise OverflowError("人的年龄不可能大于140")


# 乙用户调用get_age()
try:
    age = get_age()
except ValueError as err:
    print("用户输入的不是数字.已做出相应的处理")
    age = 0
except OverflowError as err:
    print("用户输入的年龄过大")
    age = 0

print("得到的年龄是:", age)



