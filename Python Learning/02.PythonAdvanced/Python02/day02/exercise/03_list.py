# 练习:
#   1. 模拟一个点名系统，已知全班学生名单，随机打印学生
#     的姓名进行点名，并得到此学生是否已到信息，
#     输入'y'代表已到，其它输入代表未到场
#     点名结束后打印未到者名单

names = ['tom', 'jerry', 'spike', 'tyke']

s = set(names)
L = []  # 代表未到的人的列表
for n in s:
    info = n + " 已到?(y):"
    r = input(info)
    if r != 'y':
        L.append(n)  # 把未到人的姓名加入到L列表中

print("未到人的名单如下:")
for n in L:
    print(n, end=' ')
print()





