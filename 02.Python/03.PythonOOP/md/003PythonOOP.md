
# Python面向对象编程3
---

# override 函数重写

- 重写是在自定义的类内添加相应的方法，让自定义的类生成的对象（实例）像内建对象一样进行内建的函数操作

## 对象转字符串函数重写

- repr(obj) 返回一个能代表此对象的**表达式字符串**（带引号的可以执行），通常：
    - eval(repr(obj)) == obj
    
    
- str(obj) 通常给定的对象返回一个**字符串**（这个字符串通常是给人看的）

    
- 对象转字符串函数重写方法：
    - repr() 函数的重写方法：  
    ```def __repr__(self):
        return 能够表达self内容的字符串```
    - srt() 函数的重写方法：  
    ```def __str__(self:
        return 人能看懂的字符串```
        
        
- 说明：
    1. str(obj) 函数优先调用obj.\_\_str\_\_()方法返回字符串
    2. 如果obj没有\_\_str\_\_()方法，则调用obj.\_\_str\_\_()方法返回的字符串
    3. 如果obj没有\_\_repr\_\_()方法， 则调用obj.\_\_repr\_\_()实例方法显示<xxxx>格式的字符串


```
# 此示例示意一个自定义的数字类型重写repr和str方法的用法
class MyNumber:
    def __init__(self, value):
        self.data = value
    
    def __str__(self):
        print("str被调用")
        return "数字：%d" % self.data
    
    def __repr__(self):
        print("repr被调用")
        return "MyNumber(%d)" % self.data
        
#     def __len__(self): # 重写了len
#         return 100
# n1 = MyNumber()
# x = len(n1)
# print(x)

n1 = MyNumber(100)
print(str(n1))
print(repr(n1))
print(n1)
```

    str被调用
    数字：100
    repr被调用
    MyNumber(100)
    str被调用
    数字：100


## 数值转换函数的重写

    - def __complex__(self)    complex(obj) 函数调用
    - def __int__(self)        int(obj) 函数调用
    - def __float__(self)      float(obj) 函数调用
    - def __bool__(self)       bool(obj) 函数调用


```
# 此示例示意自定义的类MyNumber能够转成数值类型
class MyNumber:
    def __init__(self, v):
        self.data = v
    def __repr(self):
        return "MyNumber(%d)" % self.data
    
    def __int__(self):
        '''此方法用于int(obj) 函数重载，必须返回整数
        此方法通常用于制定自定义对象如何转为整数的规则
        '''
        return 10000

n1 = MyNumber(100)
print(type(n1))
n = int(n1)
print(n, type(n))
```

    <class '__main__.MyNumber'>
    10000 <class 'int'>


## 内建函数重写

    - __abs__      abs(obj)
    - __len__      len(obj)
    - __reversed__ reversed(obj)
    - __round__    round(obj)


```
# 自定义一个MyList，与系统内建的类一样，用来保存有先后顺序关系的数据

class MyList:
    '''自定义列表类'''
    def __init__(self, iterator=[]):
        self.data = [x for x in iterator]
        
    def __repr__(self):
        return "MyList(%r)" % self.data
    
    def __abs__(self):
        return MyList([abs(x) for x in self.data])
    
    def __len__(self):
        return len(self.data)
    
myl = MyList([1, -2, 3, -4]) 
print(myl)
print("绝对值列表是：", abs(myl))

myl2 = MyList(range(10))
print(myl2)
print("ml2的长度是：", len(myl2))
```

    MyList([1, -2, 3, -4])
    MyList([1, 2, 3, 4])
    MyList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    10


## 布尔测试函数的重写

- 格式： `def __bool__(self):`


- 作用：
    - 用于bool(obj) 函数取值
    - 用于if语句真值表达式中
    - 用于while语句真值表达式中
    
- 说明：
    - 优先调用\_\_bool\_\_方法取值
    - 如果不存在\_\_bool\_\_方法，则用\_\_len\_\_()方法取值，如果不为零返回True，否则返回Fales
    - 如果再没有\_\_len\_\_方法，则直接返回True
    
 


```
class MyList:
    '''自定义列表类'''
    def __init__(self, iterator=[]):
        self.data = [x for x in iterator]
        
    def __repr__(self):
        return "MyList(%r)" % self.data
    
    def __abs__(self):
        return MyList([abs(x) for x in self.data])
    
    def __len__(self):
        return len(self.data)
    
myl = MyList([1, -2, 3, -4]) 
print(bool(myl)) # True 调用了len，若len也没有，返回True
```

    True


## 迭代器（高级）

- 什么是迭代器
    - 可以通过next(it) 函数取值的对象就是迭代器
    
    
- 迭代器协议：
    - 迭代器协议是指对象能够使用next函数获取下一项数据，在没有下一项数据时出发一个StopIterator来种植迭代的约定
    
    
- 实现方法：
    - 类内需要有__next__(self) 方法来实现迭代器协议
    
    
- 语法:

```class MyIterator:
    def __next__(self):
        迭代器协议的实现
        return 数据
        ```  
        
- 什么是可迭代对象
    - 是指能用iter(obj) 函数返回迭代器的对象（实例）可迭代对象内部一定要定义\_\_iter\_\_(self)方法来返回迭代器



```
# 此示例示意可迭代对象和迭代器的定义以及使用方法：
class MyList:
    def __init__(self, iterator):
        '''自定义列表的初始化方法，此方法创建一个data实例变量
        来绑定一个用来存储数据的列表'''
        self.data = list(iterator)
        
    def __repr__(self):
        '''此方法为了打印此列表数据'''
        return 'MyList(%r)' % self.data
    
    def __iter__(self):
        '''有此方法就是可迭代对象，但是要求必须返回迭代器'''
        print("__iter__方法被调用")
        return MyListIterator(self.data)

class MyListIterator:
    '''此类用来创建一个迭代器对象，用此迭代器对象可以访问
    MyList类型的数据'''
    def __init__(self, iter_data):
        self.cur = 0 # 设置迭代器的初始值为0,代表列表的索引
        # it_data 绑定要迭代的列表
        self.iter_data = iter_data
        
    def __next__(self):
        '''有此方法的对象才叫迭代器，
        此方法一定要实现迭代器协议'''
        # 如果self.cur已经超出了列表的索引范围，就报迭代结束错误
        if self.cur >= len(self.iter_data):
            raise StopIteration
        # 否则尚未迭代完成，需要返回数据
        r = self.iter_data[self.cur] # 拿到要送回去的数
        self.cur += 1 # 将当前值向后移动一个单位
        return r
    
    
myl = MyList([2,3,5,7])
print(myl)
for x in myl:
    print(x)
```

    MyList([2, 3, 5, 7])
    __iter__方法被调用
    2
    3
    5
    7


# 异常（高级）

- 回顾异常相关的语句：
        - try-except 用来捕获异常通知
        - try-finally 用来做一定要做的事情
        - raise 用来发生异常通知
        - assert 用来根据条件发出AssertionError类型的异常通知
        
## with 语句


- 语法：
    - ```with 表达式1 [as 变量1], 表达式2 [as 变量2]:
        语句块```
        
        
- 作用：
    - 使用于对资源进行访问的场合，确保使用过程中不管是否发生异常，都会执行必须"清理"操作，并释放资源
        - 如：文件使用后自动关闭，线程中锁的自动获取和释放等
        
        
- 说明：
    - 能够用于with语句进行管理的对象必须是**环境管理器**


```
# 此示例用try-except和try-finally组合来对文件进行操作
def read_from_file(filename='info.txt'):
    try: # 确保文件不崩溃
        f = open(filename)
        try:    # 这个try用来确保能够close
            print("正在读取文件")
            n = int(f.read())
        finally:
            f.close()
    except OSError:
        print("文件打开失败")

read_from_file()
```

    文件打开失败



```
# 
def read_from_file(filename='info.txt'):
    try: # 确保文件不崩溃
        with open(filename) as f: # with 会自动调用close
            print("正在读取文件")
            n = int(f.read())
            print("n=", n)
            print("文件已关闭")
    except OSError:
        print("文件打开失败")

read_from_file()
```

    正在读取文件
    n= 123
    文件已关闭


## 环境管理器
1. 类内有\_\_enter\_\_ 和 \_\_exit\_\_实例方法的类被成文环境管理器
2. 能够用with语句管理的对象必须是环境管理器
3. \_\_enter\_\_方法将在进入with语句时被调用，并返回由as变量管理的对象
4. \_\_exit\_\_将在离开with语句时被调用，并且可以用参数来判断在离开with语句时是否有异常发生，并作出相应处理


```
class A:
    def __enter__(self):
        print("已进入with语句")
        return self # 返回的对象由as绑定
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        '''此方法会在退出with语句时自动调用
        exc_type 在没有异常时为None，出现异常时为异常类型
        exc_val 在没有异常时为None，出现异常时绑定错误对象
        exc_tb 在没有异常时为None，在出现异常时绑定traceback'''
        
        if exc_type is None:
            print("已离开with语句，离开时状态正常")
        else:
            print("已离开with语句，离开时状态异常")
            print("异常类型是：", exc_type)
            print("错误对象时：", exc_val)
            print("traceback是：", exc_tb)

a = A()
with A() as a:
    print("以下是with语句内的一条语句")
    int(input())
```

    已进入with语句
    以下是with语句内的一条语句
    a
    已离开with语句，离开时状态异常
    异常类型是： <class 'ValueError'>
    错误对象时： invalid literal for int() with base 10: 'a'
    traceback是： <traceback object at 0x10bc99888>



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-31-5e7aa7e26050> in <module>
         21 with A() as a:
         22     print("以下是with语句内的一条语句")
    ---> 23     int(input())
    

    ValueError: invalid literal for int() with base 10: 'a'


## 对象的属性管理函数

- getattr(obj, name[, default])
    - 从一个对象得到对象的属性；getattr(x,'y')等同于x.y；当属性不存在时，如果给出default参数，则返回default；如果没有给出default则产生一个ArributeError错误


- hasattr(obj, name)
    - 用给定的name返回对象obj是否有该属性，此种做法可以避免在getattr(obj, name)时引发错误
    
    
- setattr(obj, name, value)
    - 给对象obj的名为name的属性设置相应的值value，set(x, 'y', v)等同于x.y = v
    
    
- delattr(obj, name)
    - 删除对象obj中的name属性，delattr(x, 'y')等同于def x.y
    



```
class Dog:
    pass

dog1 = Dog()
print(getattr(dog1, 'color', '没有颜色'))

dog1.color = 'Yellow'
print(getattr(dog1, 'color', '没有颜色'))

dog2 = Dog()
setattr(dog2, 'kind', '金毛')
print(dog2.kind)

delattr(dog2, 'kind')
```

    没有颜色
    Yellow
    金毛


# 运算符重载

- 让自定义的类生成的对象（实例）能够运用运算符进行操作


- 作用：
    - 让自定义的类的实例像内建对象一样运行运算符操作
    - 让程序简介易读
    - 对自定义的对象，将运算符赋予新的运算规则
    
    
- 算术运算符的重载：
    
    ```
    __add__(self, rhs)        self + rhs 加法
    __sub__(self, rhs)        self - rhs 减法
    __mul__(self, rhs)        self * rhs 乘法
    __truediv__(self, rhs)        self / rhs 除法
    __floordiv__(self, rhs)        self // rhs 地板除法
    __mod__(self, rhs)        self % rhs 求余
    __pow__(self, rhs)        self ** rhs 幂
    ```


- 说明：
    - *运算符重载不能改变运算的优先级*


```
class MyNumber:
    def __init__(self, v):
        self.data = v
    
    def __repr__(self):
        return "MyNumber(%d)" % self.data
    
    def __add__(self, other):
        print("__add__被调用")
        v = self.data + other.data
        return MyNumber(v)
    
    def __sub__(self, other):
        print("__sub__被调用")
        v = self.data - other.data
        return MyNumber(v)
    
    
n1 = MyNumber(100)
n2 = MyNumber(200)
n3 = n1 + n2
n4 = n2 - n1
print(n3, n4)

class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%r)" % self.data
    
    def __add__(self, other):
        return MyList(self.data + other.data)
    
    def __mul__(self, num):
        return MyList(self.data * num)
    
L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L3 = L1 + L2
print(L3) # MyList([1, 2, 3, 4, 5, 6])
L4 = L2 + L1
print(L4) # MyList([4, 5, 6, 1, 2, 3])
L5 = L1 * 2
print(L5) # MyList([1, 2, 3, 1, 2, 3])
```

    __add__被调用
    __sub__被调用
    MyNumber(300) MyNumber(100)
    MyList([1, 2, 3, 4, 5, 6])
    MyList([4, 5, 6, 1, 2, 3])
    MyList([1, 2, 3, 1, 2, 3])


## 反向算术运算符重载：

```
__radd__(self, lhs)        lhs + self 加法
__rsub__(self, lhs)        lhs - self 减法
__rmul__(self, lhs)        lhs * self 乘法
__rtruediv__(self, lhs)        lhs / self 除法
__rfloordiv__(self, lhs)        lhs // self 地板除法
__rmod__(self, lhs)        lhs % self 求余
__rpow__(self, lhs)        lhs ** self 幂
```


```
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%r)" % self.data
    
    def __add__(self, other):
        return MyList(self.data + other.data)
    
    def __mul__(self, num):
        'mul被调用'
        return MyList(self.data * num)
    
    def __rmul__(self, num):
        'rmul被调用'
        return MyList(self.data * num)
    
    
L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L4 = L1 * 2
L5 = 3 * L1
print(L4)
print(L5)
```

    MyList([1, 2, 3, 1, 2, 3])
    MyList([1, 2, 3, 1, 2, 3, 1, 2, 3])


## 复合赋值算术运算符重载

```
__iadd__(self, rhs)        self += rhs 加法
__isub__(self, rhs)        self -= rhs 减法
__imul__(self, rhs)        self *= rhs 乘法
__itruediv__(self, rhs)        self /= rhs 除法
__ifloordiv__(self, rhs)        self //= rhs 地板除法
__imod__(self, rhs)        self %= rhs 求余
__ipow__(self, rhs)        self **= rhs 幂
```


```
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%r)" % self.data
    
    def __add__(self, other):
        return MyList(self.data + other.data)
    
    def __mul__(self, num):
        return MyList(self.data * num)
    
    def __iadd__(self, rhs): 
        print("__iadd__被调用！")
        self.data.extend(rhs.data)
        return self
        
L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L1 += L2 # 当没有__iadd__方法时，等同于调用L1 = L1 + L2
print(L1)
```

    __iadd__被调用！
    MyList([1, 2, 3, 4, 5, 6])


- 问题  

```
L = [1,2,3]
def f1():
    global L # 这里必须加global L
    L = L + [4, 5, 6]

f1()
print(L)

def f2():
    # 这里就不用加global L
    L += [4, 5, 6] # 这里相当于调用了L.__iadd__([4, 5, 6])
    
f2()
```

## 比较运算符的重载

```
__lt__(self, rhs)        self < rhs 
__le__(self, rhs)        self <= rhs 
__gt__(self, rhs)        self > rhs 
__ge__(self, rhs)        self >= rhs 
__eq__(self, rhs)        self == rhs 
__ne__(self, rhs)        self != rhs 
```

## 位运算符重载

```
__invert__(self)        ~ self 取反
__and__(self, rhs)      self & rhs 位与
__or__(self, rhs)      self | rhs 位或
__xor__(self, rhs)      self ^ rhs 位异或
__lshift__(self, rhs)      self << rhs 左移
__rshift__(self, rhs)      self >> rhs 右移
```

## 反向位运算符重载

```
__rand__(self, rhs)      lhs & self 位与
__ror__(self, rhs)      lhs | self 位或
__rxor__(self, rhs)      lhs ^ self 位异或
__rlshift__(self, rhs)      lhs << self 左移
__rrshift__(self, rhs)      lhs >> self 右移
```

## 复合赋值位运算符重载
```
__iand__(self, rhs)      self &= rhs 位与
__ior__(self, rhs)      self |= rhs 位或
__ixor__(self, rhs)      self ^= rhs 位异或
__ilshift__(self, rhs)      self <<= rhs 左移
__irshift__(self, rhs)      self >>= rhs 右移
```

## 一元运算符的重载
```
__neg__(self)         - self 负号
__pos__(self)         + self 正号
__invert__(self)         ~ self 取反
```


```
# 一元运算符的重载方法：
class MyList:
    def __init__(self, iterable):
        print("__init__被调用")
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%r)" % self.data
    
    def __neg__(self):
        '''此方法用来制定-self返回的规则'''
        L = [-x for x in self.data]
        return MyList(L)
    
L1 = MyList([1, -2, 3, -4])
L2 = -L1
print(L2)
```

    __init__被调用
    __init__被调用
    MyList([-1, 2, -3, 4])


## in / not in 运算符的重载

- 重载方法：


```
class MyList:
    def __init__(self, iterable):
        print("__init__被调用")
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%r)" % self.data
    
    def __contains__(self, e):
        '''此方法用来实现 in / not in 运算符的重载'''
        print("__contains__被调用")
        for x in self.data:
            if x == e:
                return True
        return False
        
L1 = MyList([1, -2, 3, -4])
if -2 in L1:
    print("-2 在 L1 中")
else:
    print("-2 不在 L1 中")
```

    __init__被调用
    __contains__被调用
    -2 在 L1 中


## 索引和切片运算符重载

```
__getitem__(self, i)        x = self[i] 索引/切片取值
__setitem__(self, i, v)     self[i] = v 索引/切片赋值
__delitem__(self, i)        del self[i] del语句删除索引等
```


- 作用：
    - 让自定义类型的对象能够支持索引和切片操作


```
# 此示例示意[]运算符的重载
class MyList:
    def __init__(self, iterable):
        print("__init__被调用")
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%r)" % self.data
    
    def __getitem__(self, i):
        print("__getitem__被调用, i=", i)
        return self.data[i]
    
    def __setitem__(self, i, v):
        print("__setitem__被调用, i=", i, 'v = ', v)
        self.data[i] = v
        
L1 = MyList([1, -2, 3, -4])
v = L1[0]
print(v)

L1[1] = 2 # 等同于调用L1.__setitem__(1, 2)
print(L1)
```

    __init__被调用
    __getitem__被调用, i= 0
    1
    __setitem__被调用, i= 1 v =  2
    MyList([1, 2, 3, -4])


# slice 函数

- 作用：
    - 用于创建一个slice切片对象，此对象存储一个切片的起始值、中止值和步长信息
    - ` slice(start, stope=None, step=None) 创建一个切片对象 ` 
    
    
- 属性：
    - s.start 切片起始值，默认为None
    - s.stop  切片中止值，默认为None
    - s.step  切片步长，默认为None


```
class MyList:
    def __init__(self, iterable):
        print("__init__被调用")
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%r)" % self.data
    
    def __getitem__(self, i):
        print("__getitem__被调用, i=", i)
        if type(i) is int:
            print("正在做索引操作")
        elif type(i) is slice:
            print("正在做切片操作")
            print("切片的起始值为：", i.start)
            print("切片的中止值为：", i.stop)
            print("切片的步长值为：", i.step)
        return self.data[i]

L1 = MyList([1, -2, 3, -4, 5, -6])
print(L1[::2]) # 相当于 L1[slice(None, None, 2)] L.__getitem__(slice(None, None, None))

```

    __init__被调用
    __getitem__被调用, i= slice(None, None, 2)
    正在做切片操作
    切片的起始值为： None
    切片的中止值为： None
    切片的步长值为： 2
    [1, 3, 5]

