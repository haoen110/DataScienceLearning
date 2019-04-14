# 练习：
#   编写程序，用while语句解决下面的问题
#   问题:
#     输入一个数用n绑定,打印出n行的"hello world!"

n = int(input("请输入一个数: "))

# 方法1
# i = 1
# while i <= n:
#     print("hello world!")
#     i += 1
# else:
#     print("条件不满足，循环退出")

# 方法2, 直接用变量n来控制循环次数
while 1 <= n:
    print("hello world!")
    n -= 1

print("程序结束!")

