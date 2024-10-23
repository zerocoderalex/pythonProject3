import pandas as pd

# df = pd.read_csv('animal.csv')
# print(df.head())
# print(df.info())
# print(df.describe())

df = pd.read_csv('dz.csv')

df.fillna(value=0, inplace=True)
midlsalary = df.groupby('City')['Salary'].mean()

print(midlsalary)

