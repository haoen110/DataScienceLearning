def myfun(a, b, c):
    print("a bind:", a)
    print("b bind:", b)
    print("c bind:", c)

myfun(1, 2, 3)
s1 = [1, 2, 3]
myfun(*s1)
s1 = ["A", "B", "C"]
myfun(*s1)
