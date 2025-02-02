# src/train.py
import logging
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error

logger = logging.getLogger(__name__)

def train_and_evaluate():
    """Train models and evaluate performance"""
    logger.info("Training models...")
    
    try:
        # Load preprocessed data
        X_train, X_test, y_train, y_test = joblib.load("models/processed_data.joblib")
        
        models = {
            'Linear Regression': LinearRegression(),
            'Decision Tree': DecisionTreeRegressor(random_state=42),
            'Gradient Boosting': GradientBoostingRegressor(random_state=42)
        }
        
        results = {}
        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            
            r2 = r2_score(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            
            results[name] = {'R²': r2, 'MAE': mae}
            logger.info("%s - R²: %.3f, MAE: %.2f", name, r2, mae)
            
            # Save best model
            if name == 'Gradient Boosting':
                joblib.dump(model, "models/best_model.joblib")
        
        return results
    
    except Exception as e:
        logger.error("Training failed: %s", e)
        raise

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    train_and_evaluate()