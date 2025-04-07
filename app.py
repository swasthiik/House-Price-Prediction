import streamlit as st
import pickle
import pandas as pd

# Load Model
model = pickle.load(open('model.pkl', 'rb'))

st.title("🏠 House Price Prediction App")

st.markdown("### Enter House Details:")

area = st.number_input("Area (in sq ft)", min_value=100)
bedrooms = st.number_input("No. of Bedrooms", min_value=1, step=1)
bathrooms = st.number_input("No. of Bathrooms", min_value=1, step=1)

if st.button("Predict Price"):
    features = pd.DataFrame([[area, bedrooms, bathrooms]],
                            columns=['Area', 'Bedrooms', 'Bathrooms'])
    prediction = model.predict(features)
    
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")



