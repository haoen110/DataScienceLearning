# 此示例示意F.readlines的用法


try:
    f = open('../exercise/info.txt')
    L = f.readlines()  # 返回所有行文字的列表
    print(L)
    f.close()
except OSError:
    print("打开文件文件")