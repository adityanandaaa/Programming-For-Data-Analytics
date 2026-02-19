"""
Week 6 Seminar: Case Study 1 - House Pricing Exercise 2
========================================================

Dataset: House sales data from Ames, Iowa
Source: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data

Tasks:
4. Find sale prices for houses with id 222 and 333
5. Find the first 100 records in "df_location"
6. Find all rows from df_house with OverallQual at least 8 and save as "df_great"
7. (Optional) Find rows with OverallQual >= 8 AND SalePrice < 300,000 and save as "df_deal"

Author: Week 6 Seminar Series
Date: February 2026
"""

# Import pandas library for data manipulation and analysis
import pandas as pd
# Import os module for file path operations
import os

# Get the absolute path of the current script file
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the 'data source' folder within the script directory
data_dir = os.path.join(script_dir, 'data source')

print("="*70)
print("CASE STUDY 1: HOUSE PRICING EXERCISE 2")
print("="*70)

# =============================================================================
# LOAD DATA (from Exercise 1)
# =============================================================================

print("\n" + "-"*70)
print("LOADING DATA")
print("-"*70)

# Construct the full file path to house_price.csv
csv_file_path = os.path.join(data_dir, 'house_price.csv')
print(f"\nFile path: {csv_file_path}")

# Read CSV file into a DataFrame
# index_col='Id' sets the 'Id' column as the row index instead of default numeric index
df_house = pd.read_csv(csv_file_path, index_col='Id')

print("\nDataFrame df_house loaded successfully!")
# Display the number of rows and columns in the DataFrame
print(f"Shape: {df_house.shape}")
# Display the name of the index column
print(f"Index name: {df_house.index.name}")

# Create df_location from 'Neighborhood' and 'Condition1' columns
# Double bracket notation [[]] creates a DataFrame (not a Series)
df_location = df_house[['Neighborhood', 'Condition1']]

print("\nDataFrame df_location created successfully!")
print(f"Shape: {df_location.shape}")

# =============================================================================
# TASK 4: Find sale prices for houses with id 222 and 333
# =============================================================================

print("\n" + "-"*70)
print("TASK 4: Find sale prices for houses with id 222 and 333")
print("-"*70)

# Method 1: Using .loc[] with a list of index labels
# .loc[] is label-based indexing - uses the actual index values
# Pass a list [222, 333] to select multiple rows by their Id
prices_222_333 = df_house.loc[[222, 333], 'SalePrice']

print("\nMethod 1: Using .loc[] with list of IDs")
print("Sale prices for houses with Id 222 and 333:")
print(prices_222_333)

# Method 2: Using .loc[] with slice notation
# This also works but includes all houses between 222 and 333
# Note: With .loc[], both start and end are INCLUDED
print("\nMethod 2: Using .loc[] with slice (for demonstration)")
print("Note: This returns houses 222 through 333 (inclusive):")
prices_slice = df_house.loc[222:333, 'SalePrice']
print(f"Number of houses in slice: {len(prices_slice)}")
print(f"First few: {prices_slice.head()}")

# Method 3: Individual access (less efficient for multiple records)
print("\nMethod 3: Individual access")
# Access each house separately using .loc[] with single index
# .loc[index, column] returns a single scalar value
price_222 = df_house.loc[222, 'SalePrice']
price_333 = df_house.loc[333, 'SalePrice']
print(f"House Id 222: ${price_222:,}")
print(f"House Id 333: ${price_333:,}")

# Display full information for these two houses
print("\nFull information for houses 222 and 333:")
# .loc[] with list of IDs returns all columns for those houses
print(df_house.loc[[222, 333]])

# Extract as Series for further analysis
print("\nStatistics for these two houses:")
print(f"Mean price: ${prices_222_333.mean():,.2f}")
print(f"Min price: ${prices_222_333.min():,}")
print(f"Max price: ${prices_222_333.max():,}")
print(f"Price difference: ${abs(prices_222_333.iloc[0] - prices_222_333.iloc[1]):,}")

# =============================================================================
# TASK 5: Find the first 100 records in "df_location"
# =============================================================================

print("\n" + "-"*70)
print("TASK 5: Find the first 100 records in df_location")
print("-"*70)

# Method 1: Using .head() method (most common and readable)
# .head(n) returns the first n rows of a DataFrame
# Default is 5 if no argument provided
df_location_first_100 = df_location.head(100)

print("\nMethod 1: Using .head(100)")
print(f"Shape of first 100 records: {df_location_first_100.shape}")
print("\nFirst 10 of these 100 records:")
print(df_location_first_100.head(10))

# Method 2: Using .iloc[] with slice notation (position-based)
# .iloc[] uses integer positions (0-based indexing)
# Slice [0:100] means positions 0 through 99 (100 total records)
# Note: With .iloc[], the end position is EXCLUDED
df_location_first_100_iloc = df_location.iloc[0:100]

print("\nMethod 2: Using .iloc[0:100]")
print(f"Shape: {df_location_first_100_iloc.shape}")

# Method 3: Using slice notation directly (shorthand for .iloc[])
# This is syntactic sugar for .iloc[]
df_location_first_100_slice = df_location[0:100]

print("\nMethod 3: Using direct slice [0:100]")
print(f"Shape: {df_location_first_100_slice.shape}")

# Verify all methods produce the same result
# .equals() checks if two DataFrames have the same values and structure
print("\nVerification: All methods produce identical results?")
method1_equals_method2 = df_location_first_100.equals(df_location_first_100_iloc)
method2_equals_method3 = df_location_first_100_iloc.equals(df_location_first_100_slice)
print(f"Method 1 equals Method 2: {method1_equals_method2}")
print(f"Method 2 equals Method 3: {method2_equals_method3}")

# Display summary statistics for first 100 records
print("\nNeighborhood distribution in first 100 records:")
# .value_counts() returns a Series with counts of unique values
# Shows which neighborhoods appear most frequently in first 100 records
print(df_location_first_100['Neighborhood'].value_counts())

print("\nCondition1 distribution in first 100 records:")
print(df_location_first_100['Condition1'].value_counts())

# =============================================================================
# TASK 6: Find all rows with OverallQual >= 8 and save as "df_great"
# =============================================================================

print("\n" + "-"*70)
print("TASK 6: Find all rows with OverallQual >= 8 and save as df_great")
print("-"*70)

# Create a boolean mask: True where OverallQual >= 8, False otherwise
# This is a Series of boolean values with same index as df_house
mask_quality = df_house['OverallQual'] >= 8

# Display how many houses meet the criteria
# .sum() on boolean Series counts True values (True=1, False=0)
num_great_houses = mask_quality.sum()
print(f"\nNumber of houses with OverallQual >= 8: {num_great_houses}")
print(f"Percentage of total: {(num_great_houses / len(df_house) * 100):.2f}%")

# Apply the boolean mask to filter the DataFrame
# df_house.loc[mask] returns only rows where mask is True
df_great = df_house.loc[mask_quality]

print("\nDataFrame df_great created successfully!")
print(f"Shape: {df_great.shape}")
print(f"Index range: {df_great.index.min()} to {df_great.index.max()}")

# Alternative method: Direct boolean indexing (without .loc[])
# This works but .loc[] is more explicit and safer
df_great_alternative = df_house[df_house['OverallQual'] >= 8]
print(f"\nAlternative method produces same result: {df_great.equals(df_great_alternative)}")

# Display first few records
print("\nFirst 10 houses in df_great:")
print(df_great.head(10))

# Analyze the quality distribution
print("\nOverallQual distribution in df_great:")
# Since all are >= 8, show counts of 8, 9, and 10
print(df_great['OverallQual'].value_counts().sort_index())

# Statistics for great houses
print("\nStatistics for df_great:")
print(f"Average SalePrice: ${df_great['SalePrice'].mean():,.2f}")
print(f"Median SalePrice: ${df_great['SalePrice'].median():,.2f}")
print(f"Min SalePrice: ${df_great['SalePrice'].min():,}")
print(f"Max SalePrice: ${df_great['SalePrice'].max():,}")

# Compare with overall dataset
print("\nComparison with overall dataset:")
print(f"Overall average price: ${df_house['SalePrice'].mean():,.2f}")
print(f"df_great average price: ${df_great['SalePrice'].mean():,.2f}")
price_premium = df_great['SalePrice'].mean() - df_house['SalePrice'].mean()
print(f"Premium for high quality: ${price_premium:,.2f} ({(price_premium / df_house['SalePrice'].mean() * 100):.1f}%)")

# =============================================================================
# TASK 7 (Optional): Find rows with OverallQual >= 8 AND SalePrice < 300,000
# =============================================================================

print("\n" + "-"*70)
print("TASK 7 (Optional): Find rows with OverallQual >= 8 AND SalePrice < 300,000")
print("-"*70)

# Create two separate boolean masks
# mask1: Houses with OverallQual >= 8
mask_quality_8 = df_house['OverallQual'] >= 8
# mask2: Houses with SalePrice < 300,000
mask_price_low = df_house['SalePrice'] < 300000

# Combine masks using & (AND) operator
# Both conditions must be True for the result to be True
# IMPORTANT: Use & for element-wise AND (not 'and' which is for boolean values)
# Parentheses are required around each condition due to operator precedence
mask_deal = (df_house['OverallQual'] >= 8) & (df_house['SalePrice'] < 300000)

# Count how many houses meet both criteria
num_deals = mask_deal.sum()
print(f"\nNumber of houses with OverallQual >= 8 AND SalePrice < $300,000: {num_deals}")
print(f"Percentage of total dataset: {(num_deals / len(df_house) * 100):.2f}%")
print(f"Percentage of df_great: {(num_deals / len(df_great) * 100):.2f}%")

# Apply the combined mask to create df_deal
df_deal = df_house.loc[mask_deal]

print("\nDataFrame df_deal created successfully!")
print(f"Shape: {df_deal.shape}")

# Alternative method: Apply masks sequentially (less efficient)
# First filter by quality, then filter result by price
df_deal_alternative = df_house[df_house['OverallQual'] >= 8][df_house['SalePrice'] < 300000]
# Note: This alternative method may not work correctly - better to use combined mask

# Display sample records
print("\nFirst 10 houses in df_deal (great quality at affordable prices):")
# Select specific columns for better readability
display_cols = ['Neighborhood', 'OverallQual', 'OverallCond', 'YearBuilt', 'GrLivArea', 'SalePrice']
print(df_deal[display_cols].head(10))

# Analyze the deals
print("\nOverallQual distribution in df_deal:")
print(df_deal['OverallQual'].value_counts().sort_index())

print("\nPrice statistics for df_deal:")
print(f"Average SalePrice: ${df_deal['SalePrice'].mean():,.2f}")
print(f"Median SalePrice: ${df_deal['SalePrice'].median():,.2f}")
print(f"Min SalePrice: ${df_deal['SalePrice'].min():,}")
print(f"Max SalePrice: ${df_deal['SalePrice'].max():,}")

# Comparison with df_great
print("\nPrice comparison:")
print(f"df_great average: ${df_great['SalePrice'].mean():,.2f}")
print(f"df_deal average: ${df_deal['SalePrice'].mean():,.2f}")
savings = df_great['SalePrice'].mean() - df_deal['SalePrice'].mean()
print(f"Average savings: ${savings:,.2f} ({(savings / df_great['SalePrice'].mean() * 100):.1f}%)")

# Most common neighborhoods for deals
print("\nTop 5 neighborhoods for great deals:")
print(df_deal['Neighborhood'].value_counts().head(5))

# Year analysis
print("\nYear Built statistics for df_deal:")
print(f"Oldest house: {df_deal['YearBuilt'].min()}")
print(f"Newest house: {df_deal['YearBuilt'].max()}")
print(f"Average year: {df_deal['YearBuilt'].mean():.0f}")

# =============================================================================
# SUMMARY AND INSIGHTS
# =============================================================================

print("\n" + "="*70)
print("EXERCISE COMPLETED SUCCESSFULLY!")
print("="*70)

print("\nSummary of created DataFrames:")
print(f"1. df_house: {df_house.shape[0]} rows × {df_house.shape[1]} columns (full dataset)")
print(f"2. df_location: {df_location.shape[0]} rows × {df_location.shape[1]} columns (location data)")
print(f"3. df_location_first_100: {df_location_first_100.shape[0]} rows × {df_location_first_100.shape[1]} columns (first 100 records)")
print(f"4. df_great: {df_great.shape[0]} rows × {df_great.shape[1]} columns (OverallQual >= 8)")
print(f"5. df_deal: {df_deal.shape[0]} rows × {df_deal.shape[1]} columns (OverallQual >= 8 AND SalePrice < $300k)")

print("\nKey Findings:")
print(f"• House Id 222 price: ${df_house.loc[222, 'SalePrice']:,}")
print(f"• House Id 333 price: ${df_house.loc[333, 'SalePrice']:,}")
print(f"• High-quality houses (>= 8): {num_great_houses} ({(num_great_houses / len(df_house) * 100):.1f}%)")
print(f"• High-quality deals (>= 8, < $300k): {num_deals} ({(num_deals / len(df_house) * 100):.1f}%)")
print(f"• Quality premium: ${price_premium:,.2f} ({(price_premium / df_house['SalePrice'].mean() * 100):.1f}%)")

print("\nInsights:")
print(f"• {(num_deals / num_great_houses * 100):.1f}% of high-quality houses are under $300k")
print(f"• Average savings on deals: ${savings:,.2f} compared to all high-quality homes")
print(f"• Top deal neighborhood: {df_deal['Neighborhood'].value_counts().index[0]}")

print("\nAll tasks completed successfully! ✓")

# Standard Python idiom to check if script is being run directly
# Code inside only executes when running this file, not when importing it
if __name__ == "__main__":
    pass
