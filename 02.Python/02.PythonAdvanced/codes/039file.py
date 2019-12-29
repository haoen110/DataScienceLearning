# 039file.py
f = open('039file_write.txt', 'w')
L = ['我是第一行\n', '我是第二行\n']
f.writelines(L)
f.close