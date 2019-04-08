
# 此示例示意
# break语句只能终止当前循环语句的执行，
# 如果有循环嵌套时，不会跳出嵌套的外重循环

j = 1
while j <= 10:
    i = 1
    while i <= 20:
        print(i, end=' ')
        if i == 5:
            break
        i += 1
    print()  # 为了换行

    # if j == 5:
    #     break
    j += 1  # 控制外重循环的次数

