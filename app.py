import streamlit as st
import joblib
import pandas as pd

# Load the model
# Load the Random Forest model
model = joblib.load("random_forest_model.pkl")

st.title("Liver Disease Prediction App")

# Input form for user to enter data

def user_input():
    age = st.number_input("Age", min_value=1, max_value=100, value=30)
    sex = st.selectbox("Sex", ["m", "f"])
    albumin = st.number_input("Albumin", value=30.0)
    alkaline_phosphatase = st.number_input("Alkaline Phosphatase", value=60.0)
    alanine_aminotransferase = st.number_input("Alanine Aminotransferase", value=35.0)
    aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", value=45.0)
    bilirubin = st.number_input("Bilirubin", value=1.2)
    cholinesterase = st.number_input("Cholinesterase", value=5000.0)
    cholesterol = st.number_input("Cholesterol", value=200.0)
    creatinina = st.number_input("Creatinine", value=1.0)
    gamma_glutamyl_transferase = st.number_input("Gamma Glutamyl Transferase", value=50.0)
    protein = st.number_input("Protein", value=6.5)
    
    # Create a DataFrame for the input data
    data = {
        'age': age,
        'sex': 0 if sex == 'm' else 1,  # Encoding 'm' as 0 and 'f' as 1
        'albumin': albumin,
        'alkaline_phosphatase': alkaline_phosphatase,
        'alanine_aminotransferase': alanine_aminotransferase,
        'aspartate_aminotransferase': aspartate_aminotransferase,
        'bilirubin': bilirubin,
        'cholinesterase': cholinesterase,
        'cholesterol': cholesterol,
        'creatinina': creatinina,
        'gamma_glutamyl_transferase': gamma_glutamyl_transferase,
        'protein': protein
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
