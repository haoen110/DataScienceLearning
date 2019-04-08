# 03_while_embed.py

j = 1
while j <= 10:
    i = 1
    while i <= 20:
        print(i, end=' ')
        i += 1
    else:
        print()  # 为了换行

    j += 1  # 控制外重循环的次数

    