# 2. 输入三行文字，让这三行文字在一个方框居中显示
# 如输入(不要输入中文):
# hello tarena!
# my name is weimingze
# python
# 显示如下:
# +----------------------+
# |    hello tarena!     |
# | my name is weimingze |
# |        python        |
# +----------------------+

a = input("请输入第1个字符串: ")
b = input("请输入第2个字符串: ")
c = input("请输入第3个字符串: ")

# 计算最长的一个字符串的长度
m = max(len(a), len(b), len(c))

line1 = '+' + '-' * (m + 2) + '+'
print(line1)
# 打印第一行文字
print('| ' + a.center(m) + ' |')

# 打印第二行文字
print('| ' + b.center(m) + ' |')

# 打印第三行文字
print('| ' + c.center(m) + ' |')

# 打印最后一行
print(line1)