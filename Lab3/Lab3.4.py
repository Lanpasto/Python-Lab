import math

class MetalSphere:
    def __init__(self, r, v_init, alpha_0=None, g=9.81, k2=0.1, dt=0.01):
        self.r = r
        self.v_init = v_init
        self.alpha_0 = math.radians(alpha_0) if alpha_0 is not None else None
        self.g = g
        self.k2 = k2
        self.dt = dt

    def euler_cromer_method(self):
        v_x = self.v_init * math.cos(self.alpha_0)
        v_y = self.v_init * math.sin(self.alpha_0)
        x = 0
        y = 0
        while y >= 0:
            v = math.sqrt(v_x ** 2 + v_y ** 2)
            F_op = self.k2 * v ** 2
            a_x = -F_op * v_x / (self.r * v)
            a_y = -self.g - F_op * v_y / (self.r * v)
            v_x += a_x * self.dt
            v_y += a_y * self.dt
            x += v_x * self.dt
            y += v_y * self.dt
        return x

    def analytical_solution(self, alpha=None):
        if alpha is None:
            alpha = self.alpha_0
        return (self.v_init ** 2) * math.sin(2 * alpha) / self.g

    def optimal_launch_angle(self, h, v0):
        k2_over_m = self.k2 / 7  # маса 7 кг
        A = k2_over_m
        alpha_optimal = math.atan((v0 / (math.sqrt(v0**2 + 2 * self.g * h))) * ((1 + math.sqrt(1 + 4 * A * h / (v0**2))) / (2 * A)))
        return math.degrees(alpha_optimal)

    def max_distance(self, alpha):
        alpha_rad = math.radians(alpha)
        return (self.v_init ** 2) * math.sin(2 * alpha_rad) / self.g

# Задані параметри
r = 0.04  # радіус кулі в метрах
v_init = 30  # початкова швидкість в м/с

# Створення об'єкта кулі
metal_sphere = MetalSphere(r, v_init)

optimal_angle = metal_sphere.optimal_launch_angle(2, v_init)
print("Оптимальний кут кидання: {:.2f} градусів".format(optimal_angle))

# Обчислення максимальної відстані для оптимального кута кидання
max_distance_optimal_angle = metal_sphere.max_distance(optimal_angle)
print("Максимальна відстань при оптимальному куті кидання: {:.2f} м".format(max_distance_optimal_angle))
