# 01_input.py

# 此示例示意input函数的用法

s = input("请输入字符串: ")
print("您输入的字符串是:", s)

# print(s + 1)  # 报错,字符串不能直接和数字相加
i = int(s)  # 将字符串转换为数字
print(i + 1)  # 数字可以和数字相加
