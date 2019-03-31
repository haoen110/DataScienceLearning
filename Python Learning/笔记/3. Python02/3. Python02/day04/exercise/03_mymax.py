# 2. 写一个lambda表达式，求两个变量的最大值:
#    def mymax(x, y):
#        ....
#    # 或用lambda
#    mymax = lambda ....
#    print(mymax(100, 200))  # 200


def mymax(x, y):
    print('mymax被调用')
    # if x > y:
    #     return x
    # return y
    # return max(x, y)
    return x if x > y else y

# mymax = lambda x, y: max(x, y)
mymax = lambda x, y: x if x > y else y

print(mymax(100, 200))  # 200

