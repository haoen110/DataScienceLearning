

def div_apple(n):
    print('%d个苹果您想分给几个人?' % n)
    s = input('请输入人数: ')
    cnt = int(s)  # <<= 可能触发ValueError错误异常
    # 以下一行可能触发ZeroDivisionError错误异常
    result = n / cnt
    print("每人个分了", result, '个苹果')

try:
    print("开始分苹果")
    div_apple(10)
    print("分苹果完成")
except ValueError:
    print("值错误，已处理")
finally:
    print("我是finally子句，我一定会执行的!")

print("程序正常退出")