# 01_variable.py


a = 100
b = 200
def fx(c):
    d = 400
    print(a, b, c, d)

fx(300)
print('a =', a)
print('b =', b)
# print('c =', c)  # 出错，不能访问局部变量
# print('d =', d)

def fy(c):
    d = 40
    a = 10  # 此时会创建局部变量a，不会修改全局变量a
    print(a, b, c, d)

print("-------------------")
fy(30)
print('a =', a)
