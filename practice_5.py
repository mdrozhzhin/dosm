courses = [input(f'Введите название курса {i + 1}: ') for i in range(3)]

our_dict = {'политическая теория': '200 г', 'история политических учений': '300 г', 'математика': '100 г'}

print('Рецепт')
for course in courses:
    print(f'{course} : {our_dict.get(course)}')

print('Приправить политической историей. Добавить математические модели по вкусу.')

# TEST FOR GIT HUB
