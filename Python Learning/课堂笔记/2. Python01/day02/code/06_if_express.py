# 06_if_express.py


# 此示例示意条件表达式的用法
# 商场促销，过100 返 20
money = int(input("请输入商品总额: "))

pay = money - 20 if money > 100 else money

print("您需要支付", pay, "元")

