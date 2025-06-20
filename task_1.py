from pulp import LpMaximize, LpProblem, LpVariable, value, LpStatus


model = LpProblem(name="production-optimization", sense=LpMaximize)

# Змінні
x = LpVariable(name="lemonade", lowBound=0, cat="Integer")
y = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Обмеження
model += (2 * x + 1 * y <= 100, "Water_constraint")
model += (1 * x <= 50, "Sugar_constraint")
model += (1 * x <= 30, "Lemon_juice_constraint")
model += (2 * y <= 40, "Fruit_puree_constraint")

# Цільова функція
model += x + y, "Total_drinks_produced"


model.solve()


print(f"Статус: {LpStatus[model.status]}")
print(f"Виробити лимонаду: {x.value()} одиниць")
print(f"Виробити фруктового соку: {y.value()} одиниць")
print(f"Загальна кількість напоїв: {value(model.objective)}")
