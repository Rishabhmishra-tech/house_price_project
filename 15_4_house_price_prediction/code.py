import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("house_price_model.pkl")


# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# Title
st.title("🏠 House Price Prediction")

st.write(
    "Enter the house details below to predict the median house value."
)


# Input fields

longitude = st.number_input(
    "Longitude",
    value=-122.23
)

latitude = st.number_input(
    "Latitude",
    value=37.88
)

housing_median_age = st.number_input(
    "Housing Median Age",
    min_value=1,
    value=30
)

total_rooms = st.number_input(
    "Total Rooms",
    min_value=1,
    value=1000
)

total_bedrooms = st.number_input(
    "Total Bedrooms",
    min_value=1,
    value=200
)

population = st.number_input(
    "Population",
    min_value=1,
    value=500
)

households = st.number_input(
    "Households",
    min_value=1,
    value=200
)

median_income = st.number_input(
    "Median Income",
    min_value=0.0,
    value=5.0
)

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    [
        "<1H OCEAN",
        "INLAND",
        "NEAR OCEAN",
        "NEAR BAY",
        "ISLAND"
    ]
)


# Prediction button

if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "longitude": [longitude],
        "latitude": [latitude],
        "housing_median_age": [housing_median_age],
        "total_rooms": [total_rooms],
        "total_bedrooms": [total_bedrooms],
        "population": [population],
        "households": [households],
        "median_income": [median_income],
        "ocean_proximity": [ocean_proximity]
    })


    # Make prediction
    prediction = model.predict(input_data)


    # Display result
    st.success(
        f"Predicted House Value: ${prediction[0]:,.2f}"
    )
    