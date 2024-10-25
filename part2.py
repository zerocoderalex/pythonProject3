import pandas as pd
import matplotlib.pyplot as plt
from rfc3986.abnf_regexp import IQUERY_RE

data = {'value': [1,2,4,4,4,5,6,7,7,7,8,9,10,57]}

df = pd.DataFrame(data)

df.boxplot(column='value')
plt.show()

Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1

downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]

df_new.boxplot(column='value')
plt.show()