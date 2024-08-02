# train_model.py

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Charger les données
data = pd.read_csv('data.csv')

# Convertir les heures
def time_to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

data['Arrivée'] = data['Arrivée'].apply(time_to_minutes)
data['Départ'] = data['Départ'].apply(time_to_minutes)

# Encodage des variables catégorielles
encoder = OneHotEncoder()
encoded_features = encoder.fit_transform(data[['Type_Service', 'Jour_Semaine', 'Heure']])

# Ajouter les nouvelles features encodées au DataFrame
data = pd.concat([data, pd.DataFrame(encoded_features.toarray(), columns=encoder.get_feature_names_out())], axis=1)
data.drop(['Type_Service', 'Jour_Semaine', 'Heure'], axis=1, inplace=True)

# Convertir tous les noms de colonnes en chaînes de caractères
data.columns = data.columns.astype(str)

# Séparer les features et la cible
X = data.drop(['Durée'], axis=1)
y = data['Durée']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prédire et évaluer
y_pred = model.predict(X_test)
print(f'Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}')

# Sauvegarder le modèle, l'encodeur, et les colonnes
joblib.dump(model, 'model.joblib')
joblib.dump(encoder, 'encoder.joblib')
joblib.dump(X_train.columns, 'train_columns.joblib')  # Save the column names
