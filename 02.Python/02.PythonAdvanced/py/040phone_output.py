# 040phone_output.py

def poutput():
	f = open('040phone_book.txt')
	while True:
		s = f.readline()
		s = s.rstrip() # 去掉最后的\n换行符
		if not s:
			break
		else:
			name, number= s.split(sep=' ')
			print('|'+name.center(15)+'|'+number.center(15)+'|')
			print('+'+'-'*15+'+'+'-'*15+'+')
	f.close()
	
print('+'+'-'*15+'+'+'-'*15+'+')
print('|'+'name'.center(15)+'|'+'number'.center(15)+'|')
print('+'+'-'*15+'+'+'-'*15+'+')
poutput()