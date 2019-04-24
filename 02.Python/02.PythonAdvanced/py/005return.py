# 005return.py
def mymax(a, b):
	if a > b:
		return a
	else:
		return b

def mymax1(a, b):
	if a > b:
		return a
		
	return b

print(mymax(100, 200)) # 200
print(mymax(50, 10)) # 50
print(mymax('ABC', 'ABCD')) # ABCD
