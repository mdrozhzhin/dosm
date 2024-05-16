import pandas as pd
import matplotlib.pyplot as plt

# T1. Загружаем Titanic.csv
data = pd.read_csv('Titanic.csv')

# T2. Загружаем БД с индексом PassengerId
data_with_index = pd.read_csv('Titanic.csv', index_col='PassengerId')

# T3. Удаляем строки с пропущенными значениями и сохранение изменений в самой базе
data.dropna(inplace=True)

# T3. Сводная информация по
print("Сводная информация по базе данных:")
print(data.info())

# T4. Вывод сводной статистической информации по каждому количественному показателю в базе
print("\nСводная статистическая информация:")
print(data.describe())

# T5. Построение гистограммы для переменной Возраст (Age)
data['Age'].plot(kind='hist', color='red')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.title('Гистограмма возраста пассажиров')
plt.show()

# T6. Вывод описательных статистик для столбца Стоимость билета (Fare)
print("\nОписательные статистики для столбца Стоимость билета (Fare):")
print(data['Fare'].describe())

# T7. Вывод названий столбцов в базе данных в виде списка
print("\nНазвания столбцов в базе данных:")
print(list(data.columns))

# T8. Переименование столбца с классом пассажира из Pclass в Class
data.rename(columns={'Pclass': 'Class'}, inplace=True)
print('\nСтолбец Pclass переименован в Class.')

# T9. Выбор из базы данных всех строк, которые соответствуют пассажирам женского пола, и сохранение их в новую базу
# female
female_data = data[data['Sex'] == 'female']
print(f'\nБаза данных с пассажирами женского пола:\n{female_data}')

# T10. Выбор из базы данных всех строк, которые соответствуют выжившим пассажирам мужского пола младше 32 лет,
# и сохранение их в базу Ymale
Ymale_data = data[(data['Sex'] == 'male') & (data['Survived'] == 1) & (data['Age'] < 32)]
print(f'\nБД с выжившими пассажирами мужского пола младше 32 лет:\n{Ymale_data}')

# T11. Выбор из базы данных всех строк, которые соответствуют пассажирам 1 или 2 класса
class_1_2_data = data[data['Class'].isin([1, 2])]
print(f'\nСтроки, соответствующие пассажирам 1 или 2 класса:\n{class_1_2_data}')

# T12. Выбор из базы данных всех строк, которые соответствуют выжившим пассажирам 1 или 2 класса
survived_class_1_2_data = data[(data['Class'].isin([1, 2])) & (data['Survived'] == 1)]
print(f'\nСтроки, соответствующие выжившим пассажирам 1 или 2 класса\n{survived_class_1_2_data}')

# Добавление в датафрейм столбца Female, состоящего из значений 0 и 1, где 1 соответствует пассажирам женского пола
data['Female'] = (data['Sex'] == 'female').astype(int)

# 14. Вывод всех уникальных значений в столбце Embarked
print("\nУникальные значения в столбце Embarked:")
print(data['Embarked'].unique())

# Замена строковых значений на булевы для выживших и невыживших
data.loc[:, 'Survived'] = data['Survived'].replace({'Yes': 1, 'No': 0})
data['Survived'] = data['Survived'].astype(int)

# 15. Выбор только числовых столбцов перед применением функции mean()
numeric_data = data.select_dtypes(include='number')
print(numeric_data)

# 16. Вывод средних значений всех числовых переменных по группам Survived
print("\nСредние значения всех числовых переменных по группам Survived:")
print(numeric_data.groupby('Survived').mean())

# 17. Сгруппировка строк в датафрейме в соответствии со значениями переменной Survived и вывод средних значений всех
# количественных переменных по группам
print("\nСредние значения всех количественных переменных по группам Survived:")
print(data.select_dtypes(include='number').groupby('Survived').agg('mean'))

# 18. Сгруппировка строк в датафрейме в соответствии со значениями переменной Sex и сохранение в отдельный датафрейм
# таблицы со средними и медианными значениями переменной Age по группам (мужчины и женщины)
print('\nСредние и медианные значения переменной Age по группам Sex:')
print(data.groupby('Sex')['Age'].agg(['mean', 'median']))

# 19. Приведение всех названий столбцов в датафрейме к нижнему регистру и сохранение изменений
data.columns = data.columns.str.lower()

# 20. Выгрузка итогового датафрейма в файл Titanic-new.csv
data.to_csv('Titanic-new.csv', index=False)
