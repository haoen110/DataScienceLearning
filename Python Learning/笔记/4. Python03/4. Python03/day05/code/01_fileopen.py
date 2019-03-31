# 01_fileopen.py


# 此示例示意 文件的打开和关闭,及错误处理


try:
    # f = open('/etc/passwd')  # 此时能成功打开

    # f = open('/root/abc.txt')  # 此文件不存在
    f = open("./abc.txt")
    print("文件打开成功!")

    # 在此外进行文件的读写操作

    f.close()  # 关闭文件
except OSError:
    print("打开文件失败！")

