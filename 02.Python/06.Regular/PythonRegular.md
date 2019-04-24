
# 正则表达式

- 动机
    - 文本处理已经成为计算机的常见工作之一
    - 对文本内容的搜索，定位，提取是逻辑比较复杂的工作
    - 为了快速解决上述问题，产生了正则表达式技术
- 定义
    - 即文本的高级匹配模式，提供搜索，替代等功能。其本质是一系列由特殊符号组成的字串，这个字串即正则表达式。
- 匹配原理
    - 由普通字符和特殊符号组成字符串，通过描述字符的重复和位置等行为，达到匹配某一类字符串的目的
- 目标
    1. 熟练掌握正则表达式符号
    2. 实现基本的文本搜索，定位，提取，理解正则用法
    3. 能够适用re模块操作正则表达式
- 特点
    - 方便文本处理
    - 支持语言众多
    - 使用灵活多样

## re模块 

- `re.findall(pattern, string)`
    - 功能：使用正则表达式匹配目标字符串内容
    - 参数：
        - pattern  正则表达式
        - string   目标字符串
    - 返回值：列表，列表中为匹配到的内容

## 元字符的使用

### 1. 普通字符
- 元字符：a b c...
- 匹配规则：每个字符匹配对应的字符


```python
import re
re.findall("hello", "hello world")
```




    ['hello']




```python
re.findall("您好", "您好北京")
```




    ['您好']



### 2. 或
- 元字符：|
- 匹配规则：匹配 | 两边任意一个正则表达式


```python
print(re.findall("ab|cd", "abcdefghijk"))
print(re.findall("abc|cde", "abcdefghijk")) # 不匹配已经匹配过的
```

    ['ab', 'cd']
    ['abc']


### 3. 匹配单个字符
- 元字符：  . 
- 匹配规则：匹配除换行外的任意字符  
f.o --> foo  fao  f@o  f o


```python
re.findall("f.o", "foo is not fao f o f@o")
```




    ['foo', 'fao', 'f o', 'f@o']



### 4. 匹配开始位置
- 元字符 ： ^ 
- 匹配规则：匹配目标字符串的开头位置


```python
re.findall("^Tom", "Tom is a boy")
```




    ['Tom ']



### 5. 匹配结束位置
- 元字符 ： $
- 匹配规则：匹配字符串的结束位置


```python
re.findall("boy$", "Tom is a boy")
```




    ['boy']



### 6. 匹配重复
- 元字符 ： * 
- 匹配规则：匹配前面的字符出现**0次或多次**  
fo*  --> fooooooooo  f  fo


```python
re.findall("fo*", "fadsfafooooafo") # 匹配o出现0次或多次
```




    ['f', 'f', 'foooo', 'fo']



### 7. 匹配重复
- 元字符： +
- 匹配规则：匹配前面的字符出现**1次或多次**  
fo+  --> fo   fooooo


```python
re.findall("fo+", "fadsfafooooafo")
```




    ['foooo', 'fo']



### 8. 匹配重复
- 元字符：？
- 匹配规则：匹配前面的字符出现**0次或1次**  
fo? -->  f   fo


```python
re.findall("fo?", "fadsfafooooafo")
```




    ['f', 'f', 'fo', 'fo']



### 9. 匹配重复{n}
- 元字符 ： {n}
- 匹配规则： 匹配指定的重复次数  
fo{3}  --> fooo


```python
re.findall("fo{2}", "fadsfafooooafo")
```




    ['foo']



### 10. 匹配重复{m,n}
- 元字符： {m,n}
- 匹配规则：匹配前面的正则表达式 m--n次  
fo{2,4} --> foo  fooo  foooo


```python
re.findall("fo{2,4}", "fadsfafooooafoo")
```




    ['foooo', 'foo']



>匹配所用字符表达为：.+或.*

### 11. 匹配字符集合
- 元字符： [字符集]
- 匹配规则： 匹配任意一个字符集中的字符
        [abc123]   a  b  c  1  2  3 
        [a-z]  
        [A-Z]
        [0-9]
        [_123a-z]


```python
re.findall("[A-Z][a-z]*", "Boy")
```




    ['Boy']



### 12. 匹配字符集（非）
- 元字符 ： [^...]
- 匹配规则 ：字符集取非，除列出的字符之外任意一个字符
        [^abc] --> 除a b  c之外任意字符


```python
re.findall("[^ ]+", "a little boy")
```




    ['a', 'little', 'boy']



### 13.  匹配任意数字字符
- 元字符 ： \d   \D
- 匹配规则： 
        \d 匹配任意数字字符     [0-9]
        \D 匹配任意非数字字符   [^0-9]


```python
re.findall("1\d{10}", "17857024541")
```




    ['17857024541']



### 14. 匹配任意（非）普通字符
- 元字符 ： \w   \W
- 匹配规则：
        \w 普通字符  [_0-9a-zA-Z] 也能匹配普通汉字
        \W 非普通字符


```python
re.findall("\w+", "hello#nihao%adsd@afsd!df&")
```




    ['hello', 'nihao', 'adsd', 'afsd', 'df']




```python
re.findall("\W+","hello#nihao%asdf@adsgdfg!df&")
```




    ['#', '%', '@', '!', '&']



### 15. 匹配任意（非）空字符
- 元字符： 
        \s  匹配任意空字符  [空格 \r\t\n\v\f]
        \S  匹配任意非空字符


```python
re.findall("\w+\s+\w+", "hello    world")
```




    ['hello    world']




```python
re.findall("\S+", "hello this is tom")
```




    ['hello', 'this', 'is', 'tom']



### 16.  匹配字符串位置
- 元字符 ： \A   \Z
- 匹配规则： 
        \A 匹配字符串开头位置  ^
        \Z 匹配字符串结尾位置  $ 
        
>绝对匹配：正则表达式要完全匹配目标字符串内容
    - 在正则表达式开始和结束位置加上^ $ (或者\A \Z)。这样正则表达式必须匹配整个目标字符串才会有结果



```python
re.findall("\A\d+\Z","123445")
```




    ['123445']



### 17. 匹配（非）单词边界
- 元字符： \b   \B
- 匹配规则：
        \b 匹配单词边界位置  
        普通字符和非普通字符交界认为是单词边界
        \B 匹配非单词边界位置


```python
re.findall(r"num\b", "num#asdf#")
```




    ['num']




```python
re.findall(r"num\b", "numasdf#")
```




    []



    元字符总结  
    匹配单个字符 ： a   .   \d  \D  \w  \W  \s  \S
                    [...]  [^...]
    匹配重复 ： *   +  ?  {n}  {m,n}

    匹配位置 ： ^  $  \A  \Z   \b  \B 

    其他 ： |  ()  \

## 正则表达式转义

- 正则中的特殊符号：
        .  *  +  ?  ^  $  []  {}   ()  |  \

- 正则表达式如果匹配特殊字符需要加 \ 表达转义

             正则          目标字符串
        e.g.    \$\d+  ---->    $10

                 pattern        string
        python  "\\$\\d+"       "$10" 

        raw     r"\$\d+"       "$10" 

        raw字串 ： 原始字符串对内容不解释转义，就表达内容原本意义

## 贪婪与非贪婪

- 贪婪模式 ： 正则表达式的重复匹配总是尽可能多的向后匹配更多内容

        *   +   ？  {m,n}

- 非贪婪（懒惰模式） ： 尽可能少的匹配内容

贪婪 ---> 非贪婪  *？  +？  ??  {m,n}?


```python
re.findall(r"ab+?", "abbbbbbbb")
```




    ['ab']




```python
re.findall(r"ab??", "abbbbbbbb")
```




    ['a']



## 正则表达式的子组
- 可以使用()为正则表达式建立子组，子组可以看做是正则表达式内部操作的一个整体
* 子组是在正则表达式**整体匹配到内容的前提下**才会发挥作用，它不影响正则表达式整体去匹配目标内容这一原则


### 子组所用

1. 作为内部整体可以改变某些元字符的行为
       re.search(r"(ab)+\d+","ababab1234").group()
       'ababab1234'

        re.search(r"\w+@\w+\.(com|cn)","abc@123.com").group()
        'abc@123.com'

2. 子组在某些操作中可以单独提取出匹配内容
        re.search(r"(https|http|ftp)://\S+","https://www.baidu.com").group(1)
        Out[121]: 'https'

### 子组使用注意事项

* 一个正则表达式中可以有多个子组
* 子组一般由外到内，由左到右称之为第一，第二 第三。。。。子组
* 子组不能重叠，嵌套也不宜很多

### 捕获组 和 非捕获组

- 格式：`（?P<name>pattern）`
        e.g.
         re.search(r"(?P<dog>ab)cdef",'abcdefghti').group('dog')
        Out[130]: 'ab'
- 作用 ： 可以通过组名更方便获取某组内容

# 正则表达式设计原则

1. 正确性 ，能正确匹配到目标内容
2. 排他性 ，除了要匹配的内容，尽可能不会匹配与到其他内容
3. 全面性 ，需要对目标的各种情况进行考虑，做到不遗漏

    regex = compile(pattern,flags = 0)
    功能 ： 生成正则表达式对象
    参数 ： pattern  正则表达式
            flags  功能标志位，丰富正则表达式的匹配功能
    返回值 : 返回正则表达式对象

    re.findall(pattern,string,flags)
    功能 ：从目标字符串查找正则匹配内容
    参数 ： pattern  正则表达式
            string  目标字符串
        flags  标志位
    返回值 ： 返回匹配到的内容
              如果正则有子组则只返回子组对应内容

    regex.findall(string,pos,endpos)
    功能 ：从目标字符串查找正则匹配内容
    参数 ： string  目标字符串
            pos  匹配目标的起始位置
            endpos  匹配目标的终止位置
    返回值 ： 返回匹配到的内容
              如果正则有子组则只返回子组对应内容

    re.split(pattern,string,flags = 0)
    功能：根据正则匹配内容切割字符串
    参数： pattern  string  flags
    返回值： 返回列表，列表中为切割的内容

    re.sub(pattern,replaceStr,string,max,flags)
    功能： 替换正则匹配到的目标子串部分
    参数： pattern
           replaceStr ： 要替换的内容
           string 
           max   最多替换几处 默认全部替换
           flags
    返回值 ： 返回替换后的字符串

    re.subn(pattern,replaceStr,string,max,flags)
    功能： 替换正则匹配到的目标子串部分
    参数： pattern
           replaceStr ： 要替换的内容
           string 
           max   最多替换几处 默认全部替换
           flags
    返回值 ： 返回一个元组，为实际替换了几处和替换后的字符串


    re.finditer(pattern,string,flags)
    功能： 使用正则表达式匹配目标字符串
    参数： pattern  string flags
    返回值： 返回一个迭代对象，迭代到的内容是一个match对象

    fullmatch(pattern,string,flags)
    功能： 完全匹配目标字符串
    参数： pattern,string,flags
    返回值：返回匹配到的match对象
            如果没匹配成功返回None

    match(pattern,string,flags)
    功能： 从开头位置匹配目标字符串
    参数： pattern,string,flags
    返回值：返回匹配到的match对象
            如果没匹配成功返回None


    search(pattern,string,flags)
    功能： 正则表达式匹配目标字符串，只匹配第一处
    参数： pattern,string,flags
    返回值：返回匹配到的match对象
            如果没匹配成功返回None

    compile对象属性：

    flags  ： 标志位
    pattern ： 正则表达式
    groups： 有多少子组
    groupindex ： 捕获组形成组名和序列号的字典
                  组名为键，第几组为值


```python
pattern = r"(ab)cd(ef)"
s = "abcdefghigkabcdef"

#re模块直接调用
l = re.findall(pattern,s)
print(l)

#compile对象调用
regex = re.compile(pattern)
l = regex.findall(s)
print(l)
print("==================================")

l = re.split(r"\s+","Hello  world nihao China")
print("split():",l)

s = re.sub(r"\s+","#",'Hello  world     nihao China',2)
print("sub():",s)

s = re.subn(r"\s+","#",'Hello  world     nihao China')
print("subn():",s)
```

    [('ab', 'ef'), ('ab', 'ef')]
    [('ab', 'ef'), ('ab', 'ef')]
    ==================================
    split(): ['Hello', 'world', 'nihao', 'China']
    sub(): Hello#world#nihao China
    subn(): ('Hello#world#nihao#China', 3)



```python
import re 

it = re.finditer(r'\d+',"2008-2018 10年，\
    中国发生了翻天覆地的变化")

for i in it:
    print(i.group())


#fullmatch
try:
    obj = re.fullmatch(r"\w+",'abcdef123')
    print(obj.group())
except AttributeError as e:
    print(e)

#match
obj = re.match(r'foo',"foo,food on the table")
print(obj.group())

#search
obj = re.search(r'foo',"Foo,food on the table")
print(obj.group())
```

    2008
    2018
    10
    abcdef123
    foo
    foo


## match对象属性

- 属性变量
    - pos     匹配目标字符串的开始位置
    - endpos  匹配目标字符串的结束位置
    - re      正则表达式
    - string  目标字符串
    - lastgroup  最后一组的组名
    - lastindex  最后一组是第几组
- 属性方法
    - span()  匹配内容的开始位置
    - start() 匹配内容的结束位置
    - end()   匹配内容的起止位置

### group()
- 功能 ： 获取match对象对应的内容
- 参数 ： 默认为0 表示获取整个正则匹配的内容
        如果为序列号或者子组名则为获取某个子组匹配的对应内容
- 返回值：返回得到的子串

### groupdict()  获取捕获组名作为键，对应内容作为值的字典
### groups()   获取每个子组匹配内容


```python
import re 

pattern = r"(?P<dog>ab)cd(?P<pig>ef)"
regex = re.compile(pattern)

#获取match对象
match_obj = regex.search("abcdefghij",pos = 0,endpos = 6)

print(match_obj.pos)  #匹配目标字符串的开始位置
print(match_obj.endpos) #匹配目标字符串的结束位置
print(match_obj.re)     #正则表达式
print(match_obj.string) #目标字符串
print(match_obj.lastgroup) #最后一组的组名
print(match_obj.lastindex) #最后一组是第几组
print("=============================")

print(match_obj.start())  #匹配内容的开始位置
print(match_obj.end())    #匹配内容的结束位置
print(match_obj.span())   #匹配内容的起止位置

print(match_obj.group(0)) #获取整个match对象内容
print(match_obj.group(2)) #获取第二个子组匹配内容
print(match_obj.group('dog')) #获取dog子组匹配内容

print(match_obj.groupdict()) #获取捕获组字典
print(match_obj.groups())  #获取每个子组匹配内容
```

    0
    6
    re.compile('(?P<dog>ab)cd(?P<pig>ef)')
    abcdefghij
    pig
    2
    =============================
    0
    6
    (0, 6)
    abcdef
    ef
    ab
    {'dog': 'ab', 'pig': 'ef'}
    ('ab', 'ef')


## flags  参数的使用
    re.compile  re.findall  re.search  re.match
    re.finditer  re.fullmatch  re.sub  re.subn  re.split

- 作用 ： 辅助正则表达式，丰富匹配结果
        I ==  IGNORECASE  匹配时忽略字母的大小写
        S ==  DOTALL     作用于元字符 . 使其可以匹配换行 
        M ==  MULTILINE  作用于^  $  使其可以匹配每一行开头结尾位置
        X ==  VERBOSE    可以给正则添加注释
        使用多个标志位使用按位或连接
        e.g.
        flags = re.X | re.I


```python
import re 

s = '''hello world
hello kitty
你好,北京'''

pattern = r'''H\w+  #匹配第一个单词
\s+    #匹配多个空格
[a-z]+ #匹配其他
'''

regex = re.compile(pattern,flags = re.X | re.I)

try:
    s = regex.search(s).group()
except:
    print("没有匹配到内容")
else:
    print(s)
```

    hello world

