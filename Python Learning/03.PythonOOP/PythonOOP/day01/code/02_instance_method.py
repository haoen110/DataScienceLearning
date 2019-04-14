# 02_instance_method.py


# 此实例示意如何用实例方法(method)来描述Dog类的行为
class Dog:
    def eat(self, food):
        '''此方法用来描述小狗吃东西的行为'''
        print("小狗正在吃:", food)

    def sleep(self, hour):
        print("小狗睡了", hour, "小时")

    def play(self, obj):
        print("小狗正在玩", obj)

# 创建一个Dog的类的实例:
dog1 = Dog()
dog1.eat('狗粮')
dog1.sleep(1)
dog1.play("球")  # 对象不能调用类内不存在的实例方法


# 创建另一个Dog对象
dog2 = Dog()
dog2.play("飞盘")
dog2.eat("骨头")
dog2.sleep(2)
# dog2.play('杂技')  # 此调用方法可以用如下方法代替
Dog.play(dog2, '杂技')

