# 040phone_input.py
def pinput():
	try:
		f = open('040phone_book.txt', 'x')
	except FileExistsError:
		f = open('040phone_book.txt', 'a')
	except OSError:
		print("打开文件失败！")
	print("打开文件成功")
	while True:
		name = input("请输入姓名：")
		if name:
			number = input("请输入电话：")
			L = [name+' ', number+'\n']
			f.writelines(L) 
		else:
			break
	f.close()

if __name__ = '__main__':
	pinput()



