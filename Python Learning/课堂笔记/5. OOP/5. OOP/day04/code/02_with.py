# 02_with.py


# 此示例示意用try-except和with语句组合来实现文件的操作
def read_from_file(filename='info.txt'):
    try:
        with open(filename) as f:
            print("正在读取文件")
            n = int(f.read())
            print('n=', n)
            print('文件已经关闭')
        # f = open(filename)
        # try:
        #     print("正在读取文件")
        #     n = int(f.read())
        #     print("n=", n)
        # finally:
        #     f.close()
        #     print("文件已经关闭")
    except OSError:
        print("文件打开失败")


read_from_file()