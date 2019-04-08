# 练习:
#   写一个程序，输入多行文字，当输入空行时结束输入
#   将原输入的所有字符串存于列表L中
#   1. 按原来输入的行的顺序反向打印这些行
#      列:
#        输入:hello world
#        输入:welcome to china
#        输入:I like python
#        输入: <回车>
#      显示
#        I like python
#        welcome to china
#        hello world
#   2. 打印出您共输入了多少文字符?

L = []  # 用来存放每一行字符串
while True:
    s = input("输入: ")
    if not s:  # s为空则跳出循环
        break
    L.append(s)  # 追加到L中

print(L)

s = 0  # 用来记录字符个数
# 方法1,
# i = len(L) -1  # 得到最后一个行的索引
# while i >= 0:
#     print(L[i])
#     s += len(L[i])
#     i -= 1

# 方法2, 用for循环
L.reverse()  # 先反转
for line in L:
    print(line)
    s += len(line)

print("字符的个数是:", s)
