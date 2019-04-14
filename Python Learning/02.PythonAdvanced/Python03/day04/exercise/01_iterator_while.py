# 练习：
# 　　有一个集合:
#     s = {'唐僧', '悟空', '八戒', '沙僧'}
# 　　用for 语句来打印集合内的信息:
#     for x in s:
#         print(x)
#     else:
#         print("遍历结束")
#   请将上面的for语句改写为while,next,iter函数组合方式实现上述功能

s = {'唐僧', '悟空', '八戒', '沙僧'}
# for x in s:
#     print(x)
# else:
#     print("遍历结束")

it = iter(s)  # 先获取迭代器
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print("遍历结束")
        break
