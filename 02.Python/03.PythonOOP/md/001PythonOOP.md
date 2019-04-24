
# Python面向对象编程1
---

**什么是对象？**
- 对象是指现实中的物体或实体（拥有一系列变量、函数（方法）的）

**什么事面向对象？**
- 把一切看成对象（实例），让对象和对象之间建立关联关系

**对象都有什么特征？**
- 属性（名词）实例变量
    - 姓名、年龄、性别
- 行为（动作）实例方法
    - 学习、吃饭、睡觉

# class 类
---

**什么是类？**
- 拥有相同属性和行为的对象分为一组，即为一个类，类是用来描述对象的工具，用类可以创建同类对象

车（类） -------> BYD E6 (京A.88888） 实例  
---------------> BMW X5 （xxxxxx) 实例

狗（类） -------> 金毛犬 编号：007 实例  
----------------> 萨摩耶 编号：008 实例
         
类|对象|实例|
:-: | :-: | :-: |
class |object|instance|

## 类的创建


- 语法：

        class 类名(继承列表)
        '''类的文档字符串'''
        示例方法定义（类内的函数称为方法method)  
        类变量定义  
        类方法定义  
        静态方法定义



    
- 作用：


    - 创建一个类
    - 用于描述此类对象的行为和属性
    - 类用于创建此类的一个或多个对象（实例）


- 构造函数


    - 表达式：**类名**([创建传参列表])
    - 作用：创建这个类的实例对象，并返回此实例对象的引用关系

    
- 实例（对象）说明  

    - 实例有自己的作用域和名字空间，可以为该示例添加实例变量（属性）  
    - 示例可以调用类方法和示例方法  
    - 示例可以访问类和实例变量  



```python
class Dog: # 定义一个类，类名为Dog
    pass

dog1 = Dog() # 创建Dog类的对象
dog2 = Dog() # 创建Dog类的另一个对象

#类似如下语句：
int1 = int()
int2 = int()
```

### method 实例方法


- 语法：  
        class 类名(继承列表):
            def 实例方法名(self, 参数1, 参数2, ...)
            '''实例方法的文档字符串'''
            语句块

- 作用：
    - 用于描述一个对象的行为，让此类型的全部对象都拥有相同的行为


- 说明：
    - 实例方法实质是函数，是定义在类内的函数
    - 实例方法至少有一个形参，第一个形参代表调用这个方法的实例，一般命名为'self'


- 实例方法的调用语法：
        实例.实例方法名(调用传参)
        或
        类名.示例方法名(实例调用传参)


```python
class Dog:
    def eat(self, food):
        '''此方法用来描述小狗吃东西的行为'''
        print("小狗正在吃：", food)
        
    def sleep(self, hour):
        print("小狗睡了：", hour, "小时")
    
    def play(self, obj):
        print("小狗正在玩：", obj)
    
# 创建一个Dog的类的实例
dog1 = Dog()
dog1.eat("狗粮")
dog1.sleep(1)
dog1.play("球")

# 创建另一个Dog对象
dog2 = Dog()
dog2.play("飞盘")
# 可以用以下方法代替
Dog.play(dog2, "杂技")

dog2.sleep(2)
dog2.eat("骨头")
```

    小狗正在吃： 狗粮
    小狗睡了： 1 小时
    小狗正在玩： 球
    小狗正在玩： 飞盘
    小狗正在玩： 杂技
    小狗睡了： 2 小时
    小狗正在吃： 骨头


### attribute 实例属性（变量）

- 每个实例都可以有自己的变量，此变量称为实例变量（属性）


- 语法：
      实例.属性名

- 赋值规则：
    - 首次为属性赋值则创建此属性
    - 再次为属性赋值则改变属性的绑定关系
    
    
- 作用：
    - 用来记录对象自身的数据



```python
class Dog:
    def eat(self, food):
        print(self.color, '的',
              self.kinds, '正在吃', food)
    pass

# 创建第一个对象
dog1 = Dog()
dog1.kinds = '金毛' # 添加属性kinds
dog1.color = '白色' # 添加属性color
dog1.color = '黄色' # 改变属性color绑定关系
print(dog1.color, '的', dog1.kinds)

dog2 = Dog()
dog2.kinds = '萨摩耶'
dog2.color = '灰色'
print(dog2.color, '的', dog2.kinds)

dog1.eat("骨头")
dog2.eat("包子")
```

    黄色 的 金毛
    灰色 的 萨摩耶
    黄色 的 金毛 正在吃 骨头
    灰色 的 萨摩耶 正在吃 包子


- 删除属性
    - 用 del 语句可以删除一个对象的实例变量
    - 语法：
            del 对象.实例变量名


```python
class Cat:
    pass

c1 = Cat()
c1.color = '白色'
print(c1.color)
del c1.color
```

    白色


### 初始化方法

- 作用：
    - 对新创建的对象添加实例变量（属性）或相应的资源
    
    
- 语法：
        class 类名(继承列表):
            def \_\_init\_\_(self [,形参列表]):
                语句快

- 说明：
    1. 初始化方法名必须\_\_init\_\_不可变
    2. 初始化方法会在构造函数创建实例后自动调用，且将实例自身通过一个参数self传入\_\_init\_\_方法
    3. 创造函数的实参将通过\_\_init\_\_方法的形参列表传入\_\_init\_\_方法中
    4. 初始化方法内部如果需要返回则返回None


```python
# 此实例示意__init__方法的自助调用以及添加实例变量
class Car:
    def __init__(self, c, b, m):
        print('__init__方法被调用')
        self.color = c # 颜色
        self.brand = b # 品牌
        self.model = m # 型号
    
    def run(self, speed):
        print(self.color, '的',
              self.brand, self.model,
              '正在以', speed, '公里/小时的速度行驶！')
        
    def set_color(self, clr):
        '''此方法用来修改车的颜色信息'''
        self.color = clr

a4 = Car('红色', '奥迪', 'A4')
# a4.__init__(.....) 显示调用
print(a4.color)
a4.run(179)

a4.set_color('黑色')
a4.run(10)
```

    __init__方法被调用
    红色
    红色 的 奥迪 A4 正在以 179 公里/小时的速度行驶！
    黑色 的 奥迪 A4 正在以 10 公里/小时的速度行驶！


### 析构方法

- 语法：
        class 类名(继承列表):
            def __del__(self):
                语句块

- 说明：
    - 析构方法在对象销毁时被自动调用
    

- 作用：
    - 清理此对象占用的资源
    
*Python不建议在析构方法内做任何事情，因为对象销毁的时间难以确定*
    


```python
class Car:
    def __init__(self, name):
        self.name = name
        print('汽车', name, '对象已经创建！')
    
    def __del__(self):
        print(self.name, "对象已经销毁")

c1 = Car('BYD E6')
c1 = Car('BMW x5')
```

    汽车 BYD E6 对象已经创建！
    BMW x5 对象已经销毁
    汽车 BMW x5 对象已经创建！
    BYD E6 对象已经销毁


### 预置实例属性

- \_\_dict\_\_ 属性
    - 此属性绑定一个储存此实例自身实例变量的字典


```python
class Dog:
    pass
print(dog1.__dict__)
dog1.kinds = '金毛'
print(dog1.__dict__)
```

    {'kinds': '金毛', 'color': '黄色'}
    {'kinds': '金毛', 'color': '黄色'}


- \_\_class\_\_ 属性
    - 此属性绑定创建此实例的类


- 作用：
    - 可以借助此属性来访问创建此实例的类


```python
class Dog:
    pass
dog1 = Dog()
dog2 = Dog()
dog3 = dog1.__class__()
dog3.__class__ is Dog
```




    True



### 面向对象的综合示例

有两个人：  
1.
    - 姓名：张三
    - 年龄：35  
2.
    - 姓名：李四
    - 年龄：38

行为：
    1. 教别人学东西 teach
    2. 赚钱
    3. 借钱

事情：
    - 张三 教 李四 学 Python  
    - 李四 教 张三 学 跳皮筋
    - 张三 上班赚了 1000元  
    - 李四向张三借了200元


```python
# 此示例示意如何用面向对象的方式创建对象，
# 并建立对象与对象之间的逻辑关系

class Human:
    '''人类，用于描述人的行为'''
    def __init__(self, n, a):
        self.name = n
        self.age = a
        self.money = 0
        
    def teach(self, other, skill):
        print(self.name, '教', other.name, '学', skill)
    
    def works(self, money):
        self.money += money
        print(self.name, '工作赚了', money, '元钱')
        
    def borrow(self, other, money):
        if other.money > money:
            print(other.name, '借给', self.name, money, '元钱')
            other.money -= money
            self.money += money
        else:
            print(other.name, '不借给', self.name)
    
    def show_info(self):
        print(self.age, '岁的', self.name, '存有', self.money, '元钱')

# 以下的类的使用
zhang3 = Human('张三', 35)
li4 = Human('李四', 8)
zhang3.teach(li4, 'Python')
li4.teach(zhang3, '跳皮筋')

zhang3.works(1000)
li4.borrow(zhang3, 200)
zhang3.show_info()
```

    张三 教 李四 学 Python
    李四 教 张三 学 跳皮筋
    张三 工作赚了 1000 元钱
    张三 借给 李四 200 元钱
    35 岁的 张三 存有 800 元钱


### 用于类的函数

- isinstance(obj, class_or_tuple)
    - 返回这个对象obj是否某个类class或某类的实例，如果是则返回True，否则返回Flase
    - type(obj) 返回对象类型


```python
class Dog:
    pass
class Cat:
    pass
animal = Dog()
isinstance(animal, Dog) # T
isinstance(animal, Cat) # F
isinstance(animal, (Cat, int, list)) # F
isinstance(animal, (Cat, int, Dog)) # T
```




    True



## class attribute 类的变量

- 类变量是类的属性，此属性属于类  


- 作用：
    - 用来记录类相关对的数据

   
- 说明：
    - 类变量可以通过类直接访问
    - 类变量可以通过类的实例直接访问
    - 类变量可以通过此类的实例__class__属性简介访问


```python
# 此示例表示类变量的定义和使用
class Human:
    count = 0 # 创建一个类变量
    
print("Human的类变量count=", Human.count)
Human.count = 100
print("Human的类变量count=", Human.count)


class Human:
    count = 0
    
h1 = Human()
print("用h1对象访问的类变量count=", h1.count)
h1.count = 100
print("用h1对象访问的类变量count=", h1.count, "但是Human的类变量还是", Human.count)

h1.__class__.count += 1
print("用h1对象访问的类变量还是count=", h1.count, "但是Human的类变量变了", Human.count)
```

    Human的类变量count= 0
    Human的类变量count= 100
    用h1对象访问的类变量count= 0
    用h1对象访问的类变量count= 100 但是Human的类变量还是 0
    用h1对象访问的类变量还是count= 100 但是Human的类变量变了 1



```python
# 此示例示意用类变量来记录对象的个数
class Car:
    count = 0 # 创建类变量，用来记录汽车对象的总数
    def __init__(self, info):
        print(info, '被创建')
        self.data = info # 记录传入数据
        self.__class__.count += 1 # 让车的总数加1
    
    def __del__(self):
        print(self.data, '被销毁')
        self.__class__.count -= 1 # 当车被销毁总数减1

b1 = Car("BYD")
b2 = Car("TTESLA")
b3 = Car("AUDI")
print("当前汽车总数是", Car.count)
del b3
print("当前汽车总数是", Car.count)
```

    BYD 被创建
    BYD 被销毁
    TTESLA 被创建
    TTESLA 被销毁
    AUDI 被创建
    当前汽车总数是 3
    AUDI 被销毁
    当前汽车总数是 2


## 类的文档字符串

- 类内第一个没有赋值给任何变量的字符串是类的文档字符串


- 说明：
    - 类的文档字符串用类的 \_\_doc\_\_ 属性可以访问
    - 类的文档字符串可以用help()函数查看


```python
class Car:
    '''此类用来描述车的对象的行为
    这是Car类的文档字符串'''
    def run(self, speed):
        '''车的run方法'''
        pass

help(Car)
Car.__doc__
```

    Help on class Car in module __main__:
    
    class Car(builtins.object)
     |  此类用来描述车的对象的行为
     |  这是Car类的文档字符串
     |  
     |  Methods defined here:
     |  
     |  run(self, speed)
     |      车的run方法
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    





    '此类用来描述车的对象的行为\n    这是Car类的文档字符串'



## 类的\_\_slots\_\_列表

- 作用：
    - 限定一个类的实例只能有固定的属性（实例变量）
    - 通常为防止错写属性名而发生运行时错误
    
    
- 说明：
    - 含有\_\_slots\_\_列表的类创建的实例对象没有\_\_dict\_\_属性，即此实例不用字典来保存对象的属性（实例变量）


```python
# 此示例示意类的__slots__列表的作用
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student('小张', 58)
print(s1.score)
s1.socre = 100 # 此处错写了属性名！但运行时不报错！
print(s1.socre) # 这里打印出了第三个属性

class Student:
    __slots__ = ['name', 'score']
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student('小张', 58)
print(s1.score)
s1.socre = 100 # 此处出错，是因为已经用slots限定了变量
```

    58
    100
    58



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-19-5cac1bf3ae50> in <module>
         18 s1 = Student('小张', 58)
         19 print(s1.score)
    ---> 20 s1.socre = 100 # 此处错写了属性名！但运行时不报错！
         21 print(s1.socre) # 这里打印出了第三个属性


    AttributeError: 'Student' object has no attribute 'socre'


## @classmethod 类方法

- 类方法是描述类的行为的方法，类方法属于类


- 说明：
    - 类方法需要用@classmethod装饰器定义
    - 类方法至少有一个形参，第一个形参用于绑定类，预定写为'cls'
    - 类和该类的实例都可以调用类方法
    - 类方法不能访问此类创建的实例的属性（只能访问类变量）


```python
# 此示例示意类方法的定义方法和用法
class Car:
    count = 0
    
    @classmethod
    def getTotalCount(cls):
        '''此方法为类方法，
        第一个参数为cls，代编调用此方法的类'''
        return cls.count
    
    @classmethod
    def updateCount(cls, number):
        cls.count += number

print(Car.getTotalCount()) # 用类来调用类方法
#Car.count += 1 # 面向对象思想不提倡直接操作属性
Car.updateCount(1)
print(Car.getTotalCount()) 

c1 = Car()
c1.updateCount(100) # Car类的实例也可以调用类方法
print(c1.getTotalCount()) # 101
```

    0
    1


## @staticmethod 静态类方法

- 静态方法不属于类，也不属于类的实例，它相当于定义在类内普通函数，知识他的作用域属于类


```python
# 此示例示意静态方法的创建和使用
class A:
    
    @staticmethod
    def myadd(x, y):
        '''此方法为静态方法
        此方法的形参不需要传入类或实例'''
        return x+y
    
print('1+2=', A.myadd(1, 2))
a = A()
print('100+200=', a.myadd(100, 200))
```

    1+2= 3
    100+200= 300

