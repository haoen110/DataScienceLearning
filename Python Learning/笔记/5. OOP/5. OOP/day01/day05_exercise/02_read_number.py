# 2. 写程序,将文件numbers.txt中的整数读入到内存中,
#   重新形成数字组成的列表.计算这些数的最大值,
#   最小值,和他们的和

def read_from_file(filename='numbers.txt'):
    L = []
    # 读取文件数据放入列表
    try:
        f = open(filename)
        # 读数据
        try:
            for line in f:  # line 绑定末尾到'\n'的字符串
                n = int(line.rstrip())
                L.append(n)
        finally:
            f.close()
    except OSError:
        print("读取文件出错")
    except ValueError:
        print("读取文件时出错,数据可能不完整")


    return L

if __name__ == '__main__':
    L = read_from_file()
    print("最大:", max(L))
    print("最小:", min(L))
    print('和:', sum(L))