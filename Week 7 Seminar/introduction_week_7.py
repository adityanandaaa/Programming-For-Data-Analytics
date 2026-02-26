import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# --- Setup Paths ---
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "data source")
output_dir = os.path.join(script_dir, "visualizations")

# Ensure directories exist
os.makedirs(data_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

print("--- Week 7: Introduction to Titanic Dataset ---")

# --- Dataset Description ---
"""
Variable Notes:
- pclass: A proxy for socio-economic status (SES). 1st = Upper, 2nd = Middle, 3rd = Lower.
- age: Age is fractional if less than 1. If estimated, it is in the form xx.5.
- sibsp: Number of siblings/spouses aboard.
- parch: Number of parents/children aboard.
"""

# Load Dataset
# Note: Assuming titanic_train.csv is in the 'data source' folder.
# If it's missing, we use seaborn's built-in one for demonstration.
try:
    file_path = os.path.join(data_dir, "titanic_train.csv")
    if os.path.exists(file_path):
        titanic = pd.read_csv(file_path)
        print("Loaded dataset from CSV.")
    else:
        titanic = sns.load_dataset("titanic")
        print("CSV not found, loaded built-in seaborn titanic dataset.")
except Exception as e:
    print(f"Error loading data: {e}")
    titanic = sns.load_dataset("titanic")

# Basic Overview
print("\n--- First 5 Rows ---")
print(titanic.head())

print("\n--- Summary Info ---")
print(f"Shape: {titanic.shape}")
print(f"\nColumn Names: {list(titanic.columns)}")
print(f"\nData Types:\n{titanic.dtypes}")

print("\n--- Missing Values Audit ---")
missing = titanic.isnull().sum()
if missing.any():
    print(missing[missing > 0])
else:
    print("No missing values.")

# Basic Visualization: Survival Rate by Class
try:
    # Determine correct column names based on dataset source
    class_col = None
    if "Pclass" in titanic.columns:
        class_col = "Pclass"
    elif "pclass" in titanic.columns:
        class_col = "pclass"
    elif "class" in titanic.columns:
        class_col = "class"
    
    survival_col = "Survived" if "Survived" in titanic.columns else "survived"
    
    if class_col is None:
        print("Error: Could not find class column.")
    else:
        # Drop missing values for visualization
        titanic_clean = titanic[[class_col, survival_col]].dropna()
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=class_col, y=survival_col, data=titanic_clean)
        plt.title("Survival Rate by Passenger Class")
        plot_path = os.path.join(output_dir, "survival_by_class.png")
        plt.savefig(plot_path, dpi=100, bbox_inches="tight")
        print(f"\nPlot saved to: {plot_path}")
        plt.close()
except Exception as e:
    print(f"Error creating visualization: {e}")
    plt.close()
