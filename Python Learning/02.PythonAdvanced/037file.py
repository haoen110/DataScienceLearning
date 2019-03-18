# 037file.py
try:
	f = open('C:/Users/haoen110/iCloudDrive/Documents/DataScienceLearning/Python Learning/02.PythonAdvanced/037file_read.txt')
	print("打开文件成功！")
	
	s = f.readline()
	if s != '':
		print("读取成功，文字是：", s)
	else:
		print("文件内已经没有数据可读了")

	s = f.readline()
	print("第二行数据是：", s)
	s = f.readline()
	print("第三行数据是：", s)

	s = f.readline()
	if s != '':
		print("文件内已经没有数据可读了")
	else:
		print("第四行数据是", s)

	f.close()
except OSError:
	print("打开文件失败！")
