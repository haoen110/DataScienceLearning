# 05_if_embed.py

# 根据输入的月份来判断是哪儿个季度
month = int(input("请输入月份(1~12): "))

if 1 <= month <= 12:
    print("是合法的月份")
    if month <= 3:
        print("春季")
    elif month <= 6:
        print("夏季")
    elif month <= 9:
        print("秋季")
    else:
        print("冬季")
else:
    print("您的输入有误!")

