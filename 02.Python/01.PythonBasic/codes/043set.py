# 043set.py
s1 = {'曹操', '刘备', '周瑜'}
s2 = {'曹操', '周瑜', '张飞', '赵云'}
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)
print('张飞' in s1)
print(s1 ^ s2)
print(len(s1 | s2))