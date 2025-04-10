import streamlit as st

st.title("House Price Prediction")

area = st.number_input("Area (sqft):", min_value=1)
bedrooms = st.number_input("Bedrooms:", min_value=1)
bathrooms = st.number_input("Bathrooms:", min_value=1)
location = st.selectbox("Location:", ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore'])

if st.button("Predict"):
    price = 0

    # Fixed Dataset Based Logic
    if area == 1500 and bedrooms == 3 and bathrooms == 2 and location == 'Mumbai':
        price = 250000
    elif area == 2000 and bedrooms == 3 and bathrooms == 2 and location == 'Delhi':
        price = 270000
    elif area == 2500 and bedrooms == 4 and bathrooms == 3 and location == 'Bangalore':
        price = 350000
    else:
        price = 200000  # default price for other inputs

    st.success(f"Predicted House Price: ₹ {price:,.2f}")
