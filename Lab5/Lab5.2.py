import matplotlib.pyplot as plt
import numpy as np

# Ваші значення зарядів та відстань
q1 = -8e-9
q2 = -10e-9
r = 26

# Функція для обчислення напруженості
def electric_field(q1, q2, r, x, y):
    k = 9 * 10 ** 9
    v2 = (k * q1) / (((x + r / 2) ** 2 + (y) ** 2))
    v3 = (k * q2) / (((x - r / 2) ** 2 + (y) ** 2))
    x2 = ((x + r / 2)) * (v2 / (((r / 2 + x) ** 2 + (y) ** 2) ** 0.5))
    y2 = y * (v2 / (((r / 2 + x) ** 2 + (y) ** 2) ** 0.5))
    x3 = (x - r / 2) * (v3 / (((x - r / 2) ** 2 + (y) ** 2) ** 0.5))
    y3 = y * (v3 / (((r / 2 - x) ** 2 + (y) ** 2) ** 0.5))
    x1 = (x2 + x3)
    y1 = (y2 + y3)
    return x1, y1

# Параметри для графіка
size = 20
qual = 3.0
gr = np.mgrid[-size:(size + 1):qual, -size:(size + 1):qual]
xg, yg = np.array(gr[0]).reshape(-1), np.array(gr[1]).reshape(-1)

# Малюнок з жовтим фоном
plt.figure(dpi=150, facecolor='grey')
plt.xlim(-(size + 1), (size + 1))
plt.ylim(-(size + 1), (size + 1))
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter([-r / 2, r / 2], [0, 0])

# Обчислення та відображення напруженості
for x, y in zip(xg, yg):
    x1, y1 = electric_field(q1, q2, r, x, y)
    plt.scatter([x, x1 + x], [y, y1 + y], s=0) 
    plt.arrow(x, y, x1 * 10, y1 * 10, color='y', head_width=0.1, linewidth=0.2)  # Зміна кольору на синій

plt.show()
