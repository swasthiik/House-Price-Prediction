import pickle
import pandas as pd

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# User Input
area = float(input("Enter Area (sq ft): "))
bedrooms = float(input("Enter No. of Bedrooms: "))
bathrooms = float(input("Enter No. of Bathrooms: "))

# Prediction
features = pd.DataFrame([[area, bedrooms, bathrooms]],
                        columns=['Area', 'Bedrooms', 'Bathrooms'])

prediction = model.predict(features)

# Output in ₹
print(f"\nEstimated House Price: ₹ {prediction[0]:,.2f}")

