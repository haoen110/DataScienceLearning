# １．　用生成器函数primes(begin, end)生成素数，给出起始值begin和终止值stop,　生成此范围内的全部素数，不包含(stop)

# 如:
# 　　　L = [x for x in primes(10, 20)] 
# 　　　将得到列表L = [11, 13, 17, 19]

def is_prime(x):
    if x <= 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def primes(begin, end):
    i = begin
    while i < end:
        # 如果i是素数,则生成i
        if is_prime(i):
            yield i
        i += 1


L = [x for x in primes(10, 20)] 
print(L)