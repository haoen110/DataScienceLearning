# 08_or.py


# 此示例示意 or 的用法

# 如果直接输入回车键则score为'0'
score = input("请输入成绩: ") or '0'
score = int(score)

if score < 0 or score > 100:  # 判断成绩不合法
    print("您的成绩不合法!!!")
else:
    print("您输入的成绩是:", score)
