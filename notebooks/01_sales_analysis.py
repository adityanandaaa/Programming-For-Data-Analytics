"""
Example: Sales Data Analysis

This notebook demonstrates:
- Loading sales data
- Basic exploratory data analysis
- Creating visualizations
- Generating insights
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.utils.sample_data import create_sample_dataset
from src.analytics.stats import calculate_statistics, group_and_aggregate
from src.visualization.plots import create_bar_chart, create_histogram

# Create sample sales data
df = create_sample_dataset()

print("Dataset Overview:")
print(df.head(10))

# Basic statistics
print("\nSales Statistics:")
print(calculate_statistics(df, 'Sales'))

# Group by region
print("\nSales by Region:")
print(group_and_aggregate(df, 'Region', {'Sales': 'sum', 'Units': 'mean'}))

# Group by category
print("\nSales by Category:")
print(group_and_aggregate(df, 'Category', {'Sales': 'sum', 'Units': 'mean'}))

print("\nAnalysis complete!")
