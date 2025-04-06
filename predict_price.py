import pickle
import numpy as np

# Loading the trained model from 'model.pkl'
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to predict house price
def predict_price(area, bedrooms, age):
    features = np.array([[area, bedrooms, age]])
    predicted_price = model.predict(features)
    return predicted_price[0]

# Taking user input
area = float(input("Enter the area of the house in square feet: "))
bedrooms = int(input("Enter the number of bedrooms: "))
age = int(input("Enter the age of the house in years: "))

# Making prediction
predicted_price = predict_price(area, bedrooms, age)
print(f"Predicted House Price: ₹{predicted_price:,.2f}")
