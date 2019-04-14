# 练习：
# 　　写一个生成器函数myodd(x) 来生成一系列奇数
#   如:
#     myodd(10) 可以生成 1 3 5 7 9

def myodd(x):
    i = 0
    while i < x:
        if i % 2 == 1:
            yield i
        i += 1

for x in myodd(10):
    print(x)

print("------------------------")
# 问题:
# 以下两种方法的共同点和区别
# １．
for y in myodd(300000):
    print(y)

# 2.
for y in list(myodd(30000)):
    print(y)


