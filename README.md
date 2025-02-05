# Insurance-Premium-Prediction
## Problem Statement:
To give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. I am considering variables as age, sex, BMI, number of children, smoking habits and living region to predict the premium. This can assist a person in concentrating on the health side of an insurance policy rather than the ineffective part.

**Data source**: [Dataset Link](https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction)


## Approach

1. **Data Loading and Initial Checks**:
   - Load the dataset using Pandas.
   - Perform basic checks, including data types of each column and identifying any missing values.

2. **Exploratory Data Analysis (EDA)**:
   - Visualize each predictor (e.g., age, sex, bmi, smoker) against the target variable (insurance premium estimate) to identify relationships.
   - Examine the correlation between features and the target variable using Pearson and Spearman correlation coefficients.
   - Analyze the distribution of the target variable, noting any skewness or deviations from normality.
   - Check for outliers across all features, as they may impact model performance.

3. **Feature Engineering**:
   - Create new features or transform existing ones to better capture the relationships influencing the insurance premium estimates.
   - Consider normalization or standardization where appropriate, especially for models sensitive to feature scales.

4. **Model Building and Testing**:
   - Experiment with various classical machine learning algorithms, including:
     - Multiple Linear Regression
     - Decision Tree Regression
     - Random Forest Regression
     - Gradient Boosting Regression
   - Utilize techniques like GridSearchCV for hyperparameter tuning to find the best configurations for each model.
   - Evaluate model performance using metrics such as RMSE and R-squared on both training and testing datasets.
   - Conduct residual analysis to validate the assumptions of the chosen models.

5. **Model Evaluation**:
   - Compare the performance of all models to identify the one that provides the best balance between accuracy and interpretability.
   - Highlight the key features influencing the insurance premium estimates using feature importance metrics.

6. **Deployment**:
   - Deploy the best-performing model (e.g., Gradient Boosting Regressor) using Flask for the backend, with a user-friendly HTML5 interface for the frontend.
   - Implement logging at each stage of the development and deployment process, storing logs in designated files (e.g., `jupyter_notebook_logs.log` for development and `app_deployment_logs.log` for deployment).

7. **Installation**:
   1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Insurance-Premium-Prediction.git
   cd Insurance-Premium-Prediction
   ```
   2. Create and activate virtual environment:
   ```
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
   3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
8. **Running the Application**:
   1. Start FastAPI Backend:
   
   *In a terminal*:
   ```
   # From project root directory
   uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
   ```
   - API Docs will be available at: http://localhost:8000/docs
   - Backend service: http://localhost:8000

   2. Start Streamlit Frontend:
   
   *In a separate terminal*:
   ```
   # From project root directory
   streamlit run streamlit/app.py
   ```
   - Streamlit app will open in browser at: http://localhost:8501

9. ***Using the Application***:
   1. Streamlit Interface:
   - Fill in the form with your details
   - Click "Predict Premium"
   - View prediction results

   2. Direct API Access:
   ```
   curl -X POST "http://localhost:8000/predict" \
   -H "Content-Type: application/json" \
   -d '{"age": 30, "sex": "male", "bmi": 25.0, "children": 0, "smoker": "no", "region": "southeast"}'
   ```
1. ***Development***:
   1. Training the Model:
   ```
   python src/train.py
   ```

   2. Running Tests:
   ```
   python -m pytest tests/
   
   ```

By following this approach, users can input their individual health details into the web application to receive a quick estimate of their insurance premium.



