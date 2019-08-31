import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


data = pd.read_csv('Notes for Machine Learning/Salary_Data.csv')
x = data.values[:, 0]
y = data.values[:, 1]

for i in range(len(x)):
    x[i] = (x[i] - min(x)) / (max(x) - min(x))
for i in range(len(y)):
    y[i] = (y[i] - min(y)) / (max(y) - min(y))

theta = np.array([0, 1])
alpha = 0.08


def J(theta0, theta1, x, y):
    sum = 0.5 * (1 / len(x)) * np.sum(np.power((theta0 + theta1 * x) - y, 2))
    return sum

k = 0
ma = np.empty([1, 2])
cost = []

while True:
    t0 = theta[0] - alpha * (1 / len(x)) * np.sum((theta[0] + theta[1] * x) - y)
    t1 = theta[1] - alpha * (1 / len(x)) * np.sum(((theta[0] + theta[1] * x) - y) * x)
    theta = [t0, t1]
    cost.append(J(theta[0], theta[1], x, y))
    ma = np.vstack([ma, theta])
    k += 1
    if cost[-1] <= 0.001 or k >= 500:
        break


def h(x, theta0, theta1):
    return theta0 + theta1 * x


fig = plt.figure()
for i in range(len(x)):
    plt.plot([x[i], x[i]], [y[i], h(x[i], ma[-1][0], ma[-1][1])], "r--", linewidth=0.8)
plt.plot(x, y, 'o', markersize=4)
plt.plot(x, h(x, ma[-1][0], ma[-1][1]), "b")
plt.title("H")


fig2 = plt.figure()
plt.plot(range(k), cost, 'r')

# n = 1000
# a, b = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))
# z = 0.5 * (1 / len(x)) * np.sum(np.power((theta0 + theta1 * x) - y, 2))
# plt.figure('3D Surface', facecolor='lightgray')
# ax = plt.gca(projection='3d')
# ax.plot_surface(a, b, z, rstride=10, cstride=10, cmap='jet')