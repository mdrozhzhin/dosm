import requests # Для работы с HTTP-запросами
from bs4 import BeautifulSoup # Извлечение данных из HTML
import pandas as pd # Для DataFrame и манипуляции/управления данными
import seaborn as sns # Для визуализации данных
import matplotlib.pyplot as plt # Построение графиков из данных
import re # Для облегчения жизни и снижения самостоятельной писанины функций
from matplotlib.ticker import FuncFormatter # Класс для создания пользовательских функций на осях


url = "https://ru.wikipedia.org/wiki/Список_стран_по_населению"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())

table = soup.find('table', {'class': 'standard sortable'})

rows = table.find_all('tr') # Ищем табличные строки
data = []

for row in rows:
    cells = row.find_all(['th', 'td'])
    cells = [cell.get_text(strip=True) for cell in cells]
    data.append(cells)

print(data)

df = pd.DataFrame(data[1:], columns=[header.get_text(strip=True) for header in rows[0].find_all('th')])
print(df.head())

df['Население'] = df['Население'].apply(lambda x: float(re.sub(r'\D', '', x)))
print(df['Население'].head())


def millions_formatter(x, _):
    return f'{x / 1_000_000:.1f} млн.'

plt.figure(figsize=(10, 8))
sns.barplot(x='Страна', y='Население', data=df.head(10))

plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))

plt.ylim(0, df['Население'].max() * 1.1)
plt.xticks(rotation=90)
plt.title('Население первых 10 стран (в миллионах)')

for index, value in enumerate(df['Население'].head(10)):
    plt.text(index, value, f'{value / 1_000_000:.1f} млн.', ha='center', va='bottom')

plt.show()
