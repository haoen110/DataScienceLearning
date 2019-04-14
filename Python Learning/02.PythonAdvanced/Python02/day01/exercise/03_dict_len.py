# 练习:
#  1. 有字符串列表如下:
#     L = ['tarena', 'xiaozhang', 'xiaowang']
#   生成如下字典:
#     d = {'tarena': 6, 'xiaozhang': 9, 'xiaowang': 8}
#   注: 字典的值是键的长度

L = ['tarena', 'xiaozhang', 'xiaowang']
d = {x : len(x) for x in L}
print(d)