# src/preprocessing.py
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import joblib
from pathlib import Path

logger = logging.getLogger(__name__)

def preprocess_data(df: pd.DataFrame, test_size: float = 0.2) -> tuple:
    """Preprocess data and save artifacts"""
    logger.info("Preprocessing data...")
    
    # Create models directory if not exists
    Path("models").mkdir(parents=True, exist_ok=True)
    
    X = df.drop('expenses', axis=1)
    y = df['expenses']
    
    # Define transformers
    numerical_features = ['age', 'bmi', 'children']
    categorical_features = ['sex', 'smoker', 'region']
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(), categorical_features)
        ])
    
    # Fit and transform
    X_processed = preprocessor.fit_transform(X)
    
    # Split data after preprocessing
    X_train, X_test, y_train, y_test = train_test_split(
        X_processed, y, test_size=test_size, random_state=42
    )
    
    # Save artifacts
    joblib.dump(preprocessor, "models/preprocessor.joblib")
    joblib.dump((X_train, X_test, y_train, y_test), "models/processed_data.joblib")
    
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    df = pd.read_csv("data/insurance.csv")
    preprocess_data(df)
