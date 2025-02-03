import os
from setuptools import setup, find_packages

setup(
    name="insurance_prediction",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # your dependencies here
    ],
)

# Define project structure
folders = [
    "data",
    "models",
    "src",
    "tests",
    "reports",
    "reports/figures",
    "logs",
    ".github/workflows"
]

# Define files to create in each folder
files = [
    "README.md",
    "requirements.txt",
    "Dockerfile",
    "data/insurance.csv",
    "models/preprocessor.joblib",
    "models/best_model.joblib",
    "src/__init__.py",
    "src/data_loading.py",
    "src/eda.py",
    "src/preprocessing.py",
    "src/train.py",
    "src/app.py",
    "src/streamlit.py",
    "tests/__init__.py",
    "tests/test_model.py",
    "logs/app.log",
    "logs/logging_config.log",
    ".github/workflows/deploy.yml"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path in files:
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass

print("Project structure created successfully!")
