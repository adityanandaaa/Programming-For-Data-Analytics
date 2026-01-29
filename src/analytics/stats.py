"""
Analytics module for data analysis operations.
"""

import pandas as pd
import numpy as np


def calculate_statistics(df, column):
    """Calculate comprehensive statistics for a column."""
    return {
        'mean': df[column].mean(),
        'median': df[column].median(),
        'std_dev': df[column].std(),
        'min': df[column].min(),
        'max': df[column].max(),
        'quartile_25': df[column].quantile(0.25),
        'quartile_75': df[column].quantile(0.75)
    }


def group_and_aggregate(df, groupby_col, agg_dict):
    """Group data and apply aggregation functions."""
    return df.groupby(groupby_col).agg(agg_dict)


def correlation_analysis(df, numeric_only=True):
    """Calculate correlation matrix."""
    return df.corr(numeric_only=numeric_only)
