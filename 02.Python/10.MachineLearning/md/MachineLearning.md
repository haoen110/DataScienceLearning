
# 机器学习

# 一、概述

### 1. 什么是机器学习？

- 人工智能：通过人工的方法，实现或者近似实现某些需要人类智能处理的问题，都可以称为人工智能。
- 机器学习：一个计算机程序在完成任务T之后，获得经验E，而该经验的效果可以通过P得以表现，如果随着T的增加，借助P来表现的E也可以同步增进，则称这样的程序为机器学习系统。
- 特点：自我完善、自我修正、自我增强。

### 2. 为什么需要机器学习？

1. 简化或者替代人工方式的模式识别，易于系统的开发维护和升级换代。
2. 对于那些算法过于复杂，或者没有明确解法的问题，机器学习系统具有得天独厚的优势。
3. 借鉴机器学习的过程，反向推理出隐藏在业务数据背后的规则——数据挖掘。

### 3. 机器学习的类型

1. **有监督学习**、**无监督学习**、**半监督学习**和**强化学习**
2. **批量学习**和**增量学习**
3. **基于实例**的学习和**基于模型**的学习

### 4. 机器学习的流程

1. 数据
    - 数据采集
    - 数据清洗
2. 机器学习
    - 数据预处理  
    - 选择模型
    - 训练模型
    - 验证模型
3. 业务
    - 使用模型
    - 维护和升级

# 二、数据预处理

- `import sklearn.preprocessing as sp`

### 1. 均值移除(标准化) Standardization (or Z-score normalization)

- 通过算法调整令样本矩阵中每一列(特征)的平均值为0，标准差为1。这样一来，所有特征对最终模型的预测结果都有接近一致的贡献，模型对每个特征的倾向性更加均衡。
    
>Standardization (or Z-score normalization) is the process of rescaling the features so that they’ll have the properties of a Gaussian distribution with μ=0 and σ=1 where μ is the mean and σ is the standard deviation from the mean; standard scores (also called z scores) of the samples are calculated as follows:
$$z = \frac{{x - \mu }}{\sigma }$$

- `sp.scale(原始样本矩阵)` -> 经过均值移除后的样本矩阵


```python
# std.py
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [3, -1.5,  2,   -5.4],
    [0,  4,   -0.3,  2.1],
    [1,  3.3, -1.9, -4.3]])
print(raw_samples)
print('Mean:', raw_samples.mean(axis=0))  # 表示沿着行取平均值，得到每一列的均值
print('S:', raw_samples.std(axis=0))

std_samples = raw_samples.copy()
for col in std_samples.T:
    col_mean = col.mean()
    col_std = col.std()
    col -= col_mean
    col /= col_std
print('手动标准化处理后：', std_samples)
print('处理后的每一列均值：', std_samples.mean(axis=0))
print('处理后的每一列方差：', std_samples.std(axis=0))

std_samples = sp.scale(raw_samples)  # 经过均值移除后的样本矩阵
print('自动标准化处理后：', std_samples)
print('处理后的每一列均值：', std_samples.mean(axis=0))
print('处理后的每一列方差：', std_samples.std(axis=0))
```

    [[ 3.  -1.5  2.  -5.4]
     [ 0.   4.  -0.3  2.1]
     [ 1.   3.3 -1.9 -4.3]]
    Mean: [ 1.33333333  1.93333333 -0.06666667 -2.53333333]
    S: [1.24721913 2.44449495 1.60069429 3.30689515]
    手动标准化处理后： [[ 1.33630621 -1.40451644  1.29110641 -0.86687558]
     [-1.06904497  0.84543708 -0.14577008  1.40111286]
     [-0.26726124  0.55907936 -1.14533633 -0.53423728]]
    处理后的每一列均值： [ 5.55111512e-17 -1.11022302e-16 -7.40148683e-17 -7.40148683e-17]
    处理后的每一列方差： [1. 1. 1. 1.]
    自动标准化处理后： [[ 1.33630621 -1.40451644  1.29110641 -0.86687558]
     [-1.06904497  0.84543708 -0.14577008  1.40111286]
     [-0.26726124  0.55907936 -1.14533633 -0.53423728]]
    处理后的每一列均值： [ 5.55111512e-17 -1.11022302e-16 -7.40148683e-17 -7.40148683e-17]
    处理后的每一列方差： [1. 1. 1. 1.]


### 2. 范围缩放 Min-Max scaling

- 将样本矩阵每一列的元素经过某种线性变换，使得所有列的元素都处在同样的范围区间内，自行设置min和max。

$$kx + b = y \\
k \cdot co{l_{\min }} + b = \min \\
k \cdot co{l_{\max }} + b = \max$$

$$
\left( {\begin{array}{*{20}{c}}
{co{l_{\min }}}&1\\
{co{l_{\max }}}&1
\end{array}} \right)\left( {\begin{array}{*{20}{c}}
k\\
b
\end{array}} \right) = \left( {\begin{array}{*{20}{c}}
{\min }\\
{\max }
\end{array}} \right)$$

                                                      a      x      b
                                            = np.linalg.solve(a, b)
                                            = np.linalg.lstsq(a, b)[0]

- 有时候也把以[0, 1]区间作为目标范围的范围缩放称为"归一化"

>An alternative approach to Z-score normalization (or standardization) is the so-called Min-Max scaling (often also simply called “normalization” - a common cause for ambiguities).In this approach, the data is scaled to a fixed range usually 0 to 1.The cost of having this bounded range - in contrast to standardization - is that we will end up with smaller standard deviations, which can suppress the effect of outliers. A Min-Max scaling is typically done via the following equation:
$${x_i}^\prime  = \frac{{{x_i} - \min (x)}}{{\max (x) - \min (x)}}$$

- `范围缩放器 = sp.MinMaxScaler(feature_range=(min, max))`

- `范围缩放器.fit_transform(原始样本矩阵)` -> 经过范围缩放后的样本矩阵


```python
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [3, -1.5,  2,   -5.4],
    [0,  4,   -0.3,  2.1],
    [1,  3.3, -1.9, -4.3]])
print(raw_samples)
mms_samples = raw_samples.copy()

for col in mms_samples.T:
    col_min = col.min()
    col_max = col.max()
    a = np.array([
        [col_min, 1],
        [col_max, 1]])
    b = np.array([0, 1])
    x = np.linalg.solve(a, b)
    col *= x[0]
    col += x[1]
print(mms_samples)

mms = sp.MinMaxScaler(feature_range=(0, 1))
mms_samples = mms.fit_transform(raw_samples)
print(mms_samples)
```

    [[ 3.  -1.5  2.  -5.4]
     [ 0.   4.  -0.3  2.1]
     [ 1.   3.3 -1.9 -4.3]]
    [[ 1.00000000e+00  0.00000000e+00  1.00000000e+00 -1.11022302e-16]
     [ 0.00000000e+00  1.00000000e+00  4.10256410e-01  1.00000000e+00]
     [ 3.33333333e-01  8.72727273e-01  5.55111512e-17  1.46666667e-01]]
    [[1.         0.         1.         0.        ]
     [0.         1.         0.41025641 1.        ]
     [0.33333333 0.87272727 0.         0.14666667]]


### 3. 归一化

- 用每个样本各个特征值除以该样本所有特征值绝对值之和，以占比的形式来表现特征。

- `sp.normalize(原始样本矩阵, norm='l1')` -> 经过归一化后的样本矩阵
    - `l1 - l1范数`，矢量诸元素的绝对值之和
    - `l2 - l2范数`，矢量诸元素的(绝对值的)平方之和
    - `ln - ln范数`，矢量诸元素的绝对值的n次方之和


```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [3, -1.5,  2,   -5.4],
    [0,  4,   -0.3,  2.1],
    [1,  3.3, -1.9, -4.3]])
print(raw_samples)

# 手动归一
nor_samples = raw_samples.copy()
for row in nor_samples:
    row_absum = abs(row).sum()
    row /= row_absum
print(nor_samples)
print(abs(nor_samples).sum(axis=1))

# 自动归一
nor_samples = sp.normalize(raw_samples, norm='l1')
print(nor_samples)
print(abs(nor_samples).sum(axis=1))
```

    [[ 3.  -1.5  2.  -5.4]
     [ 0.   4.  -0.3  2.1]
     [ 1.   3.3 -1.9 -4.3]]
    [[ 0.25210084 -0.12605042  0.16806723 -0.45378151]
     [ 0.          0.625      -0.046875    0.328125  ]
     [ 0.0952381   0.31428571 -0.18095238 -0.40952381]]
    [1. 1. 1.]
    [[ 0.25210084 -0.12605042  0.16806723 -0.45378151]
     [ 0.          0.625      -0.046875    0.328125  ]
     [ 0.0952381   0.31428571 -0.18095238 -0.40952381]]
    [1. 1. 1.]


### 4. 二值化

- 根据事先给定阈值，将样本矩阵中高于阈值的元素设置为1，否则设置为0，得到一个完全由1和0组成的二值矩阵。

- `二值化器 = sp.Binarizer(threshold=阈值)`

- `二值化器.transform(原始样本矩阵)` -> 经过二值化后的样本矩阵


```python
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [3, -1.5,  2,   -5.4],
    [0,  4,   -0.3,  2.1],
    [1,  3.3, -1.9, -4.3]])
print(raw_samples)

# 手动二值化
bin_samples = raw_samples.copy()
bin_samples[bin_samples <= 1.4] = 0
bin_samples[bin_samples > 1.4] = 1
print(bin_samples)

# 自动二值化
bin = sp.Binarizer(threshold=1.4)
bin_samples = bin.transform(raw_samples)
print(bin_samples)
```

    [[ 3.  -1.5  2.  -5.4]
     [ 0.   4.  -0.3  2.1]
     [ 1.   3.3 -1.9 -4.3]]
    [[1. 0. 1. 0.]
     [0. 1. 0. 1.]
     [0. 1. 0. 0.]]
    [[1. 0. 1. 0.]
     [0. 1. 0. 1.]
     [0. 1. 0. 0.]]


### 5. 独热编码

- 用一个只包含一个1和若干个0的序列来表达每个特征值的编码方式，借此既保留了样本矩阵的所有细节，同时又得到一个只含有1和0的稀疏矩阵，既可以提高模型的容错性，同时还能节省内存空间。

        ----------------------原始矩阵
        1        3        2
        7        5        4
        1        8        6
        7        3        9
        ----------------------编码字典
        1:10   3:100   2:1000
        7:01   5:010   4:0100
               8:001   6:0010
                       9:0001
        ----------------------编码后样本矩阵
        101001000
        010100100
        100010010
        011000001

- `独热编码器 = sp.OneHotEncoder(sparse=是否紧缩(缺省True), dtype=类型)`

- `独热编码器.fit_transform(原始样本矩阵)` -> 经过独热编码后的样本矩阵


```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [1, 3, 2],
    [7, 5, 4],
    [1, 8, 6],
    [7, 3, 9]])
print('Raw array:\n', raw_samples)

# 建立编码字典列表
code_tables = []
for col in raw_samples.T:
    # 针对一列的编码字典
    code_table = {}
    for val in col:
        code_table[val] = None
    code_tables.append(code_table)
    
# 为编码字典列表中每个编码字典添加值
for code_table in code_tables:
    size = len(code_table)
    for one, key in enumerate(sorted(code_table.keys())):
        code_table[key] = np.zeros(shape=size, dtype=int)
        code_table[key][one] = 1
        
# 根据编码字典表对原始样本矩阵做独热编码
ohe_samples = []
for raw_sample in raw_samples:
    ohe_sample = np.array([], dtype=int)
    for i, key in enumerate(raw_sample):
        ohe_sample = np.hstack((ohe_sample, code_tables[i][key]))
    ohe_samples.append(ohe_sample)
ohe_samples = np.array(ohe_samples)
print('手动编码：\n', ohe_samples)

# 自动独热编码
ohe = sp.OneHotEncoder(sparse=False, dtype=int, categories='auto')
ohe_samples = ohe.fit_transform(raw_samples)
print('自动编码：\n', ohe_samples)
# 自动独热编码(紧缩模式)
ohe = sp.OneHotEncoder(dtype=int, categories='auto')
ohe_samples = ohe.fit_transform(raw_samples)
print('自动编码：\n', ohe_samples)
```

    Raw array:
     [[1 3 2]
     [7 5 4]
     [1 8 6]
     [7 3 9]]
    手动编码：
     [[1 0 1 0 0 1 0 0 0]
     [0 1 0 1 0 0 1 0 0]
     [1 0 0 0 1 0 0 1 0]
     [0 1 1 0 0 0 0 0 1]]
    自动编码：
     [[1 0 1 0 0 1 0 0 0]
     [0 1 0 1 0 0 1 0 0]
     [1 0 0 0 1 0 0 1 0]
     [0 1 1 0 0 0 0 0 1]]
    自动编码：
       (0, 0)	1
      (0, 2)	1
      (0, 5)	1
      (1, 1)	1
      (1, 3)	1
      (1, 6)	1
      (2, 0)	1
      (2, 4)	1
      (2, 7)	1
      (3, 1)	1
      (3, 2)	1
      (3, 8)	1


### 6. 标签编码

- 文本形式的特征值->数值形式的特征值，其编码数值源于标签字符串的字典排序，与标签本身的含义无关

        职位    车     编码为：
        员工  toyota     0
        组长  ford       1
        经理  audi       2
        老板  bmw        3

- `标签编码器 = sp.LabelEncoder()`

- `标签编码器.fit_transform(原始样本矩阵)` -> 经过标签编码后的样本矩阵

- `标签编码器.inverse_transform(经过标签编码后的样本矩阵)` -> 原始样本矩阵


```python
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array(['audi', 'ford', 'audi', 'toyota', 'ford', 'bmw', 'toyota', 'bmw'])
print('Raw array:\n', raw_samples)

lbe = sp.LabelEncoder()
lbe_samples = lbe.fit_transform(raw_samples)
print('Labeled:\n', lbe_samples)

raw_samples = lbe.inverse_transform(lbe_samples)
print('Inverse:\n', raw_samples)
```

    Raw array:
     ['audi' 'ford' 'audi' 'toyota' 'ford' 'bmw' 'toyota' 'bmw']
    Labeled:
     [0 2 0 3 2 1 3 1]
    Inverse:
     ['audi' 'ford' 'audi' 'toyota' 'ford' 'bmw' 'toyota' 'bmw']


# 三、机器学习的基本问题

1. **回归问题**：由已知的分布于连续域中的输入和输出，通过不断地模型训练，找到输入和输出之间的联系，通常这种联系可以通过一个函数方程被形式化，如：y=w0+w1x+w2x^2...，当提供未知输出的输入时，就可以根据以上函数方程，预测出与之对应的连续域输出。

2. **分类问题**：如果将回归问题中的输出从连续域变为离散域，那么该问题就是一个分类问题。

3. **聚类问题**：从已知的输入中寻找某种模式，比如相似性，根据该模式将输入划分为不同的集群，并对新的输入应用同样的划分方式，以确定其归属的集群。

4. **降维问题**：从大量的特征中选择那些对模型预测最关键的少量特征，以降低输入样本的维度，提高模型的性能。
