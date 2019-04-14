# 02_lambda.py

#   １．写一个lambda表达式，判断这个数的2次方+1是否能
#       被5整除,如果能整除返回True, 否则返回False

#   fx = lambda n: ....
#   print(fx(3)) # True
#   print(fx(4)) # False

# fx = lambda n: (n ** 2 + 1) % 5 == 0
fx = lambda n: True if (n ** 2 + 1) % 5 == 0 else False
print(fx(3)) # True
print(fx(4)) # False
