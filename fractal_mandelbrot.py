import numpy as np
import matplotlib.pyplot as plt

# Настройки параметров
width, height = 800, 800
max_iter = 256

# Создание массива для изображения
image = np.zeros((height, width))

# Генерация фрактала Мандельброта
for x in range(width):
    for y in range(height):
        zx, zy = 0, 0
        cX, cY = (x - width / 2) / (width / 4), (y - height / 2) / (height / 4)
        iteration = 0

        while zx * zx + zy * zy < 4 and iteration < max_iter:
            xtemp = zx * zx - zy * zy + cX
            zy, zx = 2.0 * zx * zy + cY, xtemp
            iteration += 1

        image[y, x] = iteration

# Визуализация фрактала
plt.imshow(image, cmap='hot', extent=(-2, 2, -2, 2))
plt.colorbar()
plt.title('Фрактал Мандельброта')
plt.show()
