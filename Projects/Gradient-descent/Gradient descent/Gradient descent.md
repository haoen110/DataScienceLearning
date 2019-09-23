
# Gradient Descent

Today, I'm going to try this method to solve a linear regression problem.

Function can be written as:

$$h(\theta)=\theta_0+\theta_1x$$

The cost function, "Squared error function", or "Mean squared error" is:

$$J(θ_0,θ_1)=\frac{1}{2}m\sum_{i=1}^m=\frac{1}{2m}(\hat{y_i}−y_i)^2=\frac{1}{2m}(h_\theta(x_i)−y_i)^2$$

Iterate until function $J(\theta)$ to 

$$Min J(θ_0,θ_1)$$ 

Iterate by:

$$ \theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j}J(θ_0,θ_1) $$

":=" means renew the value.

## Import


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from sklearn import preprocessing
import warnings
%matplotlib inline 
%config InlineBackend.figure_format = 'retina'
warnings.filterwarnings('ignore')

data = pd.read_csv("./Salary_Data.csv")
display(data)
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
      <th>YearsExperience</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.1</td>
      <td>39343.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.3</td>
      <td>46205.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.5</td>
      <td>37731.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.0</td>
      <td>43525.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.2</td>
      <td>39891.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2.9</td>
      <td>56642.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3.0</td>
      <td>60150.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3.2</td>
      <td>54445.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3.2</td>
      <td>64445.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>3.7</td>
      <td>57189.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3.9</td>
      <td>63218.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4.0</td>
      <td>55794.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>4.0</td>
      <td>56957.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>4.1</td>
      <td>57081.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>4.5</td>
      <td>61111.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>4.9</td>
      <td>67938.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>5.1</td>
      <td>66029.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>5.3</td>
      <td>83088.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>5.9</td>
      <td>81363.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>6.0</td>
      <td>93940.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>6.8</td>
      <td>91738.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>7.1</td>
      <td>98273.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>7.9</td>
      <td>101302.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>8.2</td>
      <td>113812.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>8.7</td>
      <td>109431.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>9.0</td>
      <td>105582.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>9.5</td>
      <td>116969.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>9.6</td>
      <td>112635.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>10.3</td>
      <td>122391.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>10.5</td>
      <td>121872.0</td>
    </tr>
  </tbody>
</table>
</div>


## Preprocessing

The scale of the data is too big, so we need to normalize them by:

$$ z = \frac{x-min(x)}{max(x)-min(x)} $$


```python
x = data.values[:, 0]
y = data.values[:, 1]
x = preprocessing.normalize([x]).T
y = preprocessing.normalize([y]).T
```

## Functions

The define some functinos:


```python
def h(t0, t1):
    '''linear function'''
    return t0 + t1 * x


def J(t0, t1):
    '''cost function'''
    sum = 0.5 * (1 / len(x)) * np.sum(np.power((t0 + t1 * x) - y, 2))
    return sum


def gd(t0, t1, alpha, n_iter):
    '''main function'''
    theta = [t0, t1]
    temp = np.array([t0, t1])
    cost = []

    k = 0
    while True:
        t0 = theta[0] - alpha * (1 / len(x)) * np.sum((theta[0] + theta[1] * x) - y)
        t1 = theta[1] - alpha * (1 / len(x)) * np.sum(((theta[0] + theta[1] * x) - y) * x)
        theta = [t0, t1]
        cost.append(J(t0, t1))
        temp = np.vstack([temp, theta])
        k += 1
        if k >= n_iter:
            break
    return cost, temp, theta
```

# Output


```python
cost, temp, theta = gd(0, 1, 1, 500)
print("The result is: h = %.2f + %.2f * x" % (theta[0], theta[1]))
yh = h(theta[0], theta[1])
fig1 = plt.figure(dpi=150)
plt.plot(x, yh)
plt.plot(x, y, 'o', markersize=1.5)
for i in range(len(x)):
    plt.plot([x[i], x[i]], [y[i], yh[i]], "r--", linewidth=0.8)
plt.title("Fit")
plt.tight_layout()
plt.show()
```

    The result is: h = 0.06 + 0.71 * x



![png](output_8_1.png)



```python
fig2 = plt.figure(dpi=150)
plt.plot(range(len(cost)), cost, 'r')
plt.title("Cost Function")
plt.tight_layout()
plt.show()
```


![png](output_9_0.png)


## Compared to Normal Equation

$$ \theta = (X^T X)^{-1} X^T y $$


```python
X = x
X.shape
```




    (30, 1)




```python
one = np.ones((30, 1))
one.shape
X = np.concatenate([one, X], axis=1)
```




    (30, 1)




```python
theta = np.linalg.pinv(X.T @ X) @ X.T @ y
theta
```




    array([[0.05839456],
           [0.70327706]])




```python
print("The result is: h = %.2f + %.2f * x" % (theta[0], theta[1]))
yh = h(theta[0], theta[1])
fig1 = plt.figure(dpi=150)
plt.plot(x, yh)
plt.plot(x, y, 'o', markersize=1.5)
for i in range(len(x)):
    plt.plot([x[i], x[i]], [y[i], yh[i]], "r--", linewidth=0.8)
plt.title("Fit")
plt.tight_layout()
plt.show()
```

    The result is: h = 0.06 + 0.70 * x



![png](output_14_1.png)



```python
print("gd cost:", cost[-1])
print("ne cost:", J(theta[0], theta[1]))
```

    gd cost: 8.042499159722341e-05
    ne cost: 8.014548878265756e-05





    True


