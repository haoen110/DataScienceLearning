# 2. 分解质因数,输入一个正整数，分解质因数:
#    如:
#      输入: 90
#      打印:
#          90=2*3*3*5
#   (质因数是指最小能被原数整数的素数(不包括1))

def is_prime(x):
    '''判断　x是否为素数'''
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def get_prime_list(n):
    '''此函数根据给定一个整数，返回此整数所有因数的列表'''
    # 如何用n求出所有的因数
    L = []  # 用来存放所有因数(素数)
    # 如果n不是素数，我们就拆出因数出来
    while not is_prime(n):
        # 把n拆出来一个素数因数，然后继续循环
        # 找n的一个因数:
        for x in range(2, n):
            if is_prime(x) and n % x == 0:
                # x一定是n的因数
                L.append(x)
                n /= x  # 下次再求n的因数
                n = int(n)  # 转为整数
                break
    else:
        L.append(n)
    return L

if __name__ == '__main__':
    n = int(input("请输入整数: "))
    print(get_prime_list(n))  



