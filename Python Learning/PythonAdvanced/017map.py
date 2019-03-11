# 017map.py
def pow2(x):
	return x ** 2
print(sum(map(pow2, range(1,10))))

print(sum(map(lambda x: x**2, range(1, 10))))
print(sum(map(pow, range(1,10), range(9,0,-1))))




