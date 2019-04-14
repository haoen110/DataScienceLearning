# 01_class_variable.py


# 此示例示意类变量的定义和使用
class Human:
    count = 0  # 创建一个类变量

print("Human的类变量count=", Human.count)  # 0
Human.count = 100
print(Human.count)  # 100


