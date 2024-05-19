import matplotlib.pyplot as plt

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, a):
        return Vec3(self.x + a.x, self.y + a.y, self.z + a.z)

    def __mul__(self, a):
        if isinstance(a, (float, int)):
            return Vec3(self.x * a, self.y * a, self.z * a)
        else:
            return self.x * a.x + self.y * a.y + self.z * a.z

    def __sub__(self, a):
        return Vec3(self.x - a.x, self.y - a.y, self.z - a.z)

    def cross(self, a):
        return Vec3(self.y * a.z - self.z * a.y, self.z * a.x - self.x * a.z, self.x * a.y - self.y * a.x)
# Функція для обчислення магнітної індукції
def B():
    return Vec3(0, 0, .01 + 0.0016 * t)
# Функція для обчислення електричного поля
def E():
    return Vec3(0, 0, 0)
X = Vec3(0, 0, 0)
V = Vec3(0.2, 0, 0.2)
t = 0
m: float = 1.2e-1
q = 10e-6
dt = 2
Time = 10000
N = int(Time / dt)
# Функція для обчислення сили
def Force(V):
    return (E() * q + V.cross(B()) * q) * m**-1
x = []
y = []
z = []
# Цикл обчислення траєкторії
for i in range(N):
    t = t + dt
    V = V + Force(V) * dt * m**-1
    X = X + V * dt
    x.append(X.x)
    y.append(X.y)
    z.append(X.z)
# Візуалізація траєкторії
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z,c="black")
plt.title('Частинка в магнітному полі')
fig.set_size_inches(10.5, 9.5)
plt.xlabel('x, м')
plt.ylabel('y, м')
# Зміна кольору заднього фону
ax.set_facecolor((0.9, 0.9, 0.9))  # сірий колір фону
plt.show()
