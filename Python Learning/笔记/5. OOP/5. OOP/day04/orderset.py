open # 练习：
#   实现有序集合类OrderSet()， 能实现两个集合的
#     交集 &
#     并集 |
#     补集 -
#     对称补集 ^
#     == / != 等
#     与集合相同

#   s1 = OrderSet([1,2,3,4])
#   s2 = OrderSet([3,4,5])
#   print(s1 & s2)  # OrderSet([3,4])
#   print(s1 | s2)  # OrderSet([1,2,3,4,5])
#   print(s1 - s2)  # OrderSet([1,2])
#   print(s1 ^ s2)  # OrderSet([1,2,5])
#   if OrderSet([1,2,3]) != OrderSet([1,2,3,4])
#      print("不相等")
#   # 思考是否可以实现以下操作?
#   if 2 in s1:
#      print("2 在 s1 内")


class OrderSet:
    def __init__(self, it=None):
        if it is None:
            self.data = []
        elif it:
            self.data = [x for x in it]

    def __repr__(self):
        return "OrderSet(%r)" % self.data

    def __and__(self, rhs):
        return OrderSet(
            (x for x in self.data if x in rhs.data)
        )

    def __or__(self, rhs):
        return OrderSet(
            self.data + [x for x in rhs.data
                         if x not in self.data]
        )

    def __sub__(self, rhs):
        return OrderSet(
            (x for x in self.data if x not in rhs.data)
        )

    def __xor__(self, rhs):
        return (self - rhs) | (rhs - self)

    def __eq__(self, rhs):
        return self.data == rhs.data

    def __ne__(self, rhs):
        return self.data != rhs.data

    def __contains__(self, ele):
        return ele in self.data


s0 = OrderSet()
s1 = OrderSet([1, 2, 3, 4])
s2 = OrderSet([3, 4, 5])
print(s1 & s2)  # OrderSet([3,4])
print(s1 | s2)  # OrderSet([1,2,3,4,5])
print(s1 - s2)  # OrderSet([1,2])
print(s1 ^ s2)  # OrderSet([1,2,5])
if OrderSet([1, 2, 3]) != OrderSet([1, 2, 3, 4]):
    print("不相等")
# 思考是否可以实现以下操作?
if 2 in s1:
    print("2 在 s1 内")

if 100 not in s1:
    print("100 不在 s1 内")
