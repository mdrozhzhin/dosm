import math

L = [12, 3, 8, 125, 10, 98, 54, 199]

for i in L:
    print(i)

for i in L:
    print(math.log(i))

L[4] = 0

for i in L:
    print(i)


def logaryphmic():
    try:
        for element in L:
            print(math.log(element))
    except ValueError as ex:
        print(f'Ноль не является положительным числом. Ошибка: {ex}')


logaryphmic()
