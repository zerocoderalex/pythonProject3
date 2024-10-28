from idlelib.iomenu import encoding

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'prices.csv'

data = pd.read_csv(file_path, encoding='utf-16')


prices = data['Цена']
average_price = prices.mean()
print(f'Средняя цена: {average_price}')

plt.hist(prices, bins=10, edgecolor='black')

plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

plt.show()






