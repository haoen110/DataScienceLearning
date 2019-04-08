# 03_attribute.py


# 此示例示意为对象添加属性
class Dog:
    pass

# 创建第一个对象
dog1 = Dog()
dog1.kinds = '京巴'  # 添加属性kinds
dog1.color = '白色'  # 添加属性color
dog1.color = '黃色'  # 改变属性的绑定关系

print(dog1.color, '的', dog1.kinds)  # 访问属性

dog2 = Dog()
dog2.kinds = '牧羊犬'
dog2.color = '灰色'
print(dog2.color, '的', dog2.kinds)  # 访问属性



