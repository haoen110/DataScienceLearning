# 14_file_seek.py


# 此示例示意 用F.seek方法来移动文件的读写指针位置

f = open('data.txt', 'rb')
# 方法1
# f.seek(5, 0)  # 相对于文件头向后移动5个字节
# 方法2
# f.seek(-15, 2)  # 相对于文件尾向前移动15个字节
# 方法3
b = f.read(2)  # 先读取2个字节
f.seek(3, 1)  # 相对于当前位置向后移动3个字节

b = f.read(5)
print(b)  # b'abcde'

f.close()
