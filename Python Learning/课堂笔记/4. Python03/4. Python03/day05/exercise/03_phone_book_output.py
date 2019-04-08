# 2. 写一个读取'phone_book.txt'文件的程序, 把保存的信息以表格的形式打印出来
#    +-----------+-----------------+
#    |  name     |   number        |
#    +-----------+-----------------+
#    | xiaozhang |   1388888888    |
#    +-----------+-----------------+


# 从文件中读取数据,形成相应的数据结构,传递给显示的函数
def read_info_from_file(filename='phone_book.txt'):
    '''读取文件,形成元组组成的列表'''
    L = []
    # 读取文件信息,形成元组后放入列表L
    try:
        f = open(filename)
        while True:
            # 读取数据形成元组
            s = f.readline()
            if not s:
                break
            s = s.rstrip()  # 去掉右侧的换行符'\n'
            name, number = s.split(',')  # 拆成['姓名', '电话']
            L.append((name, number))

        f.close()
    except OSError:
        print("打开文件失败!")

    return L

def print_infos(lst):
    print("打印表格请自己实现")
    print(lst)


if __name__ == '__main__':
    L = read_info_from_file()
    # print(L)
    print_infos(L)
