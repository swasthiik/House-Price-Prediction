import streamlit as st
import pickle
import pandas as pd

# Load Model
model = pickle.load(open('model.pkl', 'rb'))

# Location Encoding Same As Training
location_dict = {'Mumbai': 2, 'Delhi': 1, 'Bengalore': 0}

st.title("House Price Prediction App")

area = st.number_input('Area (in sqft)')
bedrooms = st.number_input('Bedrooms', step=1)
bathrooms = st.number_input('Bathrooms', step=1)
location = st.selectbox('Location', list(location_dict.keys()))

if st.button('Predict'):
    loc_code = location_dict[location]
    input_data = pd.DataFrame([[area, bedrooms, bathrooms, loc_code]], 
                               columns=['area', 'bedrooms', 'bathrooms', 'location'])
    prediction = model.predict(input_data)
    st.success(f'Predicted House Price: ₹ {round(prediction[0], 2)}')
