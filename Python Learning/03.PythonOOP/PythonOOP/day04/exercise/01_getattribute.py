# 写一个Car类,属性有:
#    颜色 color
#    品牌 brand
# class Car:
#     def __init__(self, c, b):
#         ...
#     # 添加一个方法
#     def get_car_attr(self, attr_name):
#         '''此方法用于获取对象的属性,如果属性名attr_name在此对象内不存在则返回 None
#         '''
#   示例:
#     c1 = Car('黑色', 'Benz')
#     v = c1.get_car_attr('color')
#     if v is None:
#         print("没有颜色属性")
#     else:
#         print("颜色是:", v)


class Car:
    def __init__(self, c, b):
        self.color, self.brand = c, b

    def get_car_attr(self, attr_name):
        '''此方法用于获取对象的属性,如果属性名attr_name
        在此对象内不存在则返回 None
        '''
        return getattr(self, attr_name, None)


c1 = Car('黑色', 'Benz')
v = c1.get_car_attr('color')
# try:
#     v = c1.__dict__['aaaaa']
# except KeyError:
#     v = None
if v is None:
    print("没有颜色属性")
else:
    print("颜色是:", v)
