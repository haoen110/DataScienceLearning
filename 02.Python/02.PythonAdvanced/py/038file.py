# 038file.py
def readline():
	try:
		f = open('038file_read.txt')
		while True:
			s = f.readline()
			if s:
				if s[-1] == '\n': # 如果最后有换行符，那么就不读
					print('-->', s[:-1])
				else:
					print('-->', s) # 读取最后一行没有\n
			else:
				break
		f.close()
	except OSError:
		print("读取文件失败")

readline()

def readlines():
	try:
		f = open('038file_read.txt')
		L = f.readlines()
		print(L)
		f.close()
	except OSError:
		print("读取文件失败")

readlines()


f = open('038file_read.txt')
print(f.read(1)) # 获取size个字符