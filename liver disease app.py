import streamlit as st
import joblib
import pandas as pd

# Load the Random Forest model
model = joblib.load("liver-disease-model.pkl")

st.title("Liver Disease Prediction App")

# Input form for user to enter data
def user_input():
    age = st.number_input("Age", min_value=1, max_value=100, value=30)
    sex = st.selectbox("Sex", ["m", "f"])
    albumin = st.number_input("Albumin", value=30.0)
    alkaline_phosphatase = st.number_input("Alkaline Phosphatase", value=60.0)
    alanine_aminotransferase = st.number_input("Alanine Aminotransferase", value=35.0)
    # Add more inputs based on your dataset features

    # Create a DataFrame for the input data
    data = {
        'age': age,
        'sex': sex,
        'albumin': albumin,
        'alkaline_phosphatase': alkaline_phosphatase,
        'alanine_aminotransferase': alanine_aminotransferase
    }
    return pd.DataFrame(data, index=[0])

# Get user input
input_data = user_input()

# Display input data
st.write("Input Data:", input_data)

# Button to make predictions
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"Prediction: {'Liver Disease' if prediction[0] == 1 else 'No Liver Disease'}")

