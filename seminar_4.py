from time import sleep

print(f'Семинар 4. Задание 1:')
sleep(1)
print(f'Дан словарь с названиями разных рептилий:\n'
      f'\t- Добавьте в словарь пару \'snake\' - \'змея\'.\n'
      f'\t- Исправьте ключ \'tortoize\' на правильный \'tortoise\'.\n'
      f'\t- Выведите на экрат сообщения вида:\n'
      f'\t\t Питон по-английски будет python\n')
sleep(1)

rept = {"python": "питон", "anaconda": "анаконда", "tortoize": "черепаха", "snake": "змея"}

del rept["tortoize"]
rept["tortoise"] = "черепаха"

for k, v in rept.items():
    sleep(0.5)
    print(f'{v.capitalize()} по-английски будет {k}.')

sleep(2)
print(f'\nСеминар 4. Задание 2:')
sleep(1)
print(f'В списке cnt хранятся названия стран, а в списке fh – значения индекса Freedom House\n'
      f'для этих стран. Создайте словарь, используя в качестве ключей названия стран, а в \n'
      f'качестве значений – значения индекса.\n')

cnt = ['Andorra', 'Belarus', 'Denmark',
       'Kenia', 'Jamaica', 'Romania']
fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]

countries_rating = dict(list(zip(cnt, fh)))
sleep(1)
print(countries_rating)


sleep(2)
print(f'\nСеминар 4. Задание 2:')
sleep(1)
print(f'Дан список, состоящий из пар чисел:\n'
      f'Создайте словарь calc , где ключами являются пары чисел, а значениями – их произведение\n'
      f'(произведение тоже должно считаться в Python, не в уме).\n')

pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]

calc = {pair: pair[0] * pair[1] for pair in pairs}

sleep(1)
print(calc)


sleep(2)
print(f'\nСеминар 4. Задание 2:')
sleep(1)
print(f'Дан словарь grades с оценками студентов за контрольную работу в 5-балльной шкале.\n'
      f'Напишите код, который сделает следующее:\n'
      f'\tВыведет на экран имя каждого студента и его оценку (каждый студент – с новой строки).\n'
      f'\tСохранит имена студентов, получивших отличные оценки, в список excel.\n'
      f'\tСохранит имена студентов, получивших хорошие оценки, в список good.\n'
      f'\tСохранит имена студентов, получивших удовлетворительные оценки, в список satisf.\n'
      f'\tСохранит имена студентов, получивших плохие оценки, в список bad.\n')

grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
          'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
          'Ursula': 4, 'Viktor': 5}

for k, v in grades.items():
    sleep(0.5)
    print(f'{k} {v}')

excel = [k for k, v in grades.items() if v == 5]
good = [k for k, v in grades.items() if v == 4]
satisf = [k for k, v in grades.items() if v == 3]
bad = [k for k, v in grades.items() if v == 2]

sleep(1)
print(f'{excel}, \n{good}, \n{satisf}, \n{bad}')
