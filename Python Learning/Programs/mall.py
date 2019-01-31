#mall.py

money = int(input("请输入商品总额"))
pay = money - 20 if money >= 100 else money
print("您需要支付", pay, "元")
