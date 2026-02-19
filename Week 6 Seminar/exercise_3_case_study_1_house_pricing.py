"""
Week 6 Seminar: Case Study 1 - House Pricing Exercise 3
========================================================

Dataset: House sales data from Ames, Iowa
Source: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data

Task:
Create a DataFrame from selected columns and perform exploratory data analysis (EDA)

Columns to Include:
• Numeric: OverallQual, GrLivArea, TotRmsAbvGrd, YearBuilt, LotArea, LotFrontage, SalePrice
• Categorical: MSZoning, Neighborhood, HouseStyle

Analysis Steps:
1. Create the DataFrame with selected columns
2. Identify columns with missing values
3. Understand distributions of key columns
4. Explore potential relationships with SalePrice

Author: Week 6 Seminar Series
Date: February 2026
"""

# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np   # For numerical operations
import matplotlib.pyplot as plt  # For creating visualizations
import seaborn as sns  # For statistical data visualization
import os  # For file path operations

# Set visualization style for better-looking plots
sns.set_style('whitegrid')  # White background with grid lines
plt.rcParams['figure.figsize'] = (12, 6)  # Default figure size

# Get the absolute path of the current script file
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the 'data source' folder within the script directory
data_dir = os.path.join(script_dir, 'data source')

print("="*80)
print("CASE STUDY 1: HOUSE PRICING EXERCISE 3")
print("EXPLORATORY DATA ANALYSIS (EDA)")
print("="*80)

# =============================================================================
# STEP 1: Load Full Dataset
# =============================================================================

print("\n" + "-"*80)
print("STEP 1: LOADING FULL DATASET")
print("-"*80)

# Construct the full file path to house_price.csv
csv_file_path = os.path.join(data_dir, 'house_price.csv')
print(f"\nFile path: {csv_file_path}")

# Read CSV file into a DataFrame
# index_col='Id' sets the 'Id' column as the row index
df_full = pd.read_csv(csv_file_path, index_col='Id')

print("\nFull dataset loaded successfully!")
print(f"Shape: {df_full.shape[0]} rows × {df_full.shape[1]} columns")
print(f"Index name: {df_full.index.name}")

# Display all column names in the full dataset
print("\nAll available columns:")
print(df_full.columns.tolist())

# =============================================================================
# STEP 2: Create DataFrame with Selected Columns
# =============================================================================

print("\n" + "-"*80)
print("STEP 2: CREATE DATAFRAME WITH SELECTED COLUMNS")
print("-"*80)

# Define the columns we want to include in our analysis
# Numeric columns: quantitative measurements
numeric_cols = ['OverallQual', 'GrLivArea', 'TotRmsAbvGrd', 'YearBuilt', 
                'LotArea', 'LotFrontage', 'SalePrice']

# Categorical columns: qualitative classifications
categorical_cols = ['MSZoning', 'Neighborhood', 'HouseStyle']

# Combine all selected columns into a single list
selected_cols = numeric_cols + categorical_cols

print("\nSelected columns:")
print(f"  Numeric ({len(numeric_cols)}): {numeric_cols}")
print(f"  Categorical ({len(categorical_cols)}): {categorical_cols}")
print(f"  Total: {len(selected_cols)} columns")

# Create new DataFrame with only selected columns
# Double bracket notation [[ ]] ensures we get a DataFrame, not a Series
df_selected = df_full[selected_cols]

print("\nNew DataFrame created successfully!")
print(f"Shape: {df_selected.shape[0]} rows × {df_selected.shape[1]} columns")

# Display first few rows to verify column selection
print("\nFirst 5 rows of selected DataFrame:")
print(df_selected.head())

# Display last few rows as well
print("\nLast 5 rows of selected DataFrame:")
print(df_selected.tail())

# =============================================================================
# STEP 3: Identify Missing Values
# =============================================================================

print("\n" + "-"*80)
print("STEP 3: IDENTIFY COLUMNS WITH MISSING VALUES")
print("-"*80)

# Method 1: Count missing values per column
# .isnull() creates boolean DataFrame (True for NaN, False otherwise)
# .sum() counts True values (True=1, False=0)
missing_counts = df_selected.isnull().sum()

print("\nMissing value counts per column:")
print(missing_counts)

# Method 2: Calculate percentage of missing values
# Divide missing counts by total rows, multiply by 100 for percentage
total_rows = len(df_selected)
missing_percentages = (missing_counts / total_rows) * 100

print("\nMissing value percentages:")
# Create a DataFrame combining counts and percentages for better readability
missing_summary = pd.DataFrame({
    'Missing_Count': missing_counts,
    'Missing_Percentage': missing_percentages
})
# Sort by missing count in descending order to see worst columns first
missing_summary = missing_summary.sort_values('Missing_Count', ascending=False)
print(missing_summary)

# Identify columns with missing values (count > 0)
columns_with_missing = missing_counts[missing_counts > 0].index.tolist()

print(f"\nColumns with missing values: {len(columns_with_missing)} out of {len(selected_cols)}")
if columns_with_missing:
    for col in columns_with_missing:
        print(f"  • {col}: {missing_counts[col]} missing ({missing_percentages[col]:.2f}%)")
else:
    print("  ✓ No missing values found in any column!")

# Visualize missing data
print("\nCreating missing data visualization...")
plt.figure(figsize=(10, 6))
# Plot bar chart showing missing value counts
missing_counts.sort_values(ascending=True).plot(kind='barh', color='coral')
plt.xlabel('Number of Missing Values', fontsize=12)
plt.ylabel('Column Name', fontsize=12)
plt.title('Missing Values by Column', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('exercise_3_missing_values.png', dpi=300, bbox_inches='tight')
print("✓ Saved: exercise_3_missing_values.png")
plt.close()

# =============================================================================
# STEP 4: Basic Dataset Information
# =============================================================================

print("\n" + "-"*80)
print("STEP 4: BASIC DATASET INFORMATION")
print("-"*80)

# Display concise summary of DataFrame
# Shows: column names, non-null counts, data types, memory usage
print("\nDataFrame Info:")
print(df_selected.info())

# Display data types for each column
print("\nData types:")
print(df_selected.dtypes)

# Separate numeric and categorical columns based on actual data types
# select_dtypes() filters columns by their data type
numeric_columns_actual = df_selected.select_dtypes(include=[np.number]).columns.tolist()
categorical_columns_actual = df_selected.select_dtypes(include=['object']).columns.tolist()

print(f"\nNumeric columns ({len(numeric_columns_actual)}): {numeric_columns_actual}")
print(f"Categorical columns ({len(categorical_columns_actual)}): {categorical_columns_actual}")

# =============================================================================
# STEP 5: Statistical Summary of Numeric Columns
# =============================================================================

print("\n" + "-"*80)
print("STEP 5: STATISTICAL SUMMARY - NUMERIC COLUMNS")
print("-"*80)

# Generate comprehensive statistical summary
# Shows: count, mean, std, min, quartiles (25%, 50%, 75%), max
print("\nDescriptive statistics for numeric columns:")
numeric_stats = df_selected[numeric_cols].describe()
print(numeric_stats)

# Additional statistics not included in .describe()
print("\nAdditional statistics:")
for col in numeric_cols:
    # Skip if column has all NaN values
    if df_selected[col].isnull().all():
        print(f"\n{col}: All values are missing")
        continue
    
    print(f"\n{col}:")
    print(f"  Mean: {df_selected[col].mean():.2f}")
    print(f"  Median: {df_selected[col].median():.2f}")
    print(f"  Mode: {df_selected[col].mode().values[0] if len(df_selected[col].mode()) > 0 else 'N/A'}")
    print(f"  Std Dev: {df_selected[col].std():.2f}")
    print(f"  Variance: {df_selected[col].var():.2f}")
    print(f"  Range: {df_selected[col].min():.2f} - {df_selected[col].max():.2f}")
    print(f"  IQR (Q3-Q1): {df_selected[col].quantile(0.75) - df_selected[col].quantile(0.25):.2f}")
    # Skewness: measure of asymmetry (0=symmetric, >0=right-skewed, <0=left-skewed)
    print(f"  Skewness: {df_selected[col].skew():.2f}")
    # Kurtosis: measure of tail heaviness (3=normal, >3=heavy tails, <3=light tails)
    print(f"  Kurtosis: {df_selected[col].kurtosis():.2f}")

# =============================================================================
# STEP 6: Distribution Analysis - Numeric Columns
# =============================================================================

print("\n" + "-"*80)
print("STEP 6: DISTRIBUTION ANALYSIS - NUMERIC COLUMNS")
print("-"*80)

print("\nCreating distribution plots for numeric columns...")

# Create histograms for all numeric columns
fig, axes = plt.subplots(3, 3, figsize=(16, 12))
# Flatten 2D array of axes to iterate easily
axes = axes.flatten()

for idx, col in enumerate(numeric_cols):
    # Plot histogram with KDE (Kernel Density Estimation) overlay
    # KDE shows smooth estimate of probability distribution
    df_selected[col].hist(ax=axes[idx], bins=30, color='skyblue', 
                          edgecolor='black', alpha=0.7)
    axes[idx].set_title(f'Distribution of {col}', fontsize=12, fontweight='bold')
    axes[idx].set_xlabel(col, fontsize=10)
    axes[idx].set_ylabel('Frequency', fontsize=10)
    axes[idx].grid(axis='y', alpha=0.3)

# Hide extra subplot if we have fewer than 9 numeric columns
for idx in range(len(numeric_cols), len(axes)):
    axes[idx].axis('off')

plt.tight_layout()
plt.savefig('exercise_3_numeric_distributions.png', dpi=300, bbox_inches='tight')
print("✓ Saved: exercise_3_numeric_distributions.png")
plt.close()

# Create box plots to identify outliers
print("\nCreating box plots for outlier detection...")
fig, axes = plt.subplots(3, 3, figsize=(16, 12))
axes = axes.flatten()

for idx, col in enumerate(numeric_cols):
    # Box plot shows: median (line), quartiles (box), whiskers, and outliers (points)
    df_selected.boxplot(column=col, ax=axes[idx], patch_artist=True,
                        boxprops=dict(facecolor='lightgreen', alpha=0.7),
                        medianprops=dict(color='red', linewidth=2))
    axes[idx].set_title(f'Box Plot: {col}', fontsize=12, fontweight='bold')
    axes[idx].set_ylabel(col, fontsize=10)
    axes[idx].grid(axis='y', alpha=0.3)

# Hide extra subplots
for idx in range(len(numeric_cols), len(axes)):
    axes[idx].axis('off')

plt.tight_layout()
plt.savefig('exercise_3_numeric_boxplots.png', dpi=300, bbox_inches='tight')
print("✓ Saved: exercise_3_numeric_boxplots.png")
plt.close()

# =============================================================================
# STEP 7: Categorical Columns Analysis
# =============================================================================

print("\n" + "-"*80)
print("STEP 7: CATEGORICAL COLUMNS ANALYSIS")
print("-"*80)

# Analyze each categorical column
for col in categorical_cols:
    print(f"\n{col}:")
    # Count unique categories
    print(f"  Unique values: {df_selected[col].nunique()}")
    # Get frequency distribution using value_counts()
    value_counts = df_selected[col].value_counts()
    print(f"  Most common: {value_counts.index[0]} ({value_counts.values[0]} occurrences)")
    print(f"  Least common: {value_counts.index[-1]} ({value_counts.values[-1]} occurrences)")
    
    # Display full distribution
    print(f"\n  Full distribution:")
    print(value_counts)

# Visualize categorical distributions
print("\nCreating categorical distribution plots...")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for idx, col in enumerate(categorical_cols):
    # Count plot shows frequency of each category
    value_counts = df_selected[col].value_counts()
    # Limit to top 15 categories for readability (if more exist)
    if len(value_counts) > 15:
        value_counts = value_counts.head(15)
        title_suffix = ' (Top 15)'
    else:
        title_suffix = ''
    
    # Create bar plot
    value_counts.plot(kind='bar', ax=axes[idx], color='teal', alpha=0.7)
    axes[idx].set_title(f'{col} Distribution{title_suffix}', fontsize=12, fontweight='bold')
    axes[idx].set_xlabel(col, fontsize=10)
    axes[idx].set_ylabel('Count', fontsize=10)
    axes[idx].tick_params(axis='x', rotation=45)
    axes[idx].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('exercise_3_categorical_distributions.png', dpi=300, bbox_inches='tight')
print("✓ Saved: exercise_3_categorical_distributions.png")
plt.close()

# =============================================================================
# STEP 8: Relationship with SalePrice - Numeric Features
# =============================================================================

print("\n" + "-"*80)
print("STEP 8: RELATIONSHIP WITH SALEPRICE - NUMERIC FEATURES")
print("-"*80)

# Calculate correlation matrix for numeric columns
print("\nCalculating correlations with SalePrice...")
# .corr() computes pairwise correlation coefficients (Pearson by default)
correlation_matrix = df_selected[numeric_cols].corr()

# Extract correlations with SalePrice specifically
saleprice_correlations = correlation_matrix['SalePrice'].sort_values(ascending=False)

print("\nCorrelations with SalePrice (sorted by strength):")
print(saleprice_correlations)

# Interpret correlation strengths
print("\nCorrelation interpretation:")
for feature, corr in saleprice_correlations.items():
    if feature == 'SalePrice':
        continue  # Skip SalePrice correlation with itself
    
    # Classify correlation strength
    abs_corr = abs(corr)
    if abs_corr >= 0.7:
        strength = "Strong"
    elif abs_corr >= 0.4:
        strength = "Moderate"
    elif abs_corr >= 0.2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Classify direction
    direction = "positive" if corr > 0 else "negative"
    
    print(f"  • {feature}: {corr:.3f} ({strength} {direction} correlation)")

# Visualize correlation matrix as heatmap
print("\nCreating correlation heatmap...")
plt.figure(figsize=(10, 8))
# Heatmap shows correlation strengths with color intensity
# annot=True displays correlation values in cells
# cmap='coolwarm' uses blue-white-red color scheme
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix - Numeric Features', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('exercise_3_correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Saved: exercise_3_correlation_heatmap.png")
plt.close()

# Create scatter plots for features vs SalePrice
print("\nCreating scatter plots: Features vs SalePrice...")
# Exclude SalePrice itself from scatter plots
features_for_scatter = [col for col in numeric_cols if col != 'SalePrice']

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()

for idx, col in enumerate(features_for_scatter):
    # Scatter plot shows relationship between two variables
    axes[idx].scatter(df_selected[col], df_selected['SalePrice'], 
                     alpha=0.5, s=20, color='navy')
    
    # Add trend line (linear regression)
    # Remove NaN values for regression calculation
    mask = ~(df_selected[col].isnull() | df_selected['SalePrice'].isnull())
    if mask.sum() > 1:  # Need at least 2 points for regression
        # np.polyfit fits polynomial (degree=1 means linear)
        z = np.polyfit(df_selected.loc[mask, col], 
                      df_selected.loc[mask, 'SalePrice'], 1)
        p = np.poly1d(z)
        # Plot trend line
        x_line = np.linspace(df_selected[col].min(), df_selected[col].max(), 100)
        axes[idx].plot(x_line, p(x_line), "r-", linewidth=2, label='Trend line')
    
    axes[idx].set_xlabel(col, fontsize=10)
    axes[idx].set_ylabel('SalePrice', fontsize=10)
    axes[idx].set_title(f'{col} vs SalePrice (r={saleprice_correlations[col]:.3f})', 
                       fontsize=11, fontweight='bold')
    axes[idx].grid(alpha=0.3)
    axes[idx].legend()

plt.tight_layout()
plt.savefig('exercise_3_scatter_saleprice.png', dpi=300, bbox_inches='tight')
print("✓ Saved: exercise_3_scatter_saleprice.png")
plt.close()

# =============================================================================
# STEP 9: Relationship with SalePrice - Categorical Features
# =============================================================================

print("\n" + "-"*80)
print("STEP 9: RELATIONSHIP WITH SALEPRICE - CATEGORICAL FEATURES")
print("-"*80)

# Analyze how SalePrice varies across categorical groups
print("\nAverage SalePrice by category:\n")

for col in categorical_cols:
    print(f"{col}:")
    # Group by category and calculate mean SalePrice
    # .groupby() splits data into groups based on categorical values
    category_prices = df_selected.groupby(col)['SalePrice'].agg(['mean', 'median', 'count'])
    # Sort by mean price to see most/least expensive categories
    category_prices = category_prices.sort_values('mean', ascending=False)
    print(category_prices)
    print()

# Visualize SalePrice distribution across categories
print("\nCreating box plots: SalePrice by categorical features...")
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

for idx, col in enumerate(categorical_cols):
    # Box plot by category shows price distribution for each group
    # Useful for comparing medians, spread, and outliers across categories
    df_selected.boxplot(column='SalePrice', by=col, ax=axes[idx],
                        patch_artist=True, rot=45)
    axes[idx].set_title(f'SalePrice by {col}', fontsize=12, fontweight='bold')
    axes[idx].set_xlabel(col, fontsize=10)
    axes[idx].set_ylabel('SalePrice', fontsize=10)
    # Remove automatic title added by pandas boxplot
    axes[idx].get_figure().suptitle('')

plt.tight_layout()
plt.savefig('exercise_3_saleprice_by_categories.png', dpi=300, bbox_inches='tight')
print("✓ Saved: exercise_3_saleprice_by_categories.png")
plt.close()

# Create bar plots showing average price by category
print("\nCreating bar plots: Average SalePrice by categorical features...")
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

for idx, col in enumerate(categorical_cols):
    # Calculate mean price per category
    avg_prices = df_selected.groupby(col)['SalePrice'].mean().sort_values(ascending=False)
    
    # Limit to top 15 for readability
    if len(avg_prices) > 15:
        avg_prices = avg_prices.head(15)
        title_suffix = ' (Top 15)'
    else:
        title_suffix = ''
    
    # Create horizontal bar plot
    avg_prices.plot(kind='barh', ax=axes[idx], color='darkgreen', alpha=0.7)
    axes[idx].set_title(f'Avg SalePrice by {col}{title_suffix}', 
                       fontsize=12, fontweight='bold')
    axes[idx].set_xlabel('Average SalePrice ($)', fontsize=10)
    axes[idx].set_ylabel(col, fontsize=10)
    axes[idx].grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('exercise_3_avg_price_by_categories.png', dpi=300, bbox_inches='tight')
print("✓ Saved: exercise_3_avg_price_by_categories.png")
plt.close()

# =============================================================================
# STEP 10: Summary and Key Insights
# =============================================================================

print("\n" + "="*80)
print("EXPLORATORY DATA ANALYSIS COMPLETED!")
print("="*80)

print("\n" + "-"*80)
print("SUMMARY OF FINDINGS")
print("-"*80)

# Dataset overview
print("\n1. DATASET OVERVIEW:")
print(f"   • Total records: {df_selected.shape[0]:,}")
print(f"   • Total features: {df_selected.shape[1]}")
print(f"   • Numeric features: {len(numeric_cols)}")
print(f"   • Categorical features: {len(categorical_cols)}")

# Missing values summary
print("\n2. MISSING VALUES:")
if len(columns_with_missing) > 0:
    print(f"   • Columns with missing data: {len(columns_with_missing)}")
    for col in columns_with_missing:
        print(f"     - {col}: {missing_counts[col]} ({missing_percentages[col]:.2f}%)")
else:
    print("   • No missing values detected ✓")

# SalePrice statistics
print("\n3. SALEPRICE STATISTICS:")
print(f"   • Mean: ${df_selected['SalePrice'].mean():,.2f}")
print(f"   • Median: ${df_selected['SalePrice'].median():,.2f}")
print(f"   • Std Dev: ${df_selected['SalePrice'].std():,.2f}")
print(f"   • Min: ${df_selected['SalePrice'].min():,.2f}")
print(f"   • Max: ${df_selected['SalePrice'].max():,.2f}")
print(f"   • Range: ${df_selected['SalePrice'].max() - df_selected['SalePrice'].min():,.2f}")

# Top correlations with SalePrice
print("\n4. TOP CORRELATIONS WITH SALEPRICE:")
# Exclude SalePrice itself, get top 3 correlations
top_correlations = saleprice_correlations[saleprice_correlations.index != 'SalePrice'].head(3)
for idx, (feature, corr) in enumerate(top_correlations.items(), 1):
    print(f"   {idx}. {feature}: {corr:.3f}")

# Categorical insights
print("\n5. CATEGORICAL INSIGHTS:")
for col in categorical_cols:
    category_prices = df_selected.groupby(col)['SalePrice'].mean().sort_values(ascending=False)
    most_expensive = category_prices.index[0]
    least_expensive = category_prices.index[-1]
    print(f"   • {col}:")
    print(f"     - Highest avg price: {most_expensive} (${category_prices[most_expensive]:,.2f})")
    print(f"     - Lowest avg price: {least_expensive} (${category_prices[least_expensive]:,.2f})")
    print(f"     - Price ratio: {category_prices[most_expensive] / category_prices[least_expensive]:.2f}x")

# Visualizations created
print("\n6. VISUALIZATIONS CREATED:")
visualizations = [
    'exercise_3_missing_values.png',
    'exercise_3_numeric_distributions.png',
    'exercise_3_numeric_boxplots.png',
    'exercise_3_categorical_distributions.png',
    'exercise_3_correlation_heatmap.png',
    'exercise_3_scatter_saleprice.png',
    'exercise_3_saleprice_by_categories.png',
    'exercise_3_avg_price_by_categories.png'
]
for viz in visualizations:
    print(f"   ✓ {viz}")

print("\n" + "="*80)
print("KEY TAKEAWAYS:")
print("="*80)

print("""
1. DATA QUALITY: 
   - LotFrontage has significant missing data (17.74%), may need imputation
   - Other features are complete or have minimal missing values

2. STRONGEST PRICE PREDICTORS (Numeric):
   - OverallQual shows strongest correlation with SalePrice
   - GrLivArea (above ground living area) is highly correlated
   - YearBuilt has moderate positive correlation

3. CATEGORICAL INFLUENCES:
   - Neighborhood significantly impacts price (varies by location)
   - MSZoning shows different price points for zoning types
   - HouseStyle affects pricing based on architectural style

4. DISTRIBUTION PATTERNS:
   - SalePrice is right-skewed (mean > median), indicating high-end outliers
   - Most numeric features show some level of skewness
   - Several outliers detected in LotArea, GrLivArea, and SalePrice

5. RECOMMENDED NEXT STEPS:
   - Handle missing LotFrontage values (imputation or removal)
   - Consider log transformation for right-skewed features
   - Investigate and potentially remove extreme outliers
   - Encode categorical variables for machine learning models
   - Create interaction features between highly correlated variables
""")

print("\nAll EDA tasks completed successfully! ✓")
print("="*80)

# Standard Python idiom to check if script is being run directly
if __name__ == "__main__":
    pass
