import numpy as np
import random
import matplotlib.pyplot as plt
from tkinter import *

# Задані параметри
L = 17
p_values = [0.4, 0.5927, 0.8]
N_trials = 5

# Функція для генерації квадратної гратки з розмірністю L
def generate_grid(L, p):
    grid = np.random.rand(L, L) < p
    return grid.astype(int)

# Функція для знаходження розміру кластера для заданої точки на гратці
def find_cluster_size(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
        return 0
    grid[i][j] = 0
    size = 1
    size += find_cluster_size(grid, i + 1, j)
    size += find_cluster_size(grid, i - 1, j)
    size += find_cluster_size(grid, i, j + 1)
    size += find_cluster_size(grid, i, j - 1)
    return size

# Функція для проведення випробувань та обчислення середнього розміру кластера для кожного p
def simulate_percolation(L, p_values, N_trials):
    results = {}
    for p in p_values:
        sizes = []
        for _ in range(N_trials):
            grid = generate_grid(L, p)
            cluster_sizes = []
            for i in range(L):
                for j in range(L):
                    size = find_cluster_size(grid, i, j)
                    if size > 0:
                        cluster_sizes.append(size)
            sizes.extend(cluster_sizes)
        results[p] = sizes
    return results

# Функція для обчислення розподілу розмірів кластерів ns(p) та побудови графіків
def plot_cluster_distribution(results):
    P_infinity_values = [] # Значення P(p -> infinity)
    for p, sizes in results.items():
        # Виведення графічного представлення для кластерів
        root = Tk()
        canvas = Canvas(root, width=250, height=250)
        canvas.pack()
        x0 = 10
        y0 = 10
        dx = 20
        dy = 20
        x1 = 30
        y1 = 30
        for i in range(0, L):
            for j in range(0, L):
                if random.random() < p:
                    square = canvas.create_rectangle(x0, y0, x1, y1, fill="green")
                    text = canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text="1", font=("Helvetica", "12"))
                else:
                    square = canvas.create_rectangle(x0, y0, x1, y1, fill='white')
                    text = canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text="0", font=("Helvetica", "12"))
                y1 += dy
                y0 += dy
            y0 = 10
            y1 = 30
            x0 += dy
            x1 += dy
        root.mainloop()
        
        # Обчислення середнього розміру кластера S
        sum_nsp = sum([s**2 * sizes.count(s) * p for s in sizes])
        sum_np = sum([sizes.count(s) * p for s in sizes])
        S = sum_nsp / sum_np
        print(f"Середнiй розмiр кластера для p = {p}: {S}")
        
        # Обчислення P(p -> infinity)
        P_infinity = sizes.count(max(sizes)) / sum([sizes.count(s) for s in sizes])
        P_infinity_values.append(P_infinity)
        print(f"P(p -> infinity) для p = {p}: {P_infinity}")
        
      # Побудова графіку розподілу розмірів кластерів
        plt.figure(figsize=(12, 8))
        hist, bins = np.histogram(sizes, bins=range(1, max(sizes) + 2), density=True)
        plt.plot(bins[:-1], hist, marker='o', label=f'p = {p}', color='orange') 
        plt.title('Cluster Size Distribution')
        plt.xlabel('Cluster Size (s)')
        plt.ylabel('Probability Density')
        plt.legend()
        plt.grid(True)
        plt.gca().set_facecolor('lightblue') 
        plt.show()

        
   # Побудова графіка P(p)
    plt.figure(figsize=(10, 6))
    plt.plot(p_values, P_infinity_values, marker='o', linestyle='-', color='green')  
    plt.title('Probability P(p)')
    plt.xlabel('p')
    plt.ylabel('P(p)')
    plt.grid(True)
    plt.gca().set_facecolor('lightyellow')  
    plt.show()


# Виконання випробувань та побудова графіка
results = simulate_percolation(L, p_values, N_trials)
plot_cluster_distribution(results)