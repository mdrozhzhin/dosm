"""
Гипотеза:
Курс Ethereum имеет положительную корреляцию с общим уровнем активности
децентрализованных финансов (DeFi) на блокчейне Ethereum.

Аргументы:
1. Рост использования DeFi-платформ: Увеличение объема операций на таких платформах, как Uniswap, Aave, Compound,
требует активов, чаще всего в ETH, что повышает спрос.
2. Транзакционные сборы: Повышенная активность на блокчейне Ethereum ведет к росту комиссий, которые оплачиваются в ETH.
Это может подстегнуть рынок и инвесторов, ожидающих роста курса.
3. Количество заблокированных средств (TVL): С ростом TVL (Total Value Locked) в DeFi-платформах происходит увеличение
количества ETH, заблокированного в смарт-контрактах, что снижает доступное предложение на рынке, потенциально повышая
курс.
"""


import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Getting historical data about Ethereum's exchange rate from CoinGecko
def get_eth_price():
    url = 'https://api.coingecko.com/api/v3/coins/ethereum/market_chart'
    params = {'vs_currency': 'usd', 'days': '365'}
    response = requests.get(url, params=params)
    data = response.json()
    prices = data['prices']
    def_df_eth = pd.DataFrame(prices, columns=['timestamp', 'Price'])
    def_df_eth['timestamp'] = pd.to_datetime(def_df_eth['timestamp'], unit='ms')
    return def_df_eth

# Getting TVL for DeFi by DeFiLlama API
def get_defi_tvl():
    url = 'https://api.llama.fi/charts'
    response = requests.get(url)
    data = response.json()
    def_df_tvl = pd.DataFrame(data)
    def_df_tvl['date'] = pd.to_datetime(def_df_tvl['date'], unit='s')
    def_df_tvl = def_df_tvl.rename(columns={'totalLiquidityUSD': 'TVL'})
    return def_df_tvl[['date', 'TVL']]


df_eth = get_eth_price()
df_tvl = get_defi_tvl()

# Merging two datasets along the time axis
df_combined = pd.concat([df_eth, df_tvl], axis=1)

# Creating MultiIndex with levels: (date, metric)
df_multiindex = pd.concat([df_eth, df_tvl], keys=['ETH Price', 'DeFi TVL'], axis=1)
df_multiindex.columns.names = ['Metric', 'Value']

# Output tables with MultiIndex
print("Table with MultiIndex:")
print(df_multiindex.head(20))

# Merge datasets
df = pd.merge(df_eth, df_tvl, left_on='timestamp', right_on='date', how='inner')
df.drop(columns=['date'], inplace=True)

# Correlation calculation
correlation = df['Price'].corr(df['TVL'])
print(f"Correlation between Ethereum price and TVL: {correlation}")

# Graphs visualization
sns.jointplot(x='Price', y='TVL', data=df, kind='reg')
plt.title('Correlation between Ethereum price and TVL')
plt.show()

"""
Как мы можем наблюдать точечной диаграмме с линейной регрессией, линия имеет положительный наклон, а
также мы можем обратить внимание на вывод расчёта корелляции между стоимостью ETH и TVL.
Вывод:
Гипотеза доказана.
"""