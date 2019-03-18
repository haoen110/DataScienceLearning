# 030poker.py
def get_poker():
	kinds = ['\u2660', '\u2663', '\u2665', '\u2666']
	number = ['A'] + [str(i) for i in range(1,11)] + list('JQK')
	L = [i + j for i in number for j in kinds ] + ['BP', 'SP'] 
	return L

import random as R

def poker():
	pk = get_poker()
	R.shuffle(pk)
	p1 = pk[:18]
	p2 = pk[18:18+17]
	p3 = pk[18+17:18+17+17]
	p4 = pk[-1:-4:-1]
	p = [p1, p2, p3, p4]
	for i in range(4):
		s = input("已经洗牌，输入回车查看第一个人的牌")
		if not s:
			print(p[i])

poker()