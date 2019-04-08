# 3. 算出 100 ~ 999 以内的水仙花数(Narcissistic number)
#    水仙花数是指百位的3次方加上十位的3次方加上个位
#    的3次方等于原数的数字
#      例如:
#        153 等于 1**3 + 5**3 + 3**3
#    参考答案:
#      153, 370, ...

# 方法1
# for x in range(100, 1000):
#     bai = x // 100
#     shi = x %100 // 10
#     ge = x % 10
#     if x == bai ** 3 + shi ** 3 + ge ** 3:
#         print(x)

# 方法2
# for x in range(100, 1000):
#     s = str(x)  # 得到字符串
#     bai = int(s[0])  # 百位
#     shi = int(s[1])  # 十位
#     ge = int(s[2])  # 个位
#     if x == bai ** 3 + shi ** 3 + ge ** 3:
#         print(x)

# 方法3
for bai in range(1, 10):
    for shi in range(10):
        for ge in range(10):
            # print(bai, shi, ge)
            x = bai * 100 + shi * 10 + ge
            if x == bai ** 3 + shi ** 3 + ge ** 3:
                print(x)
