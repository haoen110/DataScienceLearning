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
m = len(a)
if len(b) > m:
    m = len(b)
if len(c) > m:
    m = len(c)
# m为最长的字符串的长度
# print(m)

line1 = '+' + '-' * (m + 2) + '+'
print(line1)
# 打印第一行文字
left = (m - len(a)) // 2  # 计算第1行左侧空格
right = m - len(a) - left  # 计算右侧空格个数
line = '| ' + ' ' * left + a + ' ' * right + ' |'
print(line)

# 打印第二行文字
left = (m - len(b)) // 2  # 计算第1行左侧空格
right = m - len(b) - left  # 计算右侧空格个数
line = '| ' + ' ' * left + b + ' ' * right + ' |'
print(line)

# 打印第三行文字
left = (m - len(c)) // 2  # 计算第1行左侧空格
right = m - len(c) - left  # 计算右侧空格个数
line = '| ' + ' ' * left + c + ' ' * right + ' |'
print(line)

# 打印最后一行
print(line1)