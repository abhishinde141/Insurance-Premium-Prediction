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

<<<<<<< HEAD
By following this approach, users can input their individual health details into the web application to receive a quick estimate of their insurance premium.
=======
By following this approach, users can input their individual health details into the web application to receive a quick estimate of their insurance premium.
>>>>>>> 8da9ee9 (Update README.md)
