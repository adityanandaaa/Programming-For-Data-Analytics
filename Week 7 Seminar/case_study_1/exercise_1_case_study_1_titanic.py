import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Setup Paths ---
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "..", "data source")
output_dir = os.path.join(script_dir, "visualizations")

# Ensure directories exist
os.makedirs(data_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

print("--- Case Study 1: House Price Data Processing & Feature Engineering ---\n")

# Load Dataset
file_path = os.path.join(data_dir, "house_price.csv")
df_house = pd.read_csv(file_path)

print(f"Initial shape: {df_house.shape}")
print(f"Initial columns: {list(df_house.columns)}\n")

# ============================================================================
# STEP 1: REMOVE ROWS WITH MORE THAN 1 MISSING VALUE
# Purpose: Eliminate incomplete records that would skew analysis
# ============================================================================
print("--- Step 1: Remove rows with more than 1 missing value ---")
initial_rows = len(df_house)
# .isnull().sum(axis=1) counts missing values per row; <= 1 keeps rows with 0 or 1 missing value
df_house = df_house[df_house.isnull().sum(axis=1) <= 1]
print(f"Rows removed: {initial_rows - len(df_house)}")
print(f"Remaining rows: {len(df_house)}\n")

# ============================================================================
# STEP 2: REMOVE COLUMNS WITH MORE THAN 33% MISSING VALUES
# Purpose: Drop features with insufficient data coverage for reliable modeling
# ============================================================================
print("--- Step 2: Remove columns with >33% missing values ---")
# Calculate percentage of missing values per column
missing_pct = (df_house.isnull().sum() / len(df_house)) * 100
# Filter columns where missing percentage exceeds 33% threshold
cols_to_drop = missing_pct[missing_pct > 33].index.tolist()
print(f"Columns to drop: {cols_to_drop}")
# Drop the identified columns from the dataframe
df_house = df_house.drop(columns=cols_to_drop)
print(f"Remaining columns: {len(df_house.columns)}\n")

# ============================================================================
# STEP 3: IMPUTE MISSING VALUES
# Strategy: 
#   - Numerical columns: Use median (robust to outliers)
#   - Categorical columns: Use mode (most frequent value)
# ============================================================================
print("--- Step 3: Impute missing values ---")
for col in df_house.columns:
    if df_house[col].isnull().sum() > 0:  # Check if column has any missing values
        if df_house[col].dtype in ['int64', 'float64']:
            # fillna() replaces NaN with the specified value; median is robust to outliers
            df_house[col].fillna(df_house[col].median(), inplace=True)
            print(f"Imputed {col} with median")
        else:
            # mode()[0] gets the most frequent category; ideal for categorical data
            df_house[col].fillna(df_house[col].mode()[0], inplace=True)
            print(f"Imputed {col} with mode")

# Verify no missing values remain after imputation
print(f"Missing values after imputation: {df_house.isnull().sum().sum()}\n")

# ============================================================================
# STEP 4: REMOVE OUTLIERS IN SALEPRICE
# Method: Interquartile Range (IQR)
# Logic: Remove values beyond 1.5 * IQR from Q1 and Q3
# ============================================================================
print("--- Step 4: Remove outliers in SalePrice ---")
if 'SalePrice' in df_house.columns:
    # quantile(0.25) and quantile(0.75) get the 25th and 75th percentile (Q1, Q3)
    Q1 = df_house['SalePrice'].quantile(0.25)
    Q3 = df_house['SalePrice'].quantile(0.75)
    # IQR (Interquartile Range) = Q3 - Q1; measures spread of middle 50% of data
    IQR = Q3 - Q1
    # Standard IQR method: remove values outside 1.5 * IQR from Q1/Q3
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    initial_len = len(df_house)
    # Boolean indexing keeps only rows where SalePrice falls within bounds
    df_house = df_house[(df_house['SalePrice'] >= lower_bound) & (df_house['SalePrice'] <= upper_bound)]
    print(f"Outliers removed: {initial_len - len(df_house)}")
    print(f"SalePrice range: ${lower_bound:,.0f} - ${upper_bound:,.0f}\n")

# ============================================================================
# STEP 5: LOG TRANSFORMATION FOR SKEWED COLUMNS
# Purpose: Normalize distributions of highly skewed features for better modeling
# Criteria: Apply log transformation if |skewness| > 1 (highly skewed)
# ============================================================================
print("--- Step 5: Log transformation for skewed columns ---")
# select_dtypes() filters only numerical columns (int64, float64)
numerical_cols = df_house.select_dtypes(include=['int64', 'float64']).columns
skewed_cols = []

for col in numerical_cols:
    # .skew() calculates skewness; |skewness| > 1 indicates highly skewed distribution
    skewness = df_house[col].skew()
    if abs(skewness) > 1:  # Highly skewed
        skewed_cols.append((col, skewness))

print(f"Highly skewed columns (|skewness| > 1):")
for col, skew in skewed_cols:
    print(f"  {col}: {skew:.2f}")

# Create visualizations before and after transformation
if skewed_cols:
    fig, axes = plt.subplots(len(skewed_cols), 2, figsize=(12, 4 * len(skewed_cols)))
    if len(skewed_cols) == 1:
        axes = axes.reshape(1, -1)
    
    for idx, (col, _) in enumerate(skewed_cols):
        # Left: Original distribution (before transformation)
        axes[idx, 0].hist(df_house[col], bins=30, edgecolor='black')
        axes[idx, 0].set_title(f'{col} - Original Distribution')
        axes[idx, 0].set_xlabel(col)
        
        # Right: Log-transformed distribution (after transformation)
        # np.log1p(x) = log(1 + x) handles zeros gracefully (avoids log(0) = -inf)
        log_col = np.log1p(df_house[col])
        axes[idx, 1].hist(log_col, bins=30, edgecolor='black')
        axes[idx, 1].set_title(f'{col} - Log Transformed Distribution')
        axes[idx, 1].set_xlabel(f'log({col})')
        
        # Replace original column with log-transformed version to normalize distribution
        df_house[col] = log_col
    
    plt.tight_layout()
    # Save visualization showing before/after transformation
    plot_path = os.path.join(output_dir, "log_transformations.png")
    plt.savefig(plot_path, dpi=100, bbox_inches='tight')
    print(f"Visualization saved to: {plot_path}\n")
    plt.close()

# ============================================================================
# STEP 6: CREATE DUMMY COLUMNS FOR CATEGORICAL VARIABLES
# Criteria: Convert categorical variables with ≤5 unique values to dummy columns
# Benefit: Enables machine learning models to process categorical features
# ============================================================================
print("--- Step 6: Create dummy columns for categorical variables ---")
# select_dtypes(include=['object']) filters only categorical/text columns
categorical_cols = df_house.select_dtypes(include=['object']).columns
for col in categorical_cols:
    # .nunique() counts distinct values in the column
    unique_count = df_house[col].nunique()
    if unique_count <= 5:
        print(f"Creating dummies for {col} ({unique_count} unique values)")
        # pd.get_dummies() creates binary columns for each category; drop_first=True removes first column
        dummies = pd.get_dummies(df_house[col], prefix=col, drop_first=True)
        # pd.concat() joins new dummy columns alongside existing dataframe
        df_house = pd.concat([df_house, dummies], axis=1)
        # Drop original categorical column after creating dummies
        df_house.drop(columns=[col], inplace=True)
    else:
        print(f"Skipping {col} ({unique_count} unique values > 5, too many categories)")

print(f"New shape after dummy encoding: {df_house.shape}\n")

# ============================================================================
# STEP 7: CREATE TIME PERIOD GROUPS BASED ON YEARBUILT
# Rationale: Regulatory changes in 1950 and 1989 affected building standards
# Groups: Pre-1950 (older), 1950-1989 (mid-period), Post-1989 (modern)
# ============================================================================
print("--- Step 7: Create time period groups based on YearBuilt ---")
if 'YearBuilt' in df_house.columns:
    # Define time periods based on regulatory milestones
    def categorize_year(year):
        # Nested if-elif-else creates 3 categories based on year thresholds
        if year < 1950:
            return 'Pre-1950'  # Before first major building code
        elif 1950 <= year <= 1989:
            return '1950-1989'  # Period between two regulatory acts
        else:
            return 'Post-1989'  # After second major building code

    # .apply() applies the function row-wise to convert years into period categories
    df_house['YearBuilt_Period'] = df_house['YearBuilt'].apply(categorize_year)
    print(f"Time period distribution:")
    # .value_counts() shows frequency of each category
    print(df_house['YearBuilt_Period'].value_counts())
    
    # Convert time period categories to dummy columns (one-hot encoding)
    # prefix= adds column name prefix; drop_first=True avoids multicollinearity
    period_dummies = pd.get_dummies(df_house['YearBuilt_Period'], prefix='YearBuilt_Period', drop_first=True)
    # Concatenate dummy columns to the main dataframe
    df_house = pd.concat([df_house, period_dummies], axis=1)
    
    # Remove original columns now that they're encoded as dummies
    df_house.drop(columns=['YearBuilt_Period', 'YearBuilt'], inplace=True)
    print("Dummy columns created for time periods (drop_first=True for multicollinearity avoidance)\n")

# ============================================================================
# FINAL SUMMARY & VERIFICATION
# ============================================================================
print("--- Final Data Summary ---")
print(f"Final shape: {df_house.shape}")
print(f"Data types:\n{df_house.dtypes}")
print(f"\nMissing values: {df_house.isnull().sum().sum()}")
print(f"\nFirst 5 rows:")
print(df_house.head())
