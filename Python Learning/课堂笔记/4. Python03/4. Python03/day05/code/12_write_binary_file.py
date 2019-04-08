# 12_write_binary_file.py


# 此示例示意以二进制模式进行写操作

try:
    f = open("data.bin", 'wb')
    # 在此处需要以字节串为单位进行写操作
    f.write(b'\xe4')  # '中'字的编码: e4 b8 ad
    f.write(b'\xb8')
    f.write(b'\xad')
    f.write(b'\n\x41\x42\x43')
    f.close()
except OSError:
    print("文件打开失败!")