

# 此示例示意为属性和方法结合在一起使用
class Dog:
    def eat(self, food):
        print(self.color, '的',
              self.kinds, '正在吃', food)


# 创建第一个对象
dog1 = Dog()
dog1.kinds = '京巴'  # 添加属性kinds
dog1.color = '白色'  # 添加属性color
# print(dog1.color, '的', dog1.kinds)  # 访问属性
dog1.eat("骨头")

dog2 = Dog()
dog2.kinds = '牧羊犬'
dog2.color = '灰色'
# print(dog2.color, '的', dog2.kinds)  # 访问属性
dog2.eat('包子')
