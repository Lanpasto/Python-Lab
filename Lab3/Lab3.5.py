import matplotlib.pyplot as plt
import math

class FlyingObject:
    def __init__(self, initial_velocity, height, a0, mass, cross_section_area, g=9.81):
        self.v0 = initial_velocity
        self.h = height
        self.a0 = math.radians(a0)  # Переводимо кут у радіани
        self.m = mass
        self.S = cross_section_area
        self.g = g

    def calculate_trajectory(self, dt=0.01):
        self.x_trajectory = []
        self.y_trajectory = []
        t = 0
        while True:
            x = self.v0 * math.cos(self.a0) * t
            y = self.h + self.v0 * math.sin(self.a0) * t - 0.5 * self.g * t**2  # Формула для вертикального руху
            self.x_trajectory.append(x)
            self.y_trajectory.append(y)
            t += dt
            if y <= 0:
                break

def plot_trajectory(flying_object):
    plt.plot(flying_object.x_trajectory, flying_object.y_trajectory, label='Projectile',c="black")
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Projectile Motion')
    plt.legend()
    plt.grid(True)
    plt.show()

# Параметри
initial_velocity = 10  # Початкова швидкість в м/с
height = 5  # Висота початку руху в метрах
a0 = 45  # Початковий кут у градусах
mass = 6  # Маса тіла в кг
cross_section_area = 0.01  # Площа поперечного перерізу в квадратних метрах

# Створення об'єкту кулі
flying_object = FlyingObject(initial_velocity, height, a0, mass, cross_section_area)

# Обчислення траєкторії
flying_object.calculate_trajectory()

# Візуалізація траєкторії
plot_trajectory(flying_object)
