# test_model.py
import pytest
from sklearn.metrics import r2_score
from src.train import train_and_evaluate
import joblib

def test_model_performance():
    X_train, X_test, y_train, y_test = joblib.load("processed_data.joblib")
    results = train_and_evaluate(X_train, X_test, y_train, y_test)
    assert results['Gradient Boosting']['R²'] > 0.8