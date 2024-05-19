import math

class SteelBall:
    def __init__(self, radius, initial_velocity, initial_angle=None, g=9.81, drag_coefficient=0.1, time_step=0.01):
        self.radius = radius
        self.initial_velocity = initial_velocity
        self.initial_angle = math.radians(initial_angle) if initial_angle is not None else None
        self.g = g
        self.drag_coefficient = drag_coefficient
        self.time_step = time_step

    def euler_cromer_method(self):
        velocity_x = self.initial_velocity * math.cos(self.initial_angle)
        velocity_y = self.initial_velocity * math.sin(self.initial_angle)
        x_position = 0
        y_position = 0
        while y_position >= 0:
            velocity = math.sqrt(velocity_x ** 2 + velocity_y ** 2)
            drag_force = self.drag_coefficient * velocity ** 2
            acceleration_x = -drag_force * velocity_x / (self.radius * velocity)
            acceleration_y = -self.g - drag_force * velocity_y / (self.radius * velocity)
            velocity_x += acceleration_x * self.time_step
            velocity_y += acceleration_y * self.time_step
            x_position += velocity_x * self.time_step
            y_position += velocity_y * self.time_step
        return x_position

    def analytical_solution(self, angle=None):
        if angle is None:
            angle = self.initial_angle
        return (self.initial_velocity ** 2) * math.sin(2 * angle) / self.g

# Параметри
radius = 0.04  # радіус кулі в метрах
initial_velocity = 30  # початкова швидкість в м/с
initial_angle = 55  # початковий кут у градусах

# Створення об'єкта кулі
steel_ball = SteelBall(radius, initial_velocity, initial_angle)

# Обчислення максимальної відстані методом Ейлера-Кромера
max_distance_numerical = steel_ball.euler_cromer_method()

# Обчислення максимальної відстані аналітично
max_distance_analytical = steel_ball.analytical_solution()

print("Максимальна відстань (чисельний метод): {:.2f} м".format(max_distance_numerical))
print("Максимальна відстань (аналітичний метод): {:.2f} м".format(max_distance_analytical))

# Перевірка зміни відстані для нового кута
new_angle_degrees = 55  # Новий кут в градусах
angle_difference_percent = 0.02  # Відсоток зміни кута
new_angle_radians = new_angle_degrees * (1 + angle_difference_percent)

# Обчислення нової відстані політу для нового кута
new_max_distance_analytical = steel_ball.analytical_solution(math.radians(new_angle_radians))

# Зміна відстані в відсотках
change_in_distance_percent = ((new_max_distance_analytical - max_distance_analytical) / max_distance_analytical) * 100

print("Максимальна відстань (початковий кут): {:.2f} м".format(max_distance_analytical))
print("Максимальна відстань (новий кут): {:.2f} м".format(new_max_distance_analytical))
print("Зміна у відсотках: {:.2f}%".format(change_in_distance_percent))
