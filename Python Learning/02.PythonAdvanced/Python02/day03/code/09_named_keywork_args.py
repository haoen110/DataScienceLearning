# 09_named_keywork_args.py

# 此示例示意命名关键字形参

def fn(*, d, e):
    print("d=", d)
    print("e=", e)

fn(d=100, e=200)  # 合法调用
# fn(1, 2)  # 不合法，不能用位置传参
# fn(1, 2, d=100, e=200)

def fm(*args, d, e):
    print(args)
    print('d=', d)
    print('e=', e)

fm(1, 2, d=100, e=200)
fm(*"AB", **{'e': 20, 'd':10})