# 练习:
#   写程序，输入一段字符串，打印出这个字符串中出现过的字符及出现过的次数:
#     如:
#       输入: ABCDABCABA
#     输出:
#       A : 4次
#       C : 2次
#       B : 3次
#       D : 1次
#     注: 不要求打印的顺序

s = input("输入: ")
# 方法1
# d = {}  # 字典的键是出现的字符，字典的值是出现的次数
# for ch in s:  # 把我有字符都取出一遍
#     if ch not in d:
#         # 如果是第一次出现,则把ch作为键，把1作为值加入字典中
#         d[ch] = 1
#     else:
#         # 如果已经出现过,则把ch键所对应的值做 +1 操作
#         d[ch] += 1
# 
# for k in d:
#     print(k, ":", d[k], '次')

# 方法2:
d = {}
for ch in s:
    if ch not in d:  # 把将一次出现的字符加入字典中
        d[ch] = None

for ch in d:
    print(ch, ":", s.count(ch), "次")

