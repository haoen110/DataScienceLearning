s1 = {1,2,3}
s2 = {2,3,4}
s = s1

if True:  # if False
    s1 = s1 | s2  # 对于可变对象，不等同于 s1 += s2
    print(s)  # {1, 2, 3}
else:
    s1 |= s2
    print(s)  # {1, 2, 3, 4}
