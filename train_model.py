# train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample Data (Area, Bedrooms, Bathrooms, Price)
data = {
    'Area': [1000, 1500, 2000, 2500, 3000],
    'Bedrooms': [2, 3, 3, 4, 4],
    'Bathrooms': [1, 2, 2, 3, 3],
    'Price': [5000000, 7000000, 9000000, 12000000, 15000000]
}

df = pd.DataFrame(data)

# Features & Target
X = df[['Area', 'Bedrooms', 'Bathrooms']]
y = df['Price']

# Model Training
model = LinearRegression()
model.fit(X, y)

# Save Model
pickle.dump(model, open('model.pkl', 'wb'))

print("Model trained successfully with 3 Features & Saved as model.pkl")
