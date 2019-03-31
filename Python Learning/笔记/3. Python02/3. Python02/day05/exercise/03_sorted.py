# names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# 让names排序
#   排序的依据是字符串的反序
#          'moT'    'yrreJ'  'ekipS'  'keyT'
# L2 = sorted(names, ....) 
# 排序后:
# L2 = ['Spike', 'Tyke', 'Tom', 'Jerry']

names = ['Tom', 'Jerry', 'Spike', 'Tyke']

def fx(name):
    return name[::-1]

# L2 = sorted(names, key=fx) 
L2 = sorted(names, key=lambda n: n[::-1])
# L2 = ['Spike', 'Tyke', 'Tom', 'Jerry']

print(L2)