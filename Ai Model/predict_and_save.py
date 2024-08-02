import joblib
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


# Function to convert time to minutes
def time_to_minutes(time_str):
    try:
        h, m = map(int, time_str.split(':'))
        return h * 60 + m
    except ValueError:
        return None  # Handle cases where time_str is not in the correct format

# Load the trained model and encoder
model = joblib.load('model.joblib')
encoder = joblib.load('encoder.joblib')

# Load the input data from CSV
input_data = pd.read_csv('data.csv')

# Convert time columns from 'HH:MM' to minutes
input_data['Arrivée'] = input_data['Arrivée'].apply(time_to_minutes)
input_data['Départ'] = input_data['Départ'].apply(time_to_minutes)

# Handle missing values by filling with a placeholder
input_data.fillna({'Type_Service': 'Unknown', 'Jour_Semaine': 'Unknown', 'Heure': 'Unknown'}, inplace=True)

# Apply one-hot encoding to categorical features
encoded_features = encoder.transform(input_data[['Type_Service', 'Jour_Semaine', 'Heure']])
encoded_df = pd.DataFrame(encoded_features.toarray(), columns=encoder.get_feature_names_out())

# Concatenate encoded features with the input data
input_data_encoded = pd.concat([input_data.drop(columns=['Type_Service', 'Jour_Semaine', 'Heure']), encoded_df], axis=1)

# Ensure the DataFrame columns match the columns used during training
# Get the columns used during training from model's feature importances
train_columns = joblib.load('train_columns.joblib')  # Save this during training and load it here

# Reindex the DataFrame to match the training data
input_data_encoded = input_data_encoded.reindex(columns=train_columns, fill_value=0)

# Make predictions using the loaded model
predictions = model.predict(input_data_encoded)

# Add predictions to the original DataFrame
input_data['Predicted_Durée'] = predictions

# Save the results to a new CSV file
input_data.to_csv('predictions_results.csv', index=False)

print("Predictions saved to 'predictions_results.csv'")
