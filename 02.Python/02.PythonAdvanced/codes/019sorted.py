# 019sorted.py
name = ['Tom', 'Jerry', 'Spike', 'Tyke']

def fx(name):
	return name[::-1]

L2 = sorted(name, key=fx)
print(L2)