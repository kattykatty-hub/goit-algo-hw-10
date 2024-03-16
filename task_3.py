import numpy as np
from scipy.integrate import quad

def f(x):
    return x ** 2

a = 0
b = 2

# Аналітичне значення інтегралу
analytical_result = 8/3

# Застосуємо метод Монте-Карло
num_samples = 1000000
monte_carlo_result = monte_carlo_integration(f, a, b, num_samples)

# Використаємо функцію quad для порівняння
quad_result, _ = quad(f, a, b)

print("Аналітичне значення інтеграла:", analytical_result)
print("Наближене значення інтеграла за допомогою методу Монте-Карло:", monte_carlo_result)
print("Результат інтегрування за допомогою функції quad:", quad_result)
