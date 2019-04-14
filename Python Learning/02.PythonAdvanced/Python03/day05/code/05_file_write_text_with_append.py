# 04_file_write_text.py

# 此示例示意以'a'模式打开文件并写入文件

f = open('mynote.txt', 'a')
f.write('world')
f.close()