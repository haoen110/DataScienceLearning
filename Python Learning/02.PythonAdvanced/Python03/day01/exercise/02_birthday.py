# 练习：
#   写一个程序，输入你的出生日期
#     1) 算出你已经出生了多少天?
#     2) 算出你出生那天是星期几?

import time
# 写一个程序，输入你的出生日期
year = int(input("请输入年: "))
month = int(input("请输入月: "))
day = int(input("请输入日: "))

# 得到出生时的秒数
birthday_second = time.mktime((year,
                               month,
                               day,
                               0, 0, 0, 0, 0, 0))
# 得到当前时间的秒数
cur_second = time.time()

# 1) 算出你已经出生了多少天?
s = cur_second - birthday_second  # 计算时间差(秒数)
print("您已出生:", s / 60 / 60 // 24)

# 2) 算出你出生那天是星期几?
# 得到出生时的时间元组
birday = (year, month, day, 0, 0, 0, 0, 0, 0)
# 转为秒数
s = time.mktime(birday)
# 转回到时间本地元组
t = time.localtime(s)
weekday = {
        0: "星期一",
        1: "星期二",
        2: "星期三",
        3: "星期四",
        4: "星期五",
        5: "星期六",
        6: "星期日"
    }
print("您出生那天是:", weekday[t[6]])

