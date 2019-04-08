# mymod6.py

'''此模块示意__all__列表的作用和用法
'''

# 限制 用 from mymod6 import * 时只导入 f1, var1
__all__ = ['f1', 'var1']

def f1():
    pass

def f2():
    pass

def f3():
    pass

var1 = "hello"
var2 = 'world'
