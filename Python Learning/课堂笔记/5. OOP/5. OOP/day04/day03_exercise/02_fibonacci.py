# 练习2:
#    写一个类,Fibonacci 实现迭代器协议,此类的对象可以作为可迭代对象生成相应的斐波那契数
#      1 1 2 3 5 8 ....

#     class Fibonacci:
#         def __init__(self, n):
#            ...

#     实现如下操作:
#     for x in Fibonacci(10):
#         print(x)
#     L = [ x for x in Fibonacci(30)]
#     print(sum(Fibonacci(25)))
#       (需要实现迭代器协议)

# 方法2
class Fibonacci:
    def __init__(self, n):
        self.__count = n

    def __iter__(self):
        self.cur_count = 0
        self.a = 0  # 用来保存前第二个数
        self.b = 1  # 用来保存前一个数
        return self


    def __next__(self):
        if self.cur_count >= self.__count:
            raise StopIteration
        self.cur_count += 1  # 生成数加1
        self.a, self.b = self.b, self.a + self.b
        return self.a

for x in Fibonacci(10):
    print(x)

L = [x for x in Fibonacci(30)]
print(L)
print(sum(Fibonacci(25)))
