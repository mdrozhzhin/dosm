course_1 = str(input('Введите название первого курса: '))
course_2 = str(input('Введите название второго курса: '))
course_3 = str(input('Введите название третьего курса: '))

our_dict = {'политическая теория': '200 г', 'история политических учений': '300 г', 'математика': '100 г'}

print('\nРецепт')
print(f'{course_1} : {our_dict.get(course_1)}')
print(f'{course_2} : {our_dict.get(course_2)}')
print(f'{course_3} : {our_dict.get(course_3)}')
print('Приправить политической историей. Добавить математические модели по вкусу.')

# print(f'{course_1} : {our_dict.get(course_1)}\n{course_2} : {our_dict.get(course_2)}\n{course_3} : {our_dict.get(course_3)}')
# Сложночитаемый код. Для более простого чтения лучше сделать несколько print.
