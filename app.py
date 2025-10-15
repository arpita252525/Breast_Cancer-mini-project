import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -----------------------------------------------------------
# 🩺 Breast Cancer Classification Web App
# -----------------------------------------------------------

# Load trained model
model_path = "best_model.pkl"  # Ensure your model file is in the same directory
with open(model_path, "rb") as file:
    model = "/mount/src/breast_cancer-mini-project/app.py"(file)

# App Title
st.title("🩺 Breast Cancer Classification App")
st.write("This app predicts whether a tumor is **Benign (B)** or **Malignant (M)** based on cell nuclei features.")

# Sidebar Inputs
st.sidebar.header("Input Features")
st.sidebar.write("Enter the feature values below:")

# Define feature input fields
def user_input_features():
    battery = st.sidebar.number_input("Mean Radius", 0.0, 50.0, 14.0)
    texture = st.sidebar.number_input("Mean Texture", 0.0, 50.0, 19.0)
    perimeter = st.sidebar.number_input("Mean Perimeter", 0.0, 200.0, 92.0)
    area = st.sidebar.number_input("Mean Area", 0.0, 3000.0, 654.0)
    smoothness = st.sidebar.number_input("Mean Smoothness", 0.0, 1.0, 0.1)
    compactness = st.sidebar.number_input("Mean Compactness", 0.0, 1.0, 0.2)
    concavity = st.sidebar.number_input("Mean Concavity", 0.0, 1.0, 0.3)
    concave_points = st.sidebar.number_input("Mean Concave Points", 0.0, 1.0, 0.15)
    symmetry = st.sidebar.number_input("Mean Symmetry", 0.0, 1.0, 0.2)
    fractal_dimension = st.sidebar.number_input("Mean Fractal Dimension", 0.0, 1.0, 0.06)

    data = {
        'radius_mean': battery,
        'texture_mean': texture,
        'perimeter_mean': perimeter,
        'area_mean': area,
        'smoothness_mean': smoothness,
        'compactness_mean': compactness,
        'concavity_mean': concavity,
        'concave points_mean': concave_points,
        'symmetry_mean': symmetry,
        'fractal_dimension_mean': fractal_dimension
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
input_df = user_input_features()

# Display input
st.subheader("🔍 Input Features")
st.write(input_df)

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_df)
    result = "🧬 **Malignant (M)**" if prediction[0] == 1 else "🌸 **Benign (B)**"
    st.subheader("🎯 Prediction Result:")
    st.success(result)

# Footer
st.markdown("---")
st.caption("Developed by **Arpita Lakhe** | B.Sc. Computer Science Project")
