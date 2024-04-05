import pandas as pd
import matplotlib.pyplot as plt

# Загрузка базы данных из файла Titanic.csv
data = pd.read_csv("Titanic.csv")

# Загрузка базы данных с PassengerId в качестве индекса
data_indexed = pd.read_csv("Titanic.csv", index_col="PassengerId")

# Удаление строк с пропущенными значениями
data.dropna(inplace=True)

# Задание 3: Вывод сводной информации
print(data.info())

# Задание 4: Сводная статистическая информация
print(data.describe())

# Задание 5: Гистограмма для переменной Возраст (Age)
plt.hist(data['Age'], color='red')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()

# Задание 6: Описательные статистики для столбца Стоимость билета (Fare)
print(data['Fare'].describe())

# Задание 7: Названия столбцов в виде списка
print(data.columns.tolist())

# Задание 8: Переименование столбца Pclass в Class
data.rename(columns={'Pclass': 'Class'}, inplace=True)

# Задание 9: Выборка всех строк с женским полом
female = data[data['Sex'] == 'female']

# Задание 10: Выборка выживших мужчин младше 32 лет
Ymale = data[(data['Survived'] == 1) & (data['Sex'] == 'male') & (data['Age'] < 32)]

# Задание 11: Выборка пассажиров 1 или 2 класса
class_12 = data[data['Class'].isin([1, 2])]

# Задание 12: Выборка выживших пассажиров 1 или 2 класса
survived_class_12 = data[(data['Survived'] == 1) & data['Class'].isin([1, 2])]

# Задание 13: Добавление столбца Female
data['Female'] = (data['Sex'] == 'female').astype(int)

# Задание Группировка 1: Уникальные значения в столбце Embarked
print(data['Embarked'].unique())

# Задание Группировка 2: Группировка по Survived и вывод средних значений
print(data.groupby('Survived').mean())

# Задание Группировка 3: Группировка по Sex и вывод средних и медианных значений Age
grouped_sex = data.groupby('Sex')['Age'].agg(['mean', 'median'])
print(grouped_sex)

# Приведение названий столбцов к нижнему регистру
data.columns = data.columns.str.lower()

# Выгрузка датафрейма в файл Titanic-new.csv
data.to_csv('Titanic-new.csv')
