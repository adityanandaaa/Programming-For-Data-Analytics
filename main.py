"""
Main entry point for Programming for Data Analytics project.

This script demonstrates basic data analysis workflows including:
- Loading data
- Basic statistics
- Data visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.utils.sample_data import create_sample_dataset

def main():
    """Main function to run data analysis examples."""
    print("=" * 60)
    print("Programming for Data Analytics - Main Example")
    print("=" * 60)
    
    # Create sample dataset
    print("\n1. Creating sample dataset...")
    df = create_sample_dataset()
    print(f"   Dataset shape: {df.shape}")
    print(f"   Columns: {', '.join(df.columns.tolist())}")
    
    # Display basic statistics
    print("\n2. Basic Statistics:")
    print(df.describe())
    
    # Data info
    print("\n3. Dataset Information:")
    print(df.info())
    
    # Show first few rows
    print("\n4. First few rows:")
    print(df.head())
    
    print("\n" + "=" * 60)
    print("Analysis complete! Check the notebooks/ folder for more examples.")
    print("=" * 60)

if __name__ == "__main__":
    main()
