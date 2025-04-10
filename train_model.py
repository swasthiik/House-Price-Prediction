import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Sample Data
data = pd.DataFrame({
    'area': [1000, 1200, 1500, 900, 1100],
    'bedrooms': [2, 3, 3, 2, 2],
    'bathrooms': [2, 2, 3, 1, 2],
    'location': ['Delhi', 'Mumbai', 'Chennai', 'Delhi', 'Bangalore'],
    'price': [50, 70, 80, 40, 60]
})

# Encode Location
le = LabelEncoder()
data['location'] = le.fit_transform(data['location'])

# Features & Target
X = data[['area', 'bedrooms', 'bathrooms', 'location']]
y = data['price']

# Train Model
model = LinearRegression()
model.fit(X, y)

# Save Model
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save Label Encoder
with open('model/label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

print("Model & Label Encoder saved successfully!")
