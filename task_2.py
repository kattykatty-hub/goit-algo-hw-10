import numpy as np

def monte_carlo_integration(func, a, b, num_samples=10000):
    # Ініціалізуємо лічильник точок під кривою
    points_under_curve = 0
    
    # Знаходимо максимальне значення функції на інтервалі [a, b]
    f_max = max(func(x) for x in np.linspace(a, b, 100))
    
    # Генеруємо випадкові точки та обчислюємо кількість точок під кривою
    for _ in range(num_samples):
        x = np.random.uniform(a, b)
        y = np.random.uniform(0, f_max)
        if y <= func(x):
            points_under_curve += 1
    
    # Обчислюємо відношення точок під кривою до загальної кількості точок
    ratio = points_under_curve / num_samples
    
    # Обчислюємо наближене значення інтеграла
    integral = ratio * (b - a) * f_max
    
    return integral

# Визначаємо функцію, яку потрібно інтегрувати
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислюємо значення інтеграла методом Монте-Карло
num_samples = 1000000  # Збільшуємо кількість випадкових точок для більшої точності
monte_carlo_result = monte_carlo_integration(f, a, b, num_samples)
print("Наближене значення інтеграла за допомогою методу Монте-Карло:", monte_carlo_result)
