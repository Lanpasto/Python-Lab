import math

class Stone:
    def __init__(self, height, terminal_velocity, initial_velocity=0):
        self.height = height
        self.terminal_velocity = terminal_velocity
        self.initial_velocity = initial_velocity  # Початкова швидкість
        self.gravity = 9.81  # прискорення вільного падіння
        # Обчислюємо час падіння з висоти height
        self.fall_time = math.sqrt(2 * self.height / self.gravity)

    def calc_velocity_without_air_resistance(self):
        # Формула для швидкості без опору повітря
        velocity = self.initial_velocity + 0.5 * self.gravity * self.fall_time ** 2
        return velocity

height = 45 
terminal_velocity = 30 

stone = Stone(height, terminal_velocity)

velocity_without_air_resistance = stone.calc_velocity_without_air_resistance()

# Виведення результатів
print("Швидкість без опору повітря: {} м/с".format(velocity_without_air_resistance))
print("Швидкість з опором повітря: {} м/с".format(terminal_velocity))
