import pandas as pd
import sklearn.preprocessing import MinMaxScaler
import sklearn.preprocessing import LabelEncoder

df = pd.read_csv("train.csv")#чтение и преобразовывание датасета в таблицу DataFrame

df = MinMaxScaler(df['LotArea', 'GrLivArea'])#приведение значений к одному масштабу от [0, 1]

automobile_dataset = pd.read_csv("Automobile_data.csv")#чтение и преобразовывание датасета в таблицу DataFrame

automobile_dataset['fuel_type_encoded'] = LabelEncoder().fit_transform(automobile_dataset['fuel_type'])#преобразовывание категориальных признаков 

df1 = pd.read_csv("titanic.csv")

def create_age_group(age):#фильтрация по возрасту
    if age < 18:
        return 'Child'
    elif 18 <= age < 60:
        return 'Adult'
    else:
        return 'Senior'
    
df1['AgeGroup'] = df1['Age'].apply(create_age_group)#запись новых значений в новый столбец на основе возраста 