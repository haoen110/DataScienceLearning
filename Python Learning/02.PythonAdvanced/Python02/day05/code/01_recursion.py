

# 此示例示意函数间接调用自身的递归
def fa():
    fb()


def fb():
    fa()

fa()
print("递归结束")
