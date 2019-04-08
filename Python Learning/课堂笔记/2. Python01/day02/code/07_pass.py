# 07_pass.py


# 此程序示意pass语句的用法

# 判断一个学生是否不合法。如果不合法给出警告信息，
# 如果合法什么都不做

score = int(input("请输入成绩: "))
if 0 <= score <= 100:
    pass  # 此语句就是为了填充语法空白
else:
    print("您的输入有误!!!")

print("程序结束")
