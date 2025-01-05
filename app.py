import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('dummy_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title("Dummy Model Prediction App")

# User inputs
feature1 = st.number_input("Enter Feature1:")
feature2 = st.number_input("Enter Feature2:")

if st.button("Predict"):
    # Prepare the input data
    input_data = pd.DataFrame({'Feature1': [feature1], 'Feature2': [feature2]})
    prediction = model.predict(input_data)
    st.write(f"Prediction: {prediction[0]}")

