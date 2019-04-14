# mymod7.py


'''此模块示意模块内的隐藏属性'''


def f1():
    pass

def _f2():
    '''
    此函数在被其它模块用from import * 导放时，将不被导入
    '''
    pass

var1 = "变量1"
_var2 = '变量2'  # _var2也是隐藏变量，也不会被导入