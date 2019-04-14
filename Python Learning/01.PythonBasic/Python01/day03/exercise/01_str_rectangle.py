# 01_str_rectangle.py

# 写一个程序，打印一个高度为4的矩形方框
# 要求输入一个整数，此整数代表矩形的宽度，输出此矩形
# 如:
#  请输入宽度: 10
#  打印如下:
#  ##########
#  #        #
#  #        #
#  ##########

w = int(input("请输入宽度: "))

line1 = '#' * w
line2 = '#' + ' ' * (w - 2) + '#'
print(line1)
print(line2)
print(line2)
print(line1)