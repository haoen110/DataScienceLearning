# 02_class_variable.py


# 此示例示意Human类的实例可以访问count类变量
class Human:
    count = 0  # 创建一个类变量

print("Human的类变量count=", Human.count)  # 0
h1 = Human()
print("用h1对象访问Human的count变量", h1.count)  # 0
h1.count = 100
print(h1.count)  # 100
print(Human.count) # 0

h1.__class__.count += 1
print("h1.count=", h1.count)  # 100
print('Human.count=', Human.count)  # 1



