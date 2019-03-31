# 练习:
#   1. 写一个程序,从键盘输入如下信息:
#       姓名  和 电话号码
#     如 :
#       请输入姓名: xiaozhang
#       请输入电话: 13888888888
#       请输入姓名: xiaoli
#       请输入电话: 13999999999
#       请输入姓名: <回车>
#     把从键盘读取的信息存入'phone_book.txt'文件中
#       然后用 sublime text 打开并查看写入的内容

def input_phone_number():
    '''此函数用来读取用户输入,形成元组列表并返回'''
    L = []
    while True:
        name = input("请输入姓名: ")
        if not name:
            break
        number = input("请输入电话: ")

        L.append((name, number))  # 形成元组('姓名','电话')

    return L

def write_to_file(lst, filename='phone_book.txt'):
    '''将 lst列表内的数据存放到文件 filename中'''
    try:
        f = open(filename, 'w')
        for name, number in lst:
            f.write(name)
            f.write(',')
            f.write(number)
            f.write('\n')

        f.close()
    except OSError:
        print("写入文件失败!!!")


if __name__ == '__main__':
    L = input_phone_number()
    print(L)
    write_to_file(L)