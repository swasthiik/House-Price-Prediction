import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# Sample house data: area vs price
data = {
    'Area': [1000, 1500, 1800, 2400, 3000],
    'Price': [300000, 450000, 500000, 600000, 650000]
}

df = pd.DataFrame(data)
print(df)
# Create model
model = LinearRegression()

# Split data into X (features) and y (target)
X = df[['Area']]
y = df['Price']

# Fit the model
model.fit(X, y)

# Predict price for a new area
area = 2000
predicted_price = model.predict([[area]])
print(f"Predicted price for {area} sq.ft = ₹{int(predicted_price[0])}")
# Plot data and prediction line
plt.scatter(X, y, color='blue', label='Actual Prices')
plt.plot(X, model.predict(X), color='red', label='Prediction Line')
plt.xlabel('Area (sq.ft)')
plt.ylabel('Price (₹)')
plt.title('House Price Prediction')
plt.legend()
plt.grid(True)
plt.show()
