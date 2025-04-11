import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

st.title("House Price Prediction (ML Model)")

area = st.number_input("Area (sqft):", min_value=1)
bedrooms = st.number_input("Bedrooms:", min_value=1)
bathrooms = st.number_input("Bathrooms:", min_value=1)
location = st.selectbox("Location:", ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore'])

location_dict = {
    'Delhi': 0,
    'Mumbai': 2,
    'Chennai': 1,
    'Kolkata': 3,
    'Bangalore': 4
}

if st.button("Predict"):
    input_data = np.array([[area, bedrooms, bathrooms, location_dict[location]]])
    price = model.predict(input_data)[0]
    st.success(f"Predicted House Price: ₹ {price:,.2f}")
