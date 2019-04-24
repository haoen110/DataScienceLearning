
# Python面向对象编程2
---

## 编程语言的特征：
- 继承
- 封装
- 多态
    - 如：C++ / Java / Python / Swift / C#

# inheritance 继承 drived 派生

- 概念：
    - **继承**是指从已有的类中衍生出新类，新类具有原类的行为，并能扩展新的行为
    - **派生**就是从一个已有的衍生（创建）新类，在新类上可以田间新的属性的行为

- 目的：
    - **继承**是延续旧类的功能
    - **派生**是为了在旧类的基础上添加新的功能
    
- 作用：
    - 用继承派生机制，可以将一些共有功能加在基类中，实现代码的共享
    - 在不改变基类的基础上改变原有功能
    
- 名词：
    - 基类(base class)
    - 超类(super class)
    - 父类(father class)
    - 派生类(derived class)
    - 子类(child class)

- 说明：
    - 任何类都直接或间接继承自object类
    - object类是一切类的超类（祖类）不写相当于def Human(object):...
    - **类的```__base__```属性**用来记录此类的基类
    ```Human.__base__```

## 单继承

- 语法：

```class 类名(基类名):
    语句块```
    
- 说明：
    - 单继承是派生类由一个基类衍生出来的类


```python
# 此示例示意继承和派生
class Human:
    '''此类用来描述人类的共性行为'''
    def say(self, that):
        print("说：", that)
    def walk(self, distance):
        print("走了：", distance, "公里")
        
print("\n-----人类-----")        
h1 = Human()
h1.say("今天天气真热")
h1.walk(5)

class Student(Human):
    def study(self, subject):
        print("正在学习", subject)

print("\n-----学生-----")
s1 = Student()
s1.say("今天天气真热")
s1.walk(6)
s1.study("Python")

class Teacher(Student):
    def teach(self, subject):
        print("正在教", subject)

print("\n-----教师-----")
t1 = Teacher()
t1.say("明天就星期六啦")
t1.walk(8)
t1.teach("OOP")
t1.study("Piano")
```

    
    -----人类-----
    说： 今天天气真热
    走了： 5 公里
    
    -----学生-----
    说： 今天天气真热
    走了： 6 公里
    正在学习 Python
    
    -----教师-----
    说： 明天就星期六啦
    走了： 8 公里
    正在教 OOP
    正在学习 Piano


## override 覆盖

- 概念：
    - 覆盖是指在有继承关系的子类中，子类中实现了与基类同名的方法，在子类实例调用该方法时，实例调用的是子类中的覆盖版本的方法，这种现象叫做覆盖

- 子类对象显式调用基类方法的方式：
    - ```基类名.方法名(实例, 实际调用传参)```


```python
# 此示例示意覆盖的用法
class A:
    def work(self):
        print("A.work()被调用")

class B(A):
    '''B类继承自A类'''
    def work(self):  # 在这里覆盖了A类的work方法
        print("B.work()被调用")
    pass

b = B()
b.work()

a = A()
a.work()

b.__class__.__base__.work(b)
```

    B.work()被调用
    A.work()被调用
    A.work()被调用


## super 函数

super(type, obj) 返回绑定超类的实例  
super(  ) 返回绑定超类的实例，等同于```super(__class__, 实例方法的第一个参数)```（必须在方法内调用）


```python
# 此示例示意super函数来调用父类覆盖的用法
class A:
    def work(self):
        print("A.work()被调用")

class B(A):
    '''B类继承自A类'''
    def work(self):  
        print("B.work()被调用")
    
    def super_work(self):
        # self.work() # B.work()被调用
        
        # super(B, self).work() # A.work()被调用
        # super(__class__, self).work() # 在类内__class__可以直接用
        # super().work()
b = B()
super(B, b).work() # 调用超类
b.super_work()

```

    A.work()被调用
    A.work()被调用


## 显式调用基类的\_\_init\_\_初始化方法：
- 当子类中实现了`__init__`方法时，基类的`__init__`方法并不会被自动调用，此时需要显式调用


```python
# 此实例示意子类对象用super方法显式调用基类__init__方法
class Human:
    def __init__(self, n, a):
        '''此方法为人的对象添加，姓名和年龄属性'''
        self.name = n
        self.age = a
    
    def infos(self):
        print("姓名：", self.name)
        print("年龄：", self.age)

class Student(Human):
    def __init__(self, n, a, s):
        super().__init__(n, a)
        self.score = s
    
    def infos(self):
        super().infos()
        print("成绩：", self.score)
        
        
h1 = Human("小赵", 20)
h1.infos()

s1 = Student('小张', 18, 100)
s1.infos()
        

```

    姓名： 小赵
    年龄： 20
    姓名： 小张
    年龄： 18
    成绩： 100


## issubclass 判断派生子类

- 语法：  
    ```issubclass(cls, class_or_tuple)```  
     判断一个类是否继承自其他类，如果此类cls是class或tuple中的一个派生子类，则返回True，否则返回False
     
 
- 查看内建类的属性：`help(__builtins__)`


```python
class A:
    pass
class B(A):
    pass
class C(B):
    pass
print(issubclass(C, B))
print(issubclass(C, A))
print(issubclass(C, object))
print(issubclass(C, (int, str)))
print(issubclass(C, (int, str, A)))
```

    True
    True
    True
    False
    True


## enclosure 封装

- 封装是指隐藏类的实现细节，让使用者不用关心这些细节，封装的目的是让使用者尽可能少的实例变量（属性）进行操作
    - 私有属性：python类中，以双线划线'\_\_'开头，不以双下划线结尾的标识符为私有成员，以类的外部无法直接访问


```python
# 此示例示意使用私有属性和私有方法：
class A:
    def __init__(self):
        self.__p1 = 100 # __p1为私有属性，在类的外部不可调用
        
    def test(self):
        print(self.__p1)
        
    def __m1(self):
        print("我是A类的__m1方法")
        
a = A()
a.test()
a.__m1() # 在类调用不了__m1方法，访问失败
print(a.__p1) # 在类外看不到__p1属性，访问失败
```

    100



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-17-a71fa418a07d> in <module>
         12 a = A()
         13 a.test()
    ---> 14 a.__m1()
         15 print(a.__p1) # 在类外看不到__p1属性，访问失败


    AttributeError: 'A' object has no attribute '__m1'


## ploymorphic 多态

- 字面意思：“多种状态”


- 多态是指在继承/派生关系的类中，调用基类对象的方法，实际能调用子类的覆盖版本方法的现象叫多态


- 说明：
    - 多态调用的方法与对象相关，不与类型相关
    - Python的全部对象只有“运行时状态（动态）”，没有“C++/Java”里的编译时状态（静态）


```python
class Shape():
    def draw(self):
        print("Shape.draw被调用")
    
class Point(Shape):
    def draw(self):
        print("正在画一个点")

class Circle(Point):
    def draw(self):
        print("正在画一个圈")

def my_draw(s):
    s.draw() # 此处显示出多态的动态
    
# def my_draw(Circle s) # 在其他语言中，例如这样就是所谓的静态，在编译阶段规定类
#     s.draw()

s1 = Circle()
s2 = Point()
my_draw(s1)
my_draw(s2)
```

    正在画一个圈
    正在画一个点


## 编程语言的特征：
- 继承
- 封装
- 多态
    - 如：C++ / Java / Python / Swift / C#

## multiple inheritance 多继承

- 多继承是指一个子类继承自两个或两个以上的基类


- 只有C++和Python支持多继承


- 语法：  
`class 类名(基类名1, 基类名2, ...):
    语句块`


- 说明：
    - 一个子类同时继承自多个父类，父类中的方法可以同时被继承下来
    - 如果两个父类中有同名的方法，而在子类中由没有覆盖此方法时，调用结果难以确定


```python
# 此示例示意多继承的语句和使用
class Car:
    def run(self, speed):
        print("汽车以", speed, "公里/小时的速度行驶")

class Plane:
    def fly(self, height):
        print("飞机以海拔", height, "的高度飞行")

class PlaneCar(Car, Plane):
    pass

p1 = PlaneCar()
p1.fly(10000)
p1.run(50)
```

    飞机以海拔 10000 的高度飞行
    汽车以 50 公里/小时的速度行驶


- 缺陷：
    - 标识符（名字空间冲突问题）
        - 谨慎使用


```python
class A:
    def m(self):
        print("A.m()被调用")

class B:
    def m(self):
        print("B.m()被调用")
        
class AB(A, B):
    pass

ab = AB()
ab.m()
```

    A.m()被调用


## MRO ( Method Resolution Order) 问题
- 类内的\_\_mro\_\_属性用来记录继承方法的查找顺序


```python
# 此示例示意在多继承方法中的方法查找顺序问题
class A:
    def m(self):
        print("A.m")

class B(A):
    def m(self):
        print("B.m")
        super().m()
        
class C(A):
    def m(self):
        print("C.m")        
        
class D(B, C):
    def m(self):
        print("D.m")    
        super().m() ##
        
d = D()
print(D.__mro__)
d.m()
```

    (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    D.m
    B.m
    C.m

