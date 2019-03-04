###########################################
# Pandas
###########################################
import numpy as np
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0])
data.values
data.index
data[0]
data[1:3]
# 创建Series
pd.Series([2, 4, 6])
pd.Series(5, index=[100, 200, 300])
pd.Series({2: 'a', 1: 'b', 3: 'c'})
pd.Series({2: 'a', 1: 'b', 3: 'c'}, index=[3, 2])
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
states = pd.DataFrame({'population': population, 'area': area})
states.index
states.columns
states['area']
# 创建Dataframe
pd.DataFrame(population, columns=['population'])
data = [{'a': i, 'b': 2 * i} for i in range(3)]
pd.DataFrame(data)
pd.DataFrame({'population': population, 'area': area})
pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar'], index=['a', 'b', 'c'])

ind = pd.Index([2, 3, 5, 7, 11])
ind[::2]
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])
indA & indB  # 交集
indA | indB  # 并集
indA ^ indB  # 异域
###########################################
# 数据取值与选择
###########################################
# Series 数据选择方法
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
data['b']
data.keys()
list(data.items())
data['e'] = 1.25
data['a':'c']
data[0:2]
data[(data > 0.3) & (data < 0.8)]
data[['a', 'e']]

data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
data.loc[1]  # 显式
data.loc[1:3]
data.iloc[1]
data.iloc[1:3]

# Dataframe 数据选择方法
pop = pd.Series({'California': 38332521,
                 'Texas': 26448193,
                 'New York': 19651127,
                 'Florida': 19552860,
                 'Illinois': 12882135})
area = pd.Series({'California': 423967, 'Texas': 695662, 'New York': 141297,
                  'Florida': 170312, 'Illinois': 149995})
data = pd.DataFrame({'area': area, 'pop': pop})
data.area
data['density'] = data['pop'] / data['area']  # 生成新变量
data.values
data.T

data.iloc[:3, :2]
data.loc[:'Illinois', :'pop']
data.ix[:3, :'pop']  # 混合模式
data.loc[data.density > 100, ['pop', 'density']]
data.iloc[0, 2] = 90
data['Florida':'Illinois']
data[1:3]
data[data.density > 100]
###########################################
# 数值运算
###########################################
import pandas as pd
import numpy as np

rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4))
df = pd.DataFrame(rng.randint(0, 10, (3, 4)), columns=['A', 'B', 'C', 'D'])

area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193,
                        'New York': 19651127}, name='population')
population / area  # 索引为两个数组索引的并集

A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
A + B
A.add(B, fill_value=0)

A = pd.DataFrame(rng.randint(0, 20, (2, 2)), columns=list('AB'))
B = pd.DataFrame(rng.randint(0, 20, (3, 3)), columns=list('BAC'))
A + B
fill = A.stack().mean()
A.add(B, fill_value=fill)

A = rng.randint(10, size=(3, 4))
A - A[0]

df = pd.DataFrame(A, columns=list('QRST'))
df - df.iloc[0]
df.subtract(df['R'], axis=0)
halfrow = df.iloc[0, ::2]
df - halfrow
###########################################
# Pandas缺失值
###########################################
import numpy as np
import pandas as pd
vals1 = np.array([1, None, 3, 4])

vals2 = np.array([1, np.nan, 3, 4])
vals2.dtype
vals2.sum()
np.nansum(vals2)

pd.Series([1, np.nan, 2, None])
x = pd.Series(range(2), dtype=int)
x[0] = None

# 检测缺失值
data = pd.Series([1, np.nan, 'hello', None])
data.isnull()
data[data.notnull()]
data.dropna()
df = pd.DataFrame([[1, np.nan, 2],
                   [2, 3, 5],
                  [np.nan, 4, 6]])
df.dropna()
df.dropna(axis='columns')
df[3] = np.nan
df.dropna(axis='columns', how='any')
df.dropna(axis='columns', how='all')
df.dropna(axis='rows', thresh=3)

data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
data.fillna(0)
data.fillna(method='ffill')
data.fillna(method='bfill')
df.fillna(method='ffill', axis=1)
###########################################
# 层级索引
###########################################
#  The bad way
index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]
pop = pd.Series(populations, index=index)
pop[('California', 2010):('Texas', 2000)]
pop[[i for i in pop.index if i[1] == 2010]]
# Better way
index = pd.MultiIndex.from_tuples(index)
pop = pop.reindex(index)
pop[:, 2010]
# 高维数据的多级索引
pop_df = pop.unstack()  # 快速将一个多级索引的Series转换为DataFrame
a = pop_df.stack()  # 相反操作

# 多级索引创建方法
df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['data1', 'data2'])
data = {('California', 2000): 33871648,
        ('California', 2010): 37253956,
        ('Texas', 2000): 20851820,
        ('Texas', 2010): 25145561,
        ('New York', 2000): 18976457,
        ('New York', 2010): 19378102}
pd.Series(data)

# 显示地创建
pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])
pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])
pd.MultiIndex.from_product([['a', 'b'], [1, 2]])
pd.MultiIndex(levels=[['a', 'b'], [1, 2]],
              labels=[[0, 0, 1, 1], [0, 1, 0, 1]])
# 多级索引的等级名称
pop.index.names = ['state', 'year']
