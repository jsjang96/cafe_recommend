import pandas as pd
import matplotlib.pyplot as plt

with open('./data/cafe_total.csv',encoding='utf-8-sig') as f:
    total = pd.read_csv(f,index_col=False)
a = total.groupby(['시'])['매장명'].describe(include='all') # 요약보기
print(a.value_counts().sort_values())
b = total.groupby(['시'])['매장명'].value_counts()

plt.rc('font', family='Malgun Gothic')
plt.rcParams.update({'font.size': 14})
b.unstack().plot.bar()
plt.show()