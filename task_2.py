import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# 1. Функція, яку інтегруємо
def f(x):
    return x**2


# Межі інтегрування
a = 0
b = 2

# 2. Метод Монте-Карло
N = 1000000
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
monte_carlo_integral = (b - a) * np.mean(y_rand)

# 3. Аналітичне значення (через quad)
quad_result, quad_error = quad(f, a, b)

# 4. Вивід результатів
print(f"Метод Монте-Карло: {monte_carlo_integral:.6f}")
print(f"Аналітичний (quad): {quad_result:.6f} (похибка: {quad_error:.1e})")
print(f"Абсолютна похибка Монте-Карло: {abs(monte_carlo_integral - quad_result):.6f}")

# 5. Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, "r", linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()
