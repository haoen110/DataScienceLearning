# 038dict.py
d = {1: '春季有1,2,3月',
	 2: '夏季有4,5,6月',
	 3:	'秋季有7,8,9月',
	 4: '冬季有10,11,12月'}
s = int(input("请输入季度1~4"))
print(d.get(s, '信息不存在'))

