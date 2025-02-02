# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class InsuranceData(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Insurance Premium Prediction API!"}

@app.post("/predict")
def predict(data: InsuranceData):
    """Predict insurance expenses"""
    try:
        # Load artifacts
        preprocessor = joblib.load("models/preprocessor.joblib")
        model = joblib.load("models/best_model.joblib")
        
        # Create DataFrame from input
        input_df = pd.DataFrame([data.dict()])
        
        # Preprocess and predict
        processed_input = preprocessor.transform(input_df)
        prediction = model.predict(processed_input)
        
        return {"predicted_charges": float(prediction[0])}
    
    except Exception as e:
        return {"error": str(e)}