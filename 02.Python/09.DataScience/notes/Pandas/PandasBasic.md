
# Pandas对象


```python
import numpy as np
import pandas as pd
```

## 1. Series对象

带有**索引数据**的一维数组


```python
data = pd.Series([0.25, 0.5, 0.75, 1.0])
data
```




    0    0.25
    1    0.50
    2    0.75
    3    1.00
    dtype: float64



从上面看出，数据和索引（第一列）绑定在一起


```python
# values属性返回数据值
data.values
```




    array([0.25, 0.5 , 0.75, 1.  ])




```python
# index属性返回pd.Index索引对象
data.index
```




    RangeIndex(start=0, stop=4, step=1)



通过括号索引标签取值


```python
data[1]
```




    0.5




```python
data[1:3]
```




    1    0.50
    2    0.75
    dtype: float64



### (1)用字符串定义索引

Numpy数组是通过隐式定义的整数索引获取值

Series对象是一种显式定义的索引与数值关联


```python
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
data
```




    a    0.25
    b    0.50
    c    0.75
    d    1.00
    dtype: float64




```python
data['b']
```




    0.5



可以使用不连续的索引


```python
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[2, 5, 3, 7])
data
```




    2    0.25
    5    0.50
    3    0.75
    7    1.00
    dtype: float64




```python
data[5]
```




    0.5



### (2)Series作为特殊的字典


```python
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
population
```




    California    38332521
    Texas         26448193
    New York      19651127
    Florida       19552860
    Illinois      12882135
    dtype: int64



索引按照顺序排列，字典取值方法也可用


```python
population['California']
```




    38332521



还可以切片！


```python
population['California':'Illinois']
```




    California    38332521
    Texas         26448193
    New York      19651127
    Florida       19552860
    Illinois      12882135
    dtype: int64



### (3)创建Series对象

```python
>>> pd.Series(data, index=index)
```


```python
# 可以是列表
pd.Series([2, 4, 6])
```




    0    2
    1    4
    2    6
    dtype: int64




```python
# 可以是标量，会进行自动填充
pd.Series(5, index=[100, 200, 300])
```




    100    5
    200    5
    300    5
    dtype: int64




```python
# 可以是字典
pd.Series({2:'a', 1:'b', 3:'c'})
```




    2    a
    1    b
    3    c
    dtype: object




```python
# Series只会保留显式定义的键值对
pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])
```




    3    c
    2    a
    dtype: object



## 2. DataFrame对象

### (1)DataFrame作为通用的数组

按照共同的索引排列的若干个Series对象


```python
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'Illinois': 149995}
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
area = pd.Series(area_dict)
population = pd.Series(population_dict)

states = pd.DataFrame({'population': population, 'area': area})
states
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>population</th>
      <th>area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>38332521</td>
      <td>423967</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>26448193</td>
      <td>695662</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>19651127</td>
      <td>141297</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>19552860</td>
      <td>170312</td>
    </tr>
    <tr>
      <th>Illinois</th>
      <td>12882135</td>
      <td>149995</td>
    </tr>
  </tbody>
</table>
</div>



DataFrame也有一个index属性可以获取索引标签


```python
states.index
```




    Index(['California', 'Texas', 'New York', 'Florida', 'Illinois'], dtype='object')



DataFrame的colums属性存放列标签的Index对象


```python
states.columns
```




    Index(['population', 'area'], dtype='object')



可以看作通用的Numpy二维数组，他的行和列可以通过索引获取

### (2)DataFrame作为特殊的字典


```python
states['area']
```




    California    423967
    Texas         695662
    New York      141297
    Florida       170312
    Illinois      149995
    Name: area, dtype: int64



DataFrame中，``data['col0']``，只返回第一列，和NumpyArray不同

### (3)创建DataFrame对象

#### (1)通过单个Series对象创建


```python
pd.DataFrame(population,columns=['population'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>38332521</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>26448193</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>19651127</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>19552860</td>
    </tr>
    <tr>
      <th>Illinois</th>
      <td>12882135</td>
    </tr>
  </tbody>
</table>
</div>



#### (2)通过字典列表创建


```python
data = [{'a': i, 'b': 2 * i}
        for i in range(3)]
pd.DataFrame(data)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



即使某些键不存在，也会用NaN表示(Not a Number)


```python
pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>3</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



#### (3)通过Series对象字典创建


```python
pd.DataFrame({'population': population, 'area': area})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>population</th>
      <th>area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>38332521</td>
      <td>423967</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>26448193</td>
      <td>695662</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>19651127</td>
      <td>141297</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>19552860</td>
      <td>170312</td>
    </tr>
    <tr>
      <th>Illinois</th>
      <td>12882135</td>
      <td>149995</td>
    </tr>
  </tbody>
</table>
</div>



#### (4)通过NumpyArray创建


```python
pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar'], index=['a', 'b', 'c'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>foo</th>
      <th>bar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.739644</td>
      <td>0.629162</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.955598</td>
      <td>0.154161</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.180660</td>
      <td>0.552287</td>
    </tr>
  </tbody>
</table>
</div>



#### (5)通过Numpy结构化数组


```python
A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
A
```




    array([(0, 0.), (0, 0.), (0, 0.)], dtype=[('A', '<i8'), ('B', '<f8')])




```python
pd.DataFrame(A)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



## 2. Index对象

**不可变数组**和**有序集合**


```python
ind = pd.Index([2, 3, 5, 7, 11])
ind
```




    Int64Index([2, 3, 5, 7, 11], dtype='int64')



### Index看作不可变数组

操作类似于数组


```python
ind[1]
```




    3




```python
ind[::2]
```




    Int64Index([2, 5, 11], dtype='int64')



有很多类似Numpy的属性


```python
print(ind.size, ind.shape, ind.ndim, ind.dtype)
```

    5 (5,) 1 int64


区别在于，Index对象不可变，无法修改

### 看作有序集合

有set的用法


```python
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])
```


```python
indA & indB  # intersection交集
```




    Int64Index([3, 5, 7], dtype='int64')




```python
indA | indB  # union并集
```




    Int64Index([1, 2, 3, 5, 7, 9, 11], dtype='int64')




```python
indA ^ indB  # symmetric difference异或
```




    Int64Index([1, 2, 9, 11], dtype='int64')



也可以调用方法``indA.intersection(indB)``.

# 取值

## 1. Series取值

### (1)Series看作字典


```python
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
data
```




    a    0.25
    b    0.50
    c    0.75
    d    1.00
    dtype: float64




```python
data['b']
```




    0.5



检测键/索引/值


```python
'a' in data
```




    True




```python
data.keys()
```




    Index(['a', 'b', 'c', 'd'], dtype='object')




```python
list(data.items())
```




    [('a', 0.25), ('b', 0.5), ('c', 0.75), ('d', 1.0)]




```python
# 修改数据
data['e'] = 1.25
data
```




    a    0.25
    b    0.50
    c    0.75
    d    1.00
    e    1.25
    dtype: float64



### (2)Series看作一维数组


```python
# 显式索引切片
data['a':'c']
```




    a    0.25
    b    0.50
    c    0.75
    dtype: float64




```python
# 隐式索引切片
data[0:2]
```




    a    0.25
    b    0.50
    dtype: float64




```python
# 掩码
data[(data > 0.3) & (data < 0.8)]
```




    b    0.50
    c    0.75
    dtype: float64




```python
# 花哨
data[['a', 'e']]
```




    a    0.25
    e    1.25
    dtype: float64



显式：包含最后一个

隐式：不包含最后一个

### 索引器: loc, iloc, and ix

如果Series是显式整数索引，则``data[1]``取值为显式索引

而``data[1:3]``为隐式索引


```python
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
data
```




    1    a
    3    b
    5    c
    dtype: object




```python
# 显式
data[1]
```




    'a'




```python
# 隐式
data[1:3]
```




    3    b
    5    c
    dtype: object



担心混淆，所以使用索引器


```python
# 显式
data.loc[1]
```




    'a'




```python
# 显式
data.loc[1:3]
```




    1    a
    3    b
    dtype: object




```python
# 隐式
data.iloc[1]
```




    'b'




```python
# 隐式
data.iloc[1:3]
```




    3    b
    5    c
    dtype: object



``ix``为混合

## DataFrame取值

### (1)DataFrame看作字典


```python
area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>area</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>423967</td>
      <td>38332521</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>170312</td>
      <td>19552860</td>
    </tr>
    <tr>
      <th>Illinois</th>
      <td>149995</td>
      <td>12882135</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>141297</td>
      <td>19651127</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>695662</td>
      <td>26448193</td>
    </tr>
  </tbody>
</table>
</div>




```python
data['area']
```




    California    423967
    Florida       170312
    Illinois      149995
    New York      141297
    Texas         695662
    Name: area, dtype: int64




```python
data.area
```




    California    423967
    Florida       170312
    Illinois      149995
    New York      141297
    Texas         695662
    Name: area, dtype: int64




```python
data.area is data['area']
```




    True



若列名与DataFrame的方法同名的话，不能获取，并且避免用属性形式直接修改值


```python
data.pop is data['pop']
```




    False




```python
# 增加新的变量
data['density'] = data['pop'] / data['area']
data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>area</th>
      <th>pop</th>
      <th>density</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>423967</td>
      <td>38332521</td>
      <td>90.413926</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>170312</td>
      <td>19552860</td>
      <td>114.806121</td>
    </tr>
    <tr>
      <th>Illinois</th>
      <td>149995</td>
      <td>12882135</td>
      <td>85.883763</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>141297</td>
      <td>19651127</td>
      <td>139.076746</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>695662</td>
      <td>26448193</td>
      <td>38.018740</td>
    </tr>
  </tbody>
</table>
</div>



### (2)DataFrame看作二维数组


```python
# 查看数组数据
data.values
```




    array([[  4.23967000e+05,   3.83325210e+07,   9.04139261e+01],
           [  1.70312000e+05,   1.95528600e+07,   1.14806121e+02],
           [  1.49995000e+05,   1.28821350e+07,   8.58837628e+01],
           [  1.41297000e+05,   1.96511270e+07,   1.39076746e+02],
           [  6.95662000e+05,   2.64481930e+07,   3.80187404e+01]])




```python
# 进行转制
data.T
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>California</th>
      <th>Florida</th>
      <th>Illinois</th>
      <th>New York</th>
      <th>Texas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>area</th>
      <td>4.239670e+05</td>
      <td>1.703120e+05</td>
      <td>1.499950e+05</td>
      <td>1.412970e+05</td>
      <td>6.956620e+05</td>
    </tr>
    <tr>
      <th>pop</th>
      <td>3.833252e+07</td>
      <td>1.955286e+07</td>
      <td>1.288214e+07</td>
      <td>1.965113e+07</td>
      <td>2.644819e+07</td>
    </tr>
    <tr>
      <th>density</th>
      <td>9.041393e+01</td>
      <td>1.148061e+02</td>
      <td>8.588376e+01</td>
      <td>1.390767e+02</td>
      <td>3.801874e+01</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.values[0]
```




    array([  4.23967000e+05,   3.83325210e+07,   9.04139261e+01])




```python
# 隐式：从0开始，左闭右开
data.iloc[:3, :2]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>area</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>423967</td>
      <td>38332521</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>170312</td>
      <td>19552860</td>
    </tr>
    <tr>
      <th>Illinois</th>
      <td>149995</td>
      <td>12882135</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 显式
data.loc[:'Illinois', :'pop']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>area</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>423967</td>
      <td>38332521</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>170312</td>
      <td>19552860</td>
    </tr>
    <tr>
      <th>Illinois</th>
      <td>149995</td>
      <td>12882135</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 混合
data.ix[:3, :'pop']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>area</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>423967</td>
      <td>38332521</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>170312</td>
      <td>19552860</td>
    </tr>
    <tr>
      <th>Illinois</th>
      <td>149995</td>
      <td>12882135</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 结合花哨
data.loc[data.density > 100, ['pop', 'density']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pop</th>
      <th>density</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Florida</th>
      <td>19552860</td>
      <td>114.806121</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>19651127</td>
      <td>139.076746</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 修改数据
data.iloc[0, 2] = 90
data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>area</th>
      <th>pop</th>
      <th>density</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>423967</td>
      <td>38332521</td>
      <td>90.000000</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>170312</td>
      <td>19552860</td>
      <td>114.806121</td>
    </tr>
    <tr>
      <th>Illinois</th>
      <td>149995</td>
      <td>12882135</td>
      <td>85.883763</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>141297</td>
      <td>19651127</td>
      <td>139.076746</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>695662</td>
      <td>26448193</td>
      <td>38.018740</td>
    </tr>
  </tbody>
</table>
</div>



### (3)其他取值方法


```python
# 切片
data['Florida':'Illinois']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>area</th>
      <th>pop</th>
      <th>density</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Florida</th>
      <td>170312</td>
      <td>19552860</td>
      <td>114.806121</td>
    </tr>
    <tr>
      <th>Illinois</th>
      <td>149995</td>
      <td>12882135</td>
      <td>85.883763</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[1:3]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>area</th>
      <th>pop</th>
      <th>density</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Florida</th>
      <td>170312</td>
      <td>19552860</td>
      <td>114.806121</td>
    </tr>
    <tr>
      <th>Illinois</th>
      <td>149995</td>
      <td>12882135</td>
      <td>85.883763</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 掩码
data[data.density > 100]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>area</th>
      <th>pop</th>
      <th>density</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Florida</th>
      <td>170312</td>
      <td>19552860</td>
      <td>114.806121</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>141297</td>
      <td>19651127</td>
      <td>139.076746</td>
    </tr>
  </tbody>
</table>
</div>


