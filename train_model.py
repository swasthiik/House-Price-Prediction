import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load Data
data = pd.read_csv('data.csv')

# Drop rows with missing values
data.dropna(inplace=True)

# Encode Location
data['location'] = data['location'].astype('category').cat.codes

# Features & Target
X = data[['area', 'bedrooms', 'bathrooms', 'location']]
y = data['price']

# Model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))





