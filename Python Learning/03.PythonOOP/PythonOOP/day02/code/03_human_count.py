# 03_car_count.py


# 此示例示意用类变量来记录对象的个数
class Car:
    count = 0  # 创建类变量, 用来记录汽车对象的总数
    def __init__(self, info):
        print(info, "被创建")
        self.data = info  # 记录传入数据
        self.__class__.count += 1  # 让车的总数加1

    def __del__(self):
        print(self.data, '被销毁')
        # 当车被销毁时总数自动减1
        self.__class__.count -= 1  

print('当前汽车总数是:', Car.count)
b1 = Car("BYD 京A.88888")
print(Car.count)
b2 = Car('TESLA 京B.00000')
b3 = Car('Audi, 京C.66666')
print('当前汽车总数是:', Car.count)
del b1
del b2
print("当前汽车数是:", Car.count)


    