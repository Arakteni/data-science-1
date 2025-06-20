import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snus 

df = pd.read_csv('winemag-data_first150k.csv')

rate_country = df['country'].value_counts().head(5).index.tolist()#топ-5 стран по количеству записей

df_top = df[df['country'].isin(rate_country)]#фильтруем данные для топ-5 стран

#создаём boxplot
plt.figure(figsize=(10, 6))
snus.boxplot(data=df_top, x='country', y='points', palette='viridis')
plt.title('Распределение оценок по топ-5 странам')
plt.xlabel('Страна')
plt.ylabel('Оценка')
plt.xticks(rotation = 45)
plt.savefig('winemag-data_first150k-2.png')
plt.show()


num_df = df[['price', 'points']]# Выбираем только числовые столбцы

correl_matrix = num_df.corr()# Вычисляем матрицу корреляции

# Строим heatmap
plt.figure(figsize=(8, 6))
snus.heatmap(correl_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Корреляция между ценой и оценкой')
plt.savefig('winemag-data_first150k-3.png')
plt.show()


# Группируем по странам и вычисляем среднюю цену
avg_price_country = df.groupby('country')['price'].mean().sort_values(ascending=False).head(10)

# Создаем bar plot
plt.figure(figsize=(12, 6))
snus.barplot(x=avg_price_country.index, y=avg_price_country.values, palette='rocket')
plt.title('Средняя цена вина по странам')
plt.xlabel('Страна')
plt.ylabel('Средняя цена')
plt.xticks(rotation=45)
plt.savefig('winemag-data_first150k-4.png')
plt.show()



