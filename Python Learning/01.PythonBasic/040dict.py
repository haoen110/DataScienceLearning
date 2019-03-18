# 040dict.py
L = ['xiaobai', 'xiaozhang', 'xiaowang']
d = {x:len(x) for x in L}
print(d)

Nos = [1001, 1002, 1003, 1004]
names = ['Tom', 'Jerry', 'Spike', 'Tyke']
d = { Nos[i]: names[i] for i in range(min(len(Nos), len(names)))}
print(d) 