import numpy as np
import matplotlib.pyplot as plt

# Определение первой функции
def f1(x):
    if x < 2:
        return 0
    elif 2 <= x <= 4:
        return (x**2 - 2*x) / 8
    else:
        return 1

# Определение второй функции
def f2(x):
    if 2 <= x <= 4:
        return 1/4 * (x - 1)
    else:
        return 0

# Создание массива x для графиков
x1 = np.linspace(0, 6, 100)
y1 = [f1(x) for x in x1]

x2 = np.linspace(0, 6, 100)
y2 = [f2(x) for x in x2]

# Построение графиков
plt.figure(figsize=(12, 6))

# График первой функции
plt.subplot(1, 2, 1)
plt.plot(x1, y1, label='f1(x)', color='blue')
plt.title('График функции f1(x)')
plt.xlabel('x')
plt.ylabel('f1(x)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.xlim(0, 6)
plt.ylim(-0.5, 1.5)
plt.grid()
plt.legend()

# График второй функции
plt.subplot(1, 2, 2)
plt.plot(x2, y2, label='f2(x)', color='orange')
plt.title('График функции f2(x)')
plt.xlabel('x')
plt.ylabel('f2(x)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.xlim(0, 6)
plt.ylim(-0.5, 1.5)
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()