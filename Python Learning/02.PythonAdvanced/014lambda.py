# 014lambda.py
fx = lambda n: (n**2+1)%5 == 0
print(fx(3))
print(fx(4))

mymax = lambda x, y: x if x > y else y
print(mymax(100, 200))