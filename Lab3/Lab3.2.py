import math

class Projectile:
    def __init__(self, initial_velocity, gravity):
        self.initial_velocity = initial_velocity  # початкова швидкість в м/с
        self.gravity = gravity  # прискорення вільного падіння в м/с^2

    def compute_flight_time_no_drag(self):
        return 2 * self.initial_velocity / self.gravity

class ProjectileWithDrag(Projectile):
    def __init__(self, initial_velocity, gravity, drag_coefficient, cross_section_area, fluid_density):
        super().__init__(initial_velocity, gravity)
        self.drag_coefficient = drag_coefficient  # коефіцієнт форми
        self.cross_section_area = cross_section_area  # площа поперечного перерізу тіла в м^2
        self.fluid_density = fluid_density  # густина рідини в кг/м^3

    def compute_drag_force(self, velocity):
        drag_factor = 0.5 * self.drag_coefficient * self.cross_section_area * self.fluid_density
        return drag_factor * velocity * abs(velocity)

    def compute_flight_time_with_drag(self):
        discriminant = self.gravity**2 + 4 * self.compute_drag_force(self.initial_velocity) / self.fluid_density
        return (2 * self.initial_velocity) / (self.gravity + math.sqrt(discriminant))

# Дані
initial_velocity = 30  # початкова швидкість в м/с
gravity = 9.8  # прискорення вільного падіння в м/с^2
drag_coefficient = 0.1  # коефіцієнт форми
cross_section_area = 0.01  # площа поперечного перерізу тіла в м^2
fluid_density = 1.29 / 1000  # густина рідини в кг/м^3

# Обчислення часу польоту без гальмівної сили
projectile = Projectile(initial_velocity, gravity)
flight_time_no_drag = projectile.compute_flight_time_no_drag()
print("Час польоту без гальмівної сили:", round(flight_time_no_drag, 2), "с")

# Обчислення часу польоту з гальмівною силою
projectile_with_drag = ProjectileWithDrag(initial_velocity, gravity, drag_coefficient, cross_section_area, fluid_density)
flight_time_with_drag = projectile_with_drag.compute_flight_time_with_drag()
print("Час польоту з гальмівною силою:", round(flight_time_with_drag, 2), "с")
