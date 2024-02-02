days = int(input('Введите число дней: '))
minutes = 1

if days > 1:
    minutes += (days - 1) * 3
    print(f'Номер дня: {days} и число минут: {minutes}')
else:
    print(f'Номер дня: {days} и число минут: {minutes}')
