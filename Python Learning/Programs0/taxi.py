#taxi.py
# 3公里内收费13元
# 超过3公里单价2.3元/公里
# 超过15公里，每公里加收基本单价50%作为空驶费（3.45/公里）

k = int(input("请输入行驶的公里数："))
fee = 13
if k > 3:
	fee += 2.3 * (k - 3)
if k > 15:
	fee += 1.15 * (k - 15)
print("收费", round(fee), '元')