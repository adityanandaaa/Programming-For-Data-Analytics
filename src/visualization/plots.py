"""
Visualization module for creating charts and plots.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def create_histogram(df, column, title=None, bins=30):
    """Create a histogram for a column."""
    plt.figure(figsize=(10, 6))
    plt.hist(df[column], bins=bins, edgecolor='black', alpha=0.7)
    plt.title(title or f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.3)
    return plt


def create_scatter_plot(df, x_col, y_col, title=None):
    """Create a scatter plot."""
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_col], df[y_col], alpha=0.6)
    plt.title(title or f'{x_col} vs {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True, alpha=0.3)
    return plt


def create_bar_chart(df, x_col, y_col, title=None):
    """Create a bar chart."""
    plt.figure(figsize=(10, 6))
    df.set_index(x_col)[y_col].plot(kind='bar', edgecolor='black', alpha=0.7)
    plt.title(title or f'{y_col} by {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    return plt


def create_heatmap(df, title=None):
    """Create a correlation heatmap."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', center=0)
    plt.title(title or 'Correlation Heatmap')
    return plt
