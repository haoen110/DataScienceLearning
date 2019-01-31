#str_format.py

fmt = "姓名:%s, 年龄:%d"
name = input("请输入姓名：")
age = int(input("请输入年龄："))
s = fmt % (name, age)
print(s)

# 输入三行文字，让这些文字依次以20的宽度向右对齐输出
#方法一
a = input("请输入第一行文字：")
b = input("请输入第二行文字：")
c = input("请输入第三行文字：")
print('%20s'%a,'\n%20s'%b,'\n%20s'%c)
#以最长字符串左对齐
m = max(len(a), len(b), len(c))
print("最大长度是：", m)
print(' ' * (m - len(a)) + a)
print(' ' * (m - len(b)) + b)
print(' ' * (m - len(c)) + c)
#方法三
fmt = '%%%ds' % m #生成一个含有占位符的字符串
print('\nfmt=', fmt)
print(fmt % a)
print(fmt % b)
print(fmt % c)


