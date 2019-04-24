import sys
# import pdb

def add(n1 = 0,n2 = 0):
    return int(n1) + int(n2)

def sub(n1 = 0,n2 = 0):
    return  int(n1) - int(n2)

def main():
    print(sys.argv)

    # #开启pdb调试
    # pdb.set_trace()

    a = add(sys.argv[1],sys.argv[2])
    print(a)
    s = sub(sys.argv[1],sys.argv[2])
    print(s)

main()