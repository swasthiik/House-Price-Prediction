import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('output/model.pkl', 'rb'))
label_encoder = pickle.load(open('output/label_encoder.pkl', 'rb'))

st.title("House Price Prediction")
st.markdown("Enter the details below to predict the house price.")

area = st.number_input("Area (in sqft):", min_value=1, step=1)
bedrooms = st.number_input("Bedrooms:", min_value=1, step=1)
bathrooms = st.number_input("Bathrooms:", min_value=1, step=1)
location = st.selectbox("Location:", ["Mumbai", "Pune", "Delhi", "Bangalore"])

if st.button("Predict"):
    loc_encoded = label_encoder.transform([location])[0]

    input_data = np.array([[area, bedrooms, bathrooms, loc_encoded]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Price: ₹ {prediction[0]:,.2f}")


