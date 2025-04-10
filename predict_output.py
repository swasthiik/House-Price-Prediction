import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

# Load the model and label encoder
model = pickle.load(open('output/model.pkl', 'rb'))
label_encoder = pickle.load(open('output/label_encoder.pkl', 'rb'))

# Input data (you can modify this for real-time user input)
area = float(input("Enter area (in sqft): "))
bedrooms = int(input("Enter number of bedrooms: "))
bathrooms = int(input("Enter number of bathrooms: "))
location = input("Enter location (Bangalore, Mumbai, Delhi): ")

# Preprocessing input data
location_encoded = label_encoder.transform([location])[0]
input_data = pd.DataFrame([[area, bedrooms, bathrooms, location_encoded]], columns=['area', 'bedrooms', 'bathrooms', 'location'])

# Predict the price
price = model.predict(input_data)[0]
print(f"Predicted House Price: ₹{price:,.2f}")




