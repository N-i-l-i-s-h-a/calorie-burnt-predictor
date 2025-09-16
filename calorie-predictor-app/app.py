import streamlit as st
import joblib
import numpy as np
import pandas as pd

# --- MODEL LOADING ---
# Use a try-except block for robustness
try:
    model = joblib.load('calorie_predictor_model.joblib')
except FileNotFoundError:
    st.error("Model file not found. Make sure 'calorie_predictor_model.joblib' is in the same directory.")
    st.stop() # Stop the app from running further

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Calorie Predictor", page_icon="🔥", layout="centered")

# --- PAGE TITLE AND DESCRIPTION ---
st.title("🔥 Calorie Burn Predictor")
st.write("Enter your workout details to estimate the number of calories burned.")
st.write("---")

# --- USER INPUTS in a two-column layout ---
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox('Gender', ('Male', 'Female'))
    age = st.slider('Age', 1, 100, 25)
    duration = st.slider('Workout Duration (minutes)', 1, 240, 30)
    body_temp = st.slider('Body Temperature (°C)', 35.0, 42.0, 38.0, step=0.1)

with col2:
    height = st.number_input('Height (cm)', value=170.0, step=1.0)
    weight = st.number_input('Weight (kg)', value=70.0, step=0.5)
    heart_rate = st.slider('Average Heart Rate (bpm)', 60, 220, 110)

# --- PREDICTION LOGIC ---
if st.button('**Predict Calories Burnt**', use_container_width=True):
    # Convert gender to numerical
    gender_numeric = 0 if gender == 'Male' else 1

    # Create a DataFrame for the input features
    # The column names must match the ones used during model training
    input_data = pd.DataFrame({
        'Gender': [gender_numeric],
        'Age': [age],
        'Height': [height],
        'Weight': [weight],
        'Duration': [duration],
        'Heart_Rate': [heart_rate],
        'Body_Temp': [body_temp]
    })

    # Get prediction
    try:
        prediction = model.predict(input_data)
        st.success(f'## Estimated Calories Burnt: **{prediction[0]:.2f} kcal**')
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")