# 01_with.py


# 此示例示意用try-except 和 try-finally 组合来对文件进行操作
# 用with语句可以实现同样的功能,见: 02_with.py
def read_from_file(filename='info.txt'):
    try:
        f = open(filename)
        try:
            print("正在读取文件")
            n = int(f.read())
            print("n=", n)
        finally:
            f.close()
            print("文件已经关闭")
    except OSError:
        print("文件打开失败")


read_from_file()