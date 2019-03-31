
class Dog:
    pass

dog1 = Dog()
# print(dog1.color)  # 会出错,没有这个属性
print(getattr(dog1, 'color', '没有颜色'))  # 没有颜色
dog1.color = '白色'
print(getattr(dog1, 'color', '没有颜色'))  # 白色

print(getattr(dog1, 'kinds', None))