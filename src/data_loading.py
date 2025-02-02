# data_loading.py
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def load_data(file_path: str) -> pd.DataFrame:
    """Load insurance dataset from CSV."""
    try:
        df = pd.read_csv(file_path)
        logger.info("Data loaded successfully. Shape: %s", df.shape)
        return df
    except Exception as e:
        logger.error("Failed to load data: %s", e)
        raise

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    df = load_data("data/insurance.csv")
    print(df.head())