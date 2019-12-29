# 034gen.py
def myodd(x):
	i = 0
	while i < x:
		if i % 2 == 1:
			yield i
		i += 1

for x in myodd(10):
	print(x)