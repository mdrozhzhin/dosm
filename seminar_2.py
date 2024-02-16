import math
from time import sleep

print(f'Семинар 2. Задание 1:')
print(f'Напишите программу, которая запрашивает у пользователя его фамилию, имя, отчество, введенные в одну строчку '
      f'через пробел, и выводит на экран сообщения:\n\tВаша фамилия: фамилия\n\tВаше имя: имя\n\t'
      f'Ваше отчество: отчество\n')

full_name = input('Введите фамилию, имя и отчество через пробел: ')
full_name = full_name.split(' ')

sleep(1)
print(f'Ваша фамилия: {full_name[0]}')
print(f'Ваше имя: {full_name[1]}')
print(f'Ваше отчество: {full_name[2]}\n')

sleep(1)
print(f'\nСеминар 2. Задание 2:')
print(f'Напишите программу, которая берет строку "1; 2; 3; 100" и возвращает:\n\tсписок из целых чисел\n\tсписок'
      f' из чисел с плавающей точкой\n')

numeric_string = "1; 2; 3; 100"
numeric_string = numeric_string.split("; ")

integer_list = []
float_list = []

for i in numeric_string:
    integer_list.append(int(i))

for i in numeric_string:
    float_list.append(float(i))

sleep(1)
print(f'Лист из целых чисел: {integer_list}')
print(f'Лист из чисел с плавающей точкой: {float_list}\n')


sleep(1)
print(f'\nСеминар 2. Задание 3:')
print(f'#Напишите программу, которая запрашивает у пользователя номер мобильного телефона, введенный через дефис, '
      f'а возвращает номер, записанный без дефисов и пробелов.\n')

sleep(1)
phone_number = input('Введите ваш номер телефона в формате X-XXX-XXX-XX-XX: ')

new_string = phone_number.replace('-', '')
print(f'{new_string}\n')

sleep(1)
print(f'\nСеминар 2. Задание 4:')
print(f'Напишите программу, которая принимает на вход список L, в котором хранятся значения доходов домохозяйств за '
      f'месяц, а возвращает новый список L2 ‒ список логарифмированных значений доходов.\n')

incomes = [38103, 45103, 18103, 23103, 35103]
logaryphmic = []

for i in incomes:
    logaryphmic.append(math.log(i))

print(f'{logaryphmic}\n')

sleep(1)
print(f'\nСеминар 2. Задание 5:')
print(f'Напишите программу, которая принимает на вход список слов такого вида:'
      f'\n\twords = ["Speak ","to", "me ", "of", "Florence" ,"And ", "of", "the", "Renaissance"], '
      f'\n\tа возвращает список:'
      f'\n\twords_clean = ["speak", "to", "me", "of", "florence", "and", "of", "the", "renaissance"]\n'
      f'\tДругими словами, программа убирает пробелы в словах и приводит все слова к нижнему регистру.\n')
words = ["Speak ","to", "me ", "of", "Florence" ,"And ", "of", "the", "Renaissance"]

words_clean = []

for i in words:
    i = i.strip()
    i = i.lower()
    words_clean.append(i)

print(f'{words_clean}\n')
