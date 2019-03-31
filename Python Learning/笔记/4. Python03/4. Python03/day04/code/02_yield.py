# 02_yield.py


# 此示例示意生成器函数的定义及使用
def myyield():
    '''此函数为生成器函数'''
    print("即将生成2")
    yield 2  # 生成2
    print('即将生成3')
    yield 3  # 生成3
    print('即将生成5')
    yield 5
    print("myield函数返回")

#　用 for语句访问　myyield函数
# for x in myyield():
#     print(x)

gen = myyield() # gen绑定生成器(生成器一定是可迭代对象)
it = iter(gen)  # it 绑定迭代器

print(next(it))  # 2
