# 练习:
#   任意输入一些单词，存入集合中，当输入空字符串时结束输入，
#     1) 打印您输入的单词的种类数(去重)
#     2) 每个单词都打印到终端上显示
#       思考:
#         如何让打印的次序和输入的次序一致?

L = []
while True:
    s = input("请输单词: ")
    if not s:
        break
    L.append(s)

# s = set(L)  # 集合可以去重
# print("您共输入%d种单词" % len(s))
# for words in s:
#     print(words)

# 思考:
#   如何让打印的次序和输入的次序一致?

# 方法1,不用集合
# L2 = []
# for x in L:
#     if x not in L2:  # 如果x 没有加入到L2中，说明是第一次出现
#         L2.append(x)
# # 按次序打印
# for x in L2:
#     print(x)


# 方法2,用集合
s = set(L)  # 去重
for x in L:
    if x in s:  # 如果x在集合中，说明没有打印过
        print(x)
        s.discard(x)  # 删除已经过印过的


