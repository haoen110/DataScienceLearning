# 2. 编号列表如下:
#   Nos = [1001, 1002, 1003, 1004]
#   names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#   生成用Nos数据为键，以names为值的字典，如下:
#     {1001: 'Tom', 1002: 'Jerry', ......}


Nos = [1001, 1002, 1003, 1004]
names = ['Tom', 'Jerry', 'Spike', 'Tyke']

# 方法1
# d = { Nos[i]: names[i]
#      for i in range(min(len(Nos), len(names)))}

# 方法2:
d = { x: names[Nos.index(x)] for x in Nos}


print(d)

