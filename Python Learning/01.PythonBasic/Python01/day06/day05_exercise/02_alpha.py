# 2. 用循环语句生成如下字符串
#   'ABC.....XYZ'
#   'AaBbCc......XxYyZz'
#   提示:
#      用ord和chr函数结合循环语句实现

s = ''  # 用来存入大写英文字母
s2 = ''  # 用来存放大写小写混合的英文字母
for i in range(65, 65 + 26):
    # print(chr(i))
    s += chr(i)
    s2 += chr(i)  # 先放一个大写的
    # 放入一个小写的字母
    s2 += chr(i + 32)
    # ord('a') - ord('A')  # 32

print(s)
print(s2)


