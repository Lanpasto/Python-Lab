import numpy as np
import matplotlib.pyplot as plt
# Функція для обчислення похідної (швидкості зміни температури)
def deriv(t, T, k):
    return -k * (T - 43)
# Метод Ейлера
def euler_method(deriv, t0, T0, k, dt, t_end):
    num_steps = int(t_end / dt)
    t = np.zeros(num_steps + 1)
    T = np.zeros(num_steps + 1)
    t[0] = t0
    T[0] = T0

    for i in range(num_steps):
        t[i+1] = t[i] + dt
        T[i+1] = T[i] + deriv(t[i], T[i], k) * dt

    return t, T
# Метод Рунге-Кутти четвертого порядку
def runge_kutta_method(deriv, t0, T0, k, dt, t_end):
    num_steps = int(t_end / dt)
    t = np.zeros(num_steps + 1)
    T = np.zeros(num_steps + 1)
    t[0] = t0
    T[0] = T0

    for i in range(num_steps):
        t[i+1] = t[i] + dt
        k1 = deriv(t[i], T[i], k)
        k2 = deriv(t[i] + 0.5*dt, T[i] + 0.5*k1*dt, k)
        k3 = deriv(t[i] + 0.5*dt, T[i] + 0.5*k2*dt, k)
        k4 = deriv(t[i] + dt, T[i] + k3*dt, k)
        T[i+1] = T[i] + (k1 + 2*k2 + 2*k3 + k4) * dt / 6

    return t, T
# Параметри
t0 = 0  # Початковий час
T0 = 100  # Початкова температура
T_end = 43  # Кінцева температура
k_values = [0.15, 0.25, 0.34]  # коефіцієнта остигання
dt = 0.1  # Крок дискретизації
t_end = 50  # Кінцевий час

for k in k_values:
    t_euler, T_euler = euler_method(deriv, t0, T0, k, dt, t_end)
    t_rk, T_rk = runge_kutta_method(deriv, t0, T0, k, dt, t_end)

    plt.plot(t_euler, T_euler, label=f'Eйлер, k={k}')
    plt.plot(t_rk, T_rk, label=f'Рунге-Кутти, k={k}')

plt.xlabel('Час')
plt.ylabel('Температура')
plt.title('Графік температури від часу для різних значень коефіцієнта "остигання"')
plt.legend()
plt.grid(True)
plt.show()
