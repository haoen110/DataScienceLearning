# 04_while_continue.py

# 本示例示意用while循环，实现打印10以内的偶数

i = 0
while i < 10:
    if i % 2 == 1:
        i += 1
        continue
    print(i)
    i += 1
