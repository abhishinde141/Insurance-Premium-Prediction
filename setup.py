import os

# Define project structure
folders = [
    "data",
    "models",
    "src",
    "tests",
    "logs"
]

# Define files to create in each folder
files = [
    r"README.md",
    r"requirements.txt",
    r"Dockerfile",
    r"data/insurance.csv",
    r"models/preprocessor.joblib",
    r"models/best_model.joblib",
    r"src/data_loading.py",
    r"src/eda.py",
    r"src/preprocessing.py",
    r"src/train.py",
    r"src/app.py",
    r"tests/test_model.py",
    r"logs/app.log"
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
