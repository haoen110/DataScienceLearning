# 2. 输一个学生的三科成绩：
#    1. 打印出最高分是多少分
#    2. 打印出最低分是多少分
#    3. 打印出平均分是多少分

s1 = int(input("请输入第1科成绩: "))
s2 = int(input("请输入第2科成绩: "))
s3 = int(input("请输入第3科成绩: "))

# 方法1
# if s1 > s2:  # s1大
#     if s1 > s3:
#         print("最高成绩是:", s1)
#     else:
#         print("最高成绩是:", s3)
# else:  # s2大
#     if s2 > s3:
#         print("最高成绩是:", s2)
#     else:
#         print("最高成绩是:", s3)

# 方法2
if s2 <= s1 >= s3:
    print("最高成绩是:", s1)
elif s1 <= s2 >= s3:
    print("最高成绩是:", s2)
else:
    print("最高成绩是:", s3)

# 经典方法
m = s1
if s2 > m:
    m = s2
if s3 > m:
    m = s3
print("最高成绩是:", m)

