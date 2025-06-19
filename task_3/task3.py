import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('winemag-data_first150k.csv')#чтение файла и преобразовывание файла в таблицу DataFrame

'''
value_counts() - метод подсчитывающий количество уникальных значений столбца
head() - берёт первые 20 строк из value_counts
index - атрибут возвращающий индексы строк после value_counts'''
rating_country = df['country'].value_counts().head(20).index#20 чаще всего встречающихся стран в таблице

#isin() - метод проверяющий содержится ли каждое значение столбца 'country' в 'rating_country'
filter_df = df[df['country'].isin(rating_country)]#оставляет только те значения столбца 'country', которые присутствуют в 'rating_country'

#figsize - функция задающая размер графического окна(в дюймах)
plt.figure(figsize = (12, 6))#создаёт новое графическе окно размером 12 на 6 дюймов
'''
hist() - функция для построения диаграммы
bins - параметр разбивающий диапазон цен на указанное количество интервалов
edgecolor - цвет границ столбцов'''
plt.hist(filter_df['price'], bins = 30, edgecolor = 'black')#построение гистограммы

plt.title('Распредения цен')#создание заголовка
plt.xlabel('Цена')#подпись оси X
plt.ylabel('Количество')#подпись оси Y
plt.grid(True)#включает сетку для удобства чтения графика

plt.savefig('winemag-data_first150k.png')
plt.show()


plt.figure(figsize=(10, 6))#создаёт новое графическе окно размером 10 на 6 дюймов

'''
scatter - функция создающая график из точек
первый аргумент - ось X
второй аргумент - ось Y
третий аргумент - прозрачность точек(0-прозрачные, 1-непрозрачные)'''
plt.scatter(df['price'], df['points'], alpha = 0.5)#создание точечного графика

plt.title('Зависимость рейтинга от цены')#создание заголовка графика
plt.xlabel('Цена')#обозначение оси X
plt.ylabel('Рейтинг')#обозначение оси y

plt.savefig('winemag-data_first150k-2.png')
plt.show()
