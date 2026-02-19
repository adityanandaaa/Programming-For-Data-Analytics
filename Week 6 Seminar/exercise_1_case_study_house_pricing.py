"""
Week 6 Seminar: Case Study 1 - House Pricing Exercise 1
========================================================

Dataset: House sales data from Ames, Iowa
Source: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data

Tasks:
1. Import house_price.csv into DataFrame with 'id' as row index
2. Import house_price.xlsx Excel file
3. Create Pandas Series 'price' from 'SalePrice' column
4. Create DataFrame 'df_location' from 'Neighborhood' and 'Condition1' columns

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
print("CASE STUDY 1: HOUSE PRICING EXERCISE 1")
print("="*70)

# =============================================================================
# TASK 1: Import house_price.csv with 'Id' as row index
# =============================================================================

print("\n" + "-"*70)
print("TASK 1: Import house_price.csv into DataFrame with 'Id' as row index")
print("-"*70)

# Construct the full file path to house_price.csv
csv_file_path = os.path.join(data_dir, 'house_price.csv')
print(f"\nFile path: {csv_file_path}")

# Read CSV file into a DataFrame
# index_col='Id' sets the 'Id' column as the row index instead of default numeric index
# This makes it easier to reference rows by their ID numbers
df_house = pd.read_csv(csv_file_path, index_col='Id')

print("\nDataFrame df_house loaded successfully!")
# Display the number of rows and columns in the DataFrame
print(f"Shape: {df_house.shape}")
# Display the name of the index column
print(f"Index name: {df_house.index.name}")

print("\nFirst 5 rows:")
# Display the first 5 rows of the DataFrame to preview the data
print(df_house.head())

print("\nDataFrame info:")
# Display detailed information about the DataFrame:
# - Number of entries (rows)
# - Column names and their data types
# - Non-null counts for each column (helps identify missing values)
# - Memory usage
print(df_house.info())

print("\nColumn names:")
# Convert column Index object to a list and display all column names
print(df_house.columns.tolist())

# =============================================================================
# TASK 2: Import house_price.xlsx Excel file
# =============================================================================

print("\n" + "-"*70)
print("TASK 2: Import house_price.xlsx Excel file")
print("-"*70)

print("\nNote: To read Excel files, pandas uses the 'openpyxl' library.")
print("If not installed, run: pip install openpyxl")

# Use try-except block to handle potential errors when reading Excel files
try:
    # Construct the full file path to house_price.xlsx
    excel_file_path = os.path.join(data_dir, 'house_price.xlsx')
    print(f"\nFile path: {excel_file_path}")
    
    # Read Excel file into a DataFrame
    # read_excel() is the pandas function for reading Excel files
    # index_col='Id' sets the 'Id' column as the row index
    # Requires openpyxl library to be installed
    df_house_excel = pd.read_excel(excel_file_path, index_col='Id')
    
    print("\nDataFrame df_house_excel loaded successfully!")
    # Display the dimensions (rows, columns) of the Excel DataFrame
    print(f"Shape: {df_house_excel.shape}")
    # Display the index column name
    print(f"Index name: {df_house_excel.index.name}")
    
    print("\nFirst 5 rows:")
    # Show preview of first 5 rows from Excel file
    print(df_house_excel.head())
    
    print("\nVerify Excel and CSV data are identical:")
    # Compare if both DataFrames (CSV and Excel) have identical data
    # .equals() returns True if all values and structure match
    if df_house.equals(df_house_excel):
        print("✓ Both DataFrames are identical!")
    else:
        print("Note: DataFrames may have minor differences in data types or precision")
        print(f"CSV shape: {df_house.shape}, Excel shape: {df_house_excel.shape}")

# Catch ImportError if openpyxl is not installed
except ImportError as e:
    print(f"\nError: {e}")
    print("Please install openpyxl: pip install openpyxl")
# Catch any other exceptions that might occur
except Exception as e:
    print(f"\nError loading Excel file: {e}")

# =============================================================================
# TASK 3: Create Pandas Series 'price' from 'SalePrice' column
# =============================================================================

print("\n" + "-"*70)
print("TASK 3: Create Pandas Series 'price' from 'SalePrice' column")
print("-"*70)

# Extract a single column from DataFrame using bracket notation
# This creates a Series object (one-dimensional labeled array)
# The Series will maintain the same index as the original DataFrame
price = df_house['SalePrice']

print("\nSeries 'price' created successfully!")
# Verify that the object is a pandas Series
print(f"Type: {type(price)}")
# Display the name of the Series (inherited from the column name)
print(f"Name: {price.name}")
# Display the number of elements in the Series
print(f"Length: {len(price)}")
# Display the data type of the values in the Series (int64 = 64-bit integer)
print(f"Data type: {price.dtype}")

print("\nFirst 10 values:")
# Display the first 10 sale prices with their Id index
print(price.head(10))

print("\nStatistical summary:")
# Generate comprehensive statistics: count, mean, std, min, quartiles, max
print(price.describe())

print("\nBasic statistics:")
# Calculate and display the average (mean) sale price
print(f"Mean price: ${price.mean():,.2f}")
# Calculate and display the middle value (50th percentile)
print(f"Median price: ${price.median():,.2f}")
# Find and display the lowest sale price
print(f"Min price: ${price.min():,.2f}")
# Find and display the highest sale price
print(f"Max price: ${price.max():,.2f}")
# Calculate the standard deviation (measure of price variation)
print(f"Standard deviation: ${price.std():,.2f}")

# =============================================================================
# TASK 4: Create DataFrame 'df_location' from 'Neighborhood' and 'Condition1'
# =============================================================================

print("\n" + "-"*70)
print("TASK 4: Create DataFrame 'df_location' from 'Neighborhood' and 'Condition1'")
print("-"*70)

# Select multiple columns from DataFrame using double bracket notation
# Outer brackets indicate we're indexing the DataFrame
# Inner list ['Neighborhood', 'Condition1'] specifies which columns to select
# Result is a new DataFrame with only these two columns
df_location = df_house[['Neighborhood', 'Condition1']]

print("\nDataFrame 'df_location' created successfully!")
# Verify the object type is a pandas DataFrame (not a Series)
print(f"Type: {type(df_location)}")
# Display the dimensions: (rows, columns)
print(f"Shape: {df_location.shape}")
# Display the list of column names in the new DataFrame
print(f"Columns: {df_location.columns.tolist()}")

print("\nFirst 10 rows:")
# Show the first 10 rows of location data
print(df_location.head(10))

print("\nDataFrame info:")
# Display structure info: data types, non-null counts, memory usage
print(df_location.info())

print("\nUnique values in each column:")
# Count how many distinct neighborhoods exist in the dataset
# .nunique() returns the number of unique non-null values
print(f"Unique Neighborhoods: {df_location['Neighborhood'].nunique()}")
# Count how many distinct condition types exist
print(f"Unique Conditions: {df_location['Condition1'].nunique()}")

print("\nNeighborhood distribution:")
# Count occurrences of each neighborhood and display top 10
# .value_counts() returns a Series with counts sorted in descending order
print(df_location['Neighborhood'].value_counts().head(10))

print("\nCondition1 distribution:")
# Count occurrences of each condition type and display all
print(df_location['Condition1'].value_counts())

# =============================================================================
# ADDITIONAL ANALYSIS
# =============================================================================

print("\n" + "="*70)
print("ADDITIONAL ANALYSIS")
print("="*70)

print("\nCombining location data with price:")
# Create a copy of df_location to avoid modifying the original DataFrame
# .copy() creates an independent copy, changes won't affect df_location
df_location_price = df_location.copy()
# Add the 'SalePrice' column to the location DataFrame
# This allows us to analyze prices by location
df_location_price['SalePrice'] = price

print("\nAverage price by Neighborhood (Top 10):")
# Group all houses by their Neighborhood
# Calculate the mean (average) SalePrice for each neighborhood
# Sort the results in descending order (highest prices first)
# Display only the top 10 most expensive neighborhoods
neighborhood_avg_price = df_location_price.groupby('Neighborhood')['SalePrice'].mean().sort_values(ascending=False)
print(neighborhood_avg_price.head(10))

print("\nAverage price by Condition1:")
# Group all houses by their Condition1 (proximity to various conditions)
# Calculate the average SalePrice for each condition type
# Sort in descending order to see which conditions have highest prices
condition_avg_price = df_location_price.groupby('Condition1')['SalePrice'].mean().sort_values(ascending=False)
print(condition_avg_price)

# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "="*70)
print("EXERCISE COMPLETED SUCCESSFULLY!")
print("="*70)

print("\nSummary of created objects:")
# Summarize the main DataFrame loaded from CSV
print(f"1. df_house: DataFrame with {df_house.shape[0]} rows, {df_house.shape[1]} columns")
print(f"   - Index: '{df_house.index.name}'")
print(f"   - Source: house_price.csv")

# Try to summarize the Excel DataFrame (may not exist if openpyxl not installed)
try:
    print(f"\n2. df_house_excel: DataFrame with {df_house_excel.shape[0]} rows, {df_house_excel.shape[1]} columns")
    print(f"   - Index: '{df_house_excel.index.name}'")
    print(f"   - Source: house_price.xlsx")
except:
    # If Excel DataFrame doesn't exist, inform user about the requirement
    print(f"\n2. df_house_excel: Not loaded (requires openpyxl)")

# Summarize the price Series
print(f"\n3. price: Series with {len(price)} values")
print(f"   - Name: '{price.name}'")
print(f"   - Mean: ${price.mean():,.2f}")

# Summarize the location DataFrame
print(f"\n4. df_location: DataFrame with {df_location.shape[0]} rows, {df_location.shape[1]} columns")
print(f"   - Columns: {df_location.columns.tolist()}")
print(f"   - Neighborhoods: {df_location['Neighborhood'].nunique()} unique")

print("\nAll tasks completed successfully! ✓")

# Standard Python idiom to check if script is being run directly
# Code inside only executes when running this file, not when importing it
if __name__ == "__main__":
    pass
