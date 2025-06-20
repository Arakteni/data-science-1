import pandas as pd
import scipy.stats

df = pd.read_csv('winemag-data_first150k.csv')

'''
фильтруем данные и оставляем в таблице DateFrame данные 
из столбца 'country' и из строк 'France','Italy''''
filtr_df = df[df['country'].isin(['France', 'Italy'])]

'''
группируем данные по какой-то стране и высчитываем медианное значение,
данные из столбца 'country' с определенными значениями(в данном случае 'France','Italy')
и пересечения со столбцом 'price' в одноименных строках будут являться группой'''
median_price = filtr_df.groupby('country')['price'].median()


'''фильтрует данные столбца 'country' и 
оставляет строки с данными о нужной стране(в данном случае USA)'''
pendosia_df = df[df['country'] == 'USA']

'''
высчитывает среднее отклонение строк 'USA'
в столбце 'points''''
std_usa = pendosia_df['points'].std()

'''
фильтруем данные столбца 'country' и
оставляем строки 'France' и
высчитываем медианное значение рейтинга вин Франции'''
median_points_France = df[df['country'].isin(['France'])].groupby('country')['points'].median()

'''
фильтруем данные столбца 'country' и
оставляем строки 'Italy' и
высчитываем медианное значение рейтинга вин Франции'''
median_points_Italy = df[df['country'].isin(['Italy'])].groupby('country')['points'].median()

median_points_France > median_points_Italy:
