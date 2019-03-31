# 08_star_args.py

# 此示例示意星号元组形参

def func(*args):
    print("参数个数是:", len(args))
    print('args =', args)

func(1,2,3,4)
func("hello", "world", 1, 2, 3)