"""
Utility functions for data manipulation and analysis.
"""

import pandas as pd
import numpy as np


def load_csv(filepath):
    """Load data from CSV file."""
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded data from {filepath}")
        return df
    except FileNotFoundError:
        print(f"Error: File {filepath} not found")
        return None


def get_basic_stats(df):
    """Get basic statistics from a DataFrame."""
    return {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'summary': df.describe().to_dict()
    }


def remove_missing_values(df, threshold=0.5):
    """Remove columns with missing values above threshold."""
    missing_ratio = df.isnull().sum() / len(df)
    cols_to_drop = missing_ratio[missing_ratio > threshold].index
    return df.drop(columns=cols_to_drop)


def normalize_column(df, column):
    """Normalize a column to 0-1 range."""
    min_val = df[column].min()
    max_val = df[column].max()
    return (df[column] - min_val) / (max_val - min_val)


def create_sample_dataset():
    """Create a sample dataset for demonstration."""
    np.random.seed(42)
    data = {
        'Date': pd.date_range('2024-01-01', periods=100),
        'Sales': np.random.randint(1000, 5000, 100),
        'Units': np.random.randint(10, 100, 100),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
        'Category': np.random.choice(['Electronics', 'Clothing', 'Food'], 100)
    }
    return pd.DataFrame(data)
