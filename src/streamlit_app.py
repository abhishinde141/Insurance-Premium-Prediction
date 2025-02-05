import streamlit as st
import requests

# Configure API endpoint
API_URL = "http://localhost:8000/predict"

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
        # Prepare input data
        input_data = {
            "age": age,
            "sex": sex,
            "bmi": bmi,
            "children": children,
            "smoker": smoker,
            "region": region
        }
        
        # Make API call
        try:
            response = requests.post(API_URL, json=input_data)
            if response.status_code == 200:
                result = response.json()
                st.success(f"Predicted Insurance Premium: **${result['predicted_charges']:,.2f}**")
            else:
                st.error(f"API Error: {response.text}")
        
        except requests.exceptions.RequestException as e:
            st.error(f"Connection Error: {str(e)}")

# Footer section
st.markdown("---")
st.markdown(
    """
    **Developed by Abhijeet Shinde**
    [![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/abhishinde141)
    """
)
st.markdown("Made with ❤️ using Streamlit 🚀")
