# 10_try_finally.py


# 以煎蛋为例, 
  # 1. 打开天燃
  # 2. 煎蛋
  # 3. 关闭天燃气

def fry_egg():
    print("打开天燃气点燃...")
    try:
        count = int(input("请输入鸡蛋个数:"))
        print("煎蛋完成,共煎了%d个鸡蛋" % count)
    finally:
        print("关闭天燃气")

try:
    fry_egg()
except:
    print("程序已转为正常状态!")

