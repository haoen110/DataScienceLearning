# 10_star_star_dict_kwargs.py


# 此示例示意双星号字典形参kwargs收集多余的关键字传参
def func(**kwargs):
    print("关键字参数个数是:", len(kwargs))
    print("kwargs =", kwargs)


func(name='tarena', age=15)
func()
