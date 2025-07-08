import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("titanic.csv")

le = LabelEncoder()
df['Sex_encoder'] = le.fit_transform(df['Sex'])#приведение категориальных признаков

def create_age(age):
    if age < 18:
        return 'Child'
    elif 18 <= age < 60:
        return 'Adult'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].apply(create_age)
df['AgeGroupEncoder'] = le.fit_transform(df['AgeGroup'])#приведение категориальных признаков


imputer = SimpleImputer(strategy='mean')

target = 'Survived'
Y = df[target]
features = ['Pclass', 'Fare', 'AgeGroupEncoder', 'Sex_encoder']
X = df[features]


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "KNN": KNeighborsClassifier(),
    "Random Forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42)
}

results = {}
best_model_name = None
best_score = 0

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    score = accuracy_score(y_test, y_pred)
    results[name] = score
    
    if score > best_score:
        best_score = score
        best_model_name = name

print("Accuracy scores:")
for name, score in results.items():
    print(f"{name}: {score:.4f}")

print(f"\nBest model is {best_model_name} with accuracy {best_score:.4f}")

best_model = models[best_model_name]
y_pred = best_model.predict(X_test_scaled)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Not Survived', 'Survived'],
            yticklabels=['Not Survived', 'Survived'])
plt.title(f'Confusion Matrix for {best_model_name}')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()