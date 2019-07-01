# Numpy基础
###########################################
import numpy as np
np.array([1, 4, 2, 5, 3])
np.array([3.14, 4., 2., 3.], dtype=int)
np.zeros(10, dtype=int)
np.ones((3, 5), dtype=float)
np.full((3, 5), 3.14)
np.arange(0, 20, 2)
np.linspace(0, 1, 5)
np.random.random((3, 3))
np.random.normal(0, 1, (3, 3))  # 均值为0，标准差为1
np.random.randint(0, 10, (3, 3))
np.eye(3)
x1 = np.random.randint(10, size=(3, 4, 5))
print(x1.ndim, x1.shape, x1.size, x1.nbytes)

###########################################
# 数组索引；切片；复制；拼接和分裂
###########################################
import numpy as np
x1 = np.random.randint(10, size=10)
x1
print(x1[0], x1[4], x1[-1])

x2 = np.random.randint(10, size=(3, 4))
x2
print(x2[0, 0], x2[2, 0], x2[2, -1])
x2[0, 0] = 3.14  # 赋值时浮点会被截断

x1
x1[:5]
x1[4:7]
x1[::2]
x1[1::2]
x1[::-1]
x1[:5:-2]

x2
x2[:2, :3]
x2[:3, ::2]
x2[::-1, ::-1]
x2[:, 0]
x2[0, :]
x2[0]

x2_copy = x2[:2, :2].copy()
x2_copy[1, 0] = 43
print(x2, x2_copy)

grid = np.arange(1, 10).reshape((3, 3))
x = np.array([1, 2, 3])
x.reshape((1, 3))
x[np.newaxis, :]
x.reshape((3, 1))
x[:, np.newaxis]

# 合并
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate(([x, y]))
z = np.array([99, 99, 99])
print(np.concatenate([x, y, z]))
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
np.concatenate([grid, grid])
np.concatenate([grid, grid], axis=1)
np.vstack([x, grid])
np.hstack([grid, x.reshape(3, 1)])

# 拆分
x = [1, 2, 3, 99,  99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)

grid = np.arange(16).reshape((4, 4))
upper, lower = np.vsplit(grid, [2])
left, right = np.hsplit(grid, [2])

print(upper)
print(lower)
print(left)
print(right)

###########################################
# 通用函数
###########################################
np.arange(5)/np.arange(1,6)
x = np.arange(9).reshape((3, 3))
2 ** x
np.add(1, 2)
np.subtract(1, 2)
np.negative(2)
np.multiply(2, 3)
np.divide(6, 2)
np.floor_divide(3, 2)
np.power(2,3)
np.mod(9, 4)
np.abs(-8)
np.sin(np.pi)
np.arctan(1)
np.exp(4)
np.log(10)
np.log2(2)

x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
y = np.zeros(10)
np.power(2, x, out=y[::2])
print(y)

x = np.arange(1, 6)
np.add.reduce(x)  # 所有乘积
np.multiply.reduce(x)  # 所有之和
np.add.accumulate(x)  #计算中间结果
np.multiply.accumulate(x)  #计算中间结果
np.multiply.outer(x, x)  # 外积
np.sum(x)
np.min(x)
np.max(x)
M = np.random.random((3, 4))
M.sum()
M.min()
M.min(axis=0)
M.max(axis=1)
M.mean()
M.std()
M.var()
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('~/Documents/PythonDataScienceHandbook-master/notebooks/data/president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights.mean(), heights.std(), heights.min(), heights.max(), np.percentile(heights, 25), np.median(heights))
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height(cm)')
plt.ylabel('number')

###########################################
# 广播
###########################################
import numpy as np
a = np.array([0, 1, 2])
b = a[:, np.newaxis]
M = np.ones((3, 3))
M + a
a + b
# 规则1：如果两个数组的维度数不同，那么小纬度数组的形状将会在左补1
# 规则2：如果两个数组的形状在任何一个纬度上都不匹配，那么数组的形状会沿着维度为1的纬度扩展以匹配另外一个数组的形状。
# 规则3：如果两个数组的形状在任何一个纬度上都不匹配并且没有任何一个纬度等于1，那么会引发异常。
M = np.ones((2, 3))
a = np.arange(3)
print(M.shape, a.shape)
M + a  # 规则1 -> 规则2 -> 最终形状都为(2, 3)

a = np.arange(3).reshape((3, 1))
b = np.arange(3)
a + b

M = np.ones((3, 2))
a =  np.arange(3)
M + a  # 出现错误！因为根据规则2，a数组的第一个纬度进行扩展以匹配M的维度
a.shape
a[:, np.newaxis].shape
M + a[:, np.newaxis]  # 完成

# 应用一：归一化
X = np.random.random((10, 3))
Xmean = X.mean(0)
X_centered.mean(0)
# 应用二：画一个二维函数
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
import matplotlib.pyplot as plt
X_centered = X - Xmean
X_centered
plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
plt.colorbar()

###########################################
# 比较、掩码、布尔逻辑
###########################################
x = np.array([1, 2, 3, 4, 5])
x < 3
x != 3
(2 * x) == (x ** 2)

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
np.count_nonzero(x < 6)
np.sum(x < 6)
np.sum(x < 6, 0)
np.sum(x < 6, axis=1)
np.any(x > 8)
np.any(x < 0)
np.all(x < 10)
np.all(x == 10)
np.all(x < 8, axis=1)
np.sum((inches > 0.5) & (inches < 1))  # & | ~ ^(np.bitwise_nor)
x[x < 5]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
rainfall = pd.read_csv('./02.Python/09.DataScience/data/Seattle2014.csv')['PRCP'].values
inches = rainfall / 254  # 1/10mm -> inches
inches.shape
plt.hist(inches, 40)
rainy = (inches > 0)
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)
np.median(inches[rainy])
np.mean(inches[summer])
np.max(inches[summer])
np.median((inches[rainy & ~summer]))

###########################################
# 花哨的索引
###########################################
import numpy as np
rand = np.random.RandomState(42)
x = rand.randint(100, size=10)
[x[3], x[7], x[2]]
ind = [3, 7, 4]
x[ind]
ind = np.array([[3, 7],
                [4, 5]])
x[ind]
X = np.arange(12).reshape((3, 4))
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
X[row, col]
X[row[:, np.newaxis], col]
row[:, np.newaxis] * col
X[2, [2, 0, 1]]
X[1:, [2, 0, 1]]
mask = np.array([1, 0, 1, 0], dtype=bool)
X[row[:, np.newaxis], mask]
#  选择随机点
mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
X = rand.multivariate_normal(mean, cov, 100)
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
plt.scatter(X[:, 0], X[:, 1])
indices = np.random.choice(X.shape[0], 20, replace=False)
selection = X[indices]
plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1], facecolor='none', edgecolors='b', s=200)
# 修改值
x = np.arange(10)
i = np.array([2, 1, 8, 4])
x[i] = 99
x[i] -= 10
###########################################
# 数组的排序
###########################################
x = np.array([2, 1, 4, 3, 5])
np.sort(x)
np.argsort(x)
rand = np.random.RandomState(42)
X = rand.randint(0, 10, (4, 6))
np.sort(X, axis=0)
np.sort(X, axis=1)
np.partition(x, 3)  # 第三小得值
# K个最近邻
X = rand.rand(10, 2)
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
plt.scatter(X[:, 0], X[:, 1], s=100)
dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1)
nearest = np.argsort(dist_sq, axis=1)
K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)
plt.scatter(X[:, 0], X[:, 1], s=100)
for i in range(X.shape[0]):
    for j in nearest_partition[i, :K+1]:
        plt.plot(*zip(X[j], X[i]), color='black')
