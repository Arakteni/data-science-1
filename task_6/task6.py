import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer

df = pd.read_csv("titanic.csv")

target = "Survived"

Y = df['Survived']

features = ['Pclass', 'Fare', 'Age', 'Sex']
X = df[features]

X = pd.get_dummies(X, columns=['Sex'])

imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_imputed, Y, test_size=0.2, random_state=42) 

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели на тестовых данных: {accuracy:.2f}")
