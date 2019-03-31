# 13_file_tell.py


# 此示例示意用 f.tell()方法获取文件当前的读写位置

f = open('data.txt', 'rb')
print("当前的读写位置是:", f.tell())  # 0
b = f.read(5)
print("当前的读写位置是:", f.tell())  # 5
b = f.read()  # 读取全部内容
print("文件最后的位置是:", f.tell())  # 20
f.close()
