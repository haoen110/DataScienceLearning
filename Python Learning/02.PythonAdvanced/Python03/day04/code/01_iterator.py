# 01_iterator.py


# 此示例示意用迭代器来访问可迭代对象

# 用for 语句访问可迭代对象L
L = [2, 3, 5, 7]
for x in L:
    print(x)

print('--------以下是while语句访问L--------')
# 用while循环语句来访问如下列表
it = iter(L)  # 用L来生成一个迭代器
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print("迭代终止,迭代器不能提供任何数据")
        break


