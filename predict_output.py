import pickle
import numpy as np

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Sample Input (Area in sqft, No of bedrooms)
data = np.array([[2000, 3]])

# Predict Output
prediction = model.predict(data)

print("Predicted House Price:", prediction)

