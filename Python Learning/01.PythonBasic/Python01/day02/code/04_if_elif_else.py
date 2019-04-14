# 04_if_elif_else.py

# 输入一个数字，判断这个数是0,还是正数，还是负数 

n = int(input("请输入一个数: "))

if n == 0:
    print("您输入的是0")
elif n > 0:
    print("您输入的是正数") 
else:
    print("您输入的是负数")