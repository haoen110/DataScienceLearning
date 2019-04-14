


# 此示例示意环境管理器的定义及使用
class A:
    def __enter__(self):
        print("已进入with语句")
        return self  # 返回的对象将由 as绑定
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("已离开with语句")

# a = A()
with A() as a:
    print("这是with语句内的一条语句")
    int(input("请输入整数: "))
