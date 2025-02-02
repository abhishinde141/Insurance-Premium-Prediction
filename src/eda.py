# eda.py
import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

logger = logging.getLogger(__name__)

def perform_eda(df: pd.DataFrame) -> None:
    """Generate EDA plots and summaries."""
    logger.info("Performing EDA...")
    
    # Summary statistics
    print(df.describe())
    
    # Distribution of target variable
    plt.figure(figsize=(10, 6))
    sns.histplot(df['expenses'], kde=True)
    plt.title("Distribution of Insurance Expenses")
    plt.savefig("reports/expenses_distribution.png")
    
    # Correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("reports/correlation_heatmap.png")
    
    # Categorical variable analysis
    categorical = ['sex', 'smoker', 'region']
    for col in categorical:
        plt.figure()
        sns.boxplot(x=col, y='expenses', data=df)
        plt.savefig(f"reports/{col}_vs_expenses.png")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    df = pd.read_csv("data/insurance.csv")
    perform_eda(df)