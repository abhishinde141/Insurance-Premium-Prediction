import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessor
MODEL_PATH = "models/best_model.joblib"
PREPROCESSOR_PATH = "models/preprocessor.joblib"

try:
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    model = joblib.load(MODEL_PATH)
    # st.success("✅ Model and Preprocessor loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Create form
st.title("🚑 Health Insurance Premium Predictor")
st.markdown("""
Predict your health insurance costs based on your profile.
""")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
        children = st.number_input("Children", min_value=0, max_value=10, value=0)
    
    with col2:
        sex = st.selectbox("Sex", ["male", "female"])
        smoker = st.selectbox("Smoker", ["yes", "no"])
        region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])
    
    submitted = st.form_submit_button("Predict Premium 💰")
    
    if submitted:
        # Prepare input data as a DataFrame
        input_data = pd.DataFrame({
            "age": [age],
            "sex": [sex],
            "bmi": [bmi],
            "children": [children],
            "smoker": [smoker],
            "region": [region]
        })

        # Make prediction
        try:
            processed_input = preprocessor.transform(input_data)
            prediction = model.predict(processed_input)
            st.success(f"Predicted Insurance Premium: **${prediction[0]:,.2f}**")
        except Exception as e:
            st.error(f"❌ Prediction Error: {e}")

# Footer section
st.markdown("---")
st.markdown(
    """
    **Developed by Abhijeet Shinde**
    [![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/abhishinde141)
    """
)
st.markdown("Made with ❤️ using Streamlit 🚀")
