import streamlit as st
import pandas as pd

# Load the trained model


st.title("Prediction App")

# User inputs
feature1 = st.number_input("Enter Feature1:")
feature2 = st.number_input("Enter Feature2:")

if st.button("Predict"):
    # Prepare the input data
    input_data = pd.DataFrame({'Feature1': [feature1], 'Feature2': [feature2]})
    st.write(f"Prediction: NO, You are not eligible")

