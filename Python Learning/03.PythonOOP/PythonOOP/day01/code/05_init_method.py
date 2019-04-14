# 05_init_method.py


# 此示例示意 __init__方法的自动调用及添加实例变量
class Car:
    def __init__(self, c, b, m):
        # print("__init__方法被调用")
        self.color = c  # 颜色
        self.brand = b  # 品牌
        self.model = m  # 型号

    def run(self, speed):
        print(self.color, '的',
              self.brand, self.model,
              '正在以', speed, '公里/小时的速度行驶!')

    def set_color(self, clr):
        '''此方法用来修改车的颜色信息'''
        self.color = clr


a4 = Car('红色', '奥迪', 'A4')  # 创建了一辆车
a4.run(179)  # 上路跑
# a4.color = '黑色'
a4.set_color('黑色')
a4.run(300)  # 

t1 = Car('蓝色', 'TESLA', 'Modle S')
t1.run(299)


