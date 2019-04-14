#计算密集型
def count(x,y):
    c = 0
    while c < 6000000:
        c += 1
        x += 1
        y += 1

#IO秘籍函数
def write():
    f = open('test.txt','w')
    for i in range(1000000):
        f.write("hello world\n")
    f.close()
def read():
    f = open('test.txt')
    lines = f.readlines()
    f.close()