from pulp import LpMaximize, LpProblem, LpVariable

# Ініціалізуємо модель
model = LpProblem(name="production_planning", sense=LpMaximize)

# Ініціалізуємо змінні рішення
lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Додаємо обмеження на ресурси
water_constraint = 2 * lemonade + fruit_juice <= 100
sugar_constraint = lemonade <= 50
lemon_juice_constraint = lemonade <= 30
fruit_puree_constraint = 2 * fruit_juice <= 40

# Додаємо обмеження до моделі
model += water_constraint, "water_constraint"
model += sugar_constraint, "sugar_constraint"
model += lemon_juice_constraint, "lemon_juice_constraint"
model += fruit_puree_constraint, "fruit_puree_constraint"

# Функція максимізації - загальна кількість продуктів
model += lemonade + fruit_juice, "total_products"

# Розв'язуємо модель
model.solve()

# Виводимо результати
print("Результати оптимізації:")
print(f"Лимонад: {lemonade.varValue} одиниць")
print(f"Фруктовий сік: {fruit_juice.varValue} одиниць")
