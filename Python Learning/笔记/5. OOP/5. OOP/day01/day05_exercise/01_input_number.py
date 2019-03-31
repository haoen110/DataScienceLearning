# 1. 写程序让用户输入一系列整数,当输入小于零的数时结束输入
#    1) 将输入的数字存于列表中
#    2) 将列表中的数字写入到文件numbers.txt中
#    (提示: 需要将整数转为字符串或字节串才能存入文件中)


# 1) 将输入的数字存于列表中
def get_number():
    '''此函数返回整数的列表'''
    L = []
    while True:
        i = int(input("请输入整数: "))
        if i < 0:
            break
        L.append(i)
    return L

# 2) 将列表中的数字写入到文件numbers.txt中
def save_to_file(lst, filename='numbers.txt'):
    try:
        # 打开文件
        f = open(filename, 'w')

        # 写入数据到文件
        for i in lst:
            f.write(str(i))
            f.write('\n')

        # 关闭文件
        f.close()
    except OSError:
        print("打开失败")

if __name__ == '__main__':
    L = get_number()
    print(L)
    save_to_file(L)