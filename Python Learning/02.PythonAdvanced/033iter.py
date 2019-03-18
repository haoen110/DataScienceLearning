# 033iter.py
s = {'唐僧', '悟空', '八戒', '沙僧'}
it = iter(s)
while True:
	try:
		s = next(it)
		print(s)
	except:
		break