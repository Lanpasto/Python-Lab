from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

import numpy as np

distance: float = 22e-2
num_points: int = 26 #(число точок табулювання)
charge_1: float = -8e-9 #(номінал першого електричного заряду)
charge_2: float = -10e-9 #(номінал другого електричного заряду)
eps_0: float = 8.85e-12 #(елеткрична стала)

def potential(x: float, y: float) -> float:
    r_1: float = np.sqrt((distance - x) ** 2 + y ** 2)
    r_2: float = np.sqrt(x ** 2 + y ** 2)
    k: float = 1 / (4 * np.pi * eps_0)
    return k * (charge_1 / r_2 + charge_2 / r_1)/100000

def i_to_x(i: float) -> float:
    return 2 * distance * i / num_points - distance / 2.5

def j_to_y(j: float) -> float:
    return distance * j / num_points - distance / 2.

u = np.arange(1, num_points)
X, Y = np.meshgrid(u, u)
V: int = np.array([potential(x, y) for x, y in zip([i_to_x(i) for i in X], [j_to_y(j) for j in Y])]) #розрахунок потенціалу

fig = plt.figure(figsize=(10, 12))

ax1 = fig.add_subplot(321)
CS=ax1.contour(X, Y, V, levels=7, linewidths=1, colors='grey') #побудова контурного графіку
plt.clabel(CS,inline=1, fontsize=10)
plt.xlabel('x, мм')
plt.ylabel('y, мм')

ax2 = fig.add_subplot(322, projection="3d")
CS=ax2.plot_surface(X, Y, V, cmap=cm.coolwarm, linewidth=0, antialiased=False) #побудова графіку поверхні
plt.xlabel('x, мм')
plt.ylabel('y, мм')

ax3 = fig.add_subplot(313)
Ex, Ey = np.gradient(V) #побудова векторного поля
Ex *= -1  
Ey *= -1  
ax3.quiver(X, Y, -Ex, -Ey, color='red')

plt.show()
