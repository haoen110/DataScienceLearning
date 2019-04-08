# 练习 ：
#   1. 输入一个正方形的周长，输出正方形的面积
#   2. 输入一个圆的半径，打印出这个圆的面积
#   3. 输入一个正方型的面积，打印这个正方型的周长
#   ( 要求: 用math模块内的函数和数据)

# 导入math模块
import math as m

# 1. 输入一个正方形的周长，输出正方形的面积
length = float(input("请输入正方形的周长："))
area = m.pow(length / 4, 2)
print('此正方形的面积是:', area)

# 2. 输入一个圆的半径，打印出这个圆的面积
r = float(input("请输入一个圆的半径:"))
area = m.pow(r, 2)*m.pi
print('此圆的面积是:', area)

# 3. 输入一个正方型的面积，打印这个正方型的周长
area = float(input("请输入一个正方型的面积:"))
length = m.sqrt(area) * 4
print("此正方形的周长是:", length)
