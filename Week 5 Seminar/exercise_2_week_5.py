# Week 5 Seminar - Exercise 2
# Programming for Data Analytics
# Date: February 12, 2026

"""
Week 5 Exercise 2 - Loading CSV Data with Irregular Values
-----------------------------------------------------------
EXERCISE QUESTION:
Load the first 1000 records stored in file "all_games.csv" into a numpy array.
You only need to load columns "meta_score" and "user_review", and irregular 
data should be properly dealt with.

CONCEPTS COVERED:
- Loading CSV files with np.genfromtxt()
- Handling missing/irregular data (e.g., "tbd" values)
- Selecting specific columns with usecols
- Limiting rows with max_rows
- Data type conversion and validation
- Dealing with non-numeric data in numeric columns

LEARNING OBJECTIVES:
- Understand how to load real-world CSV data with missing values
- Master column selection and row limiting
- Handle data quality issues (missing values, text in numeric columns)
- Use appropriate NumPy functions for data loading
"""

import numpy as np
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def exercise_2_part_a():
    """
    Exercise 2 - Part A: Load CSV with irregular data
    
    QUESTION: Load the first 1000 records from "all_games.csv" into a numpy array.
              Only load columns "meta_score" and "user_review".
              Deal with irregular data properly (e.g., "tbd" values).
    
    ANSWER: Use np.genfromtxt() with these parameters:
            - delimiter=',' for CSV format
            - skip_header=1 to skip column names
            - usecols=[2, 3] to select meta_score (column 2) and user_review (column 3)
            - max_rows=1000 to limit to first 1000 records
            - filling_values=np.nan to replace irregular data with NaN
            - invalid_raise=False to handle non-numeric values gracefully
    
    DATA QUALITY NOTES:
    - The CSV has 7 columns: name, platform, meta_score, user_review, year, month, day
    - meta_score is at index 2, user_review is at index 3
    - Some user_review values are "tbd" (to be determined) - these are irregular/missing
    - np.genfromtxt() automatically converts "tbd" to NaN when loading as float
    """
    print("\n" + "="*80)
    print("EXERCISE 2 - PART A: Load CSV Data with Irregular Values")
    print("="*80)
    
    # Construct absolute path to the CSV file
    csv_path = os.path.join(SCRIPT_DIR, 'all_games.csv')
    
    print(f"\nLoading data from: {csv_path}")
    print("Target: First 1000 records, columns 'meta_score' and 'user_review'")
    
    # Method 1: Using np.genfromtxt() - Best for handling irregular data
    print("\n" + "-"*80)
    print("METHOD 1: Using np.genfromtxt() (handles irregular data automatically)")
    print("-"*80)
    
    # Load the data
    # Column indices: 0=name, 1=platform, 2=meta_score, 3=user_review, 4=year, 5=month, 6=day
    games_data = np.genfromtxt(
        csv_path,
        delimiter=',',           # CSV format
        skip_header=1,           # Skip the header row
        usecols=[2, 3],          # Select only meta_score and user_review
        max_rows=1000,           # Load first 1000 records
        filling_values=np.nan,   # Replace missing/invalid values with NaN
        invalid_raise=False      # Don't raise error on invalid values
    )
    
    print(f"\nLoaded array shape: {games_data.shape}")
    print(f"Data type: {games_data.dtype}")
    print(f"\nFirst 10 rows:")
    print(games_data[:10])
    
    # Check for missing/irregular data
    print(f"\n" + "-"*80)
    print("DATA QUALITY ANALYSIS:")
    print("-"*80)
    
    # Count NaN values
    nan_count = np.isnan(games_data).sum()
    total_values = games_data.size
    nan_percentage = (nan_count / total_values) * 100
    
    print(f"Total values: {total_values}")
    print(f"NaN (missing) values: {nan_count}")
    print(f"Percentage missing: {nan_percentage:.2f}%")
    
    # Check each column separately
    meta_score_col = games_data[:, 0]
    user_review_col = games_data[:, 1]
    
    meta_score_nan = np.isnan(meta_score_col).sum()
    user_review_nan = np.isnan(user_review_col).sum()
    
    print(f"\nColumn 0 (meta_score): {meta_score_nan} NaN values ({(meta_score_nan/1000)*100:.2f}%)")
    print(f"Column 1 (user_review): {user_review_nan} NaN values ({(user_review_nan/1000)*100:.2f}%)")
    
    # Display some rows with NaN values (if any)
    if nan_count > 0:
        print(f"\n" + "-"*80)
        print("SAMPLE ROWS WITH MISSING DATA:")
        print("-"*80)
        
        # Find rows with any NaN values
        rows_with_nan = np.any(np.isnan(games_data), axis=1)
        nan_row_indices = np.where(rows_with_nan)[0]
        
        print(f"Found {len(nan_row_indices)} rows with missing values")
        print(f"First 5 rows with NaN:")
        for i in nan_row_indices[:5]:
            print(f"  Row {i}: meta_score={games_data[i, 0]}, user_review={games_data[i, 1]}")
    
    return games_data


def exercise_2_part_b():
    """
    Exercise 2 - Part B: Statistical Analysis of Loaded Data
    
    This part demonstrates what you can do with the loaded data,
    including handling missing values in calculations.
    
    STATISTICAL OPERATIONS:
    - np.nanmean() - Mean ignoring NaN values
    - np.nanmedian() - Median ignoring NaN values
    - np.nanstd() - Standard deviation ignoring NaN values
    - np.nanmin() / np.nanmax() - Min/Max ignoring NaN values
    """
    print("\n" + "="*80)
    print("EXERCISE 2 - PART B: Statistical Analysis")
    print("="*80)
    
    # Load the data
    csv_path = os.path.join(SCRIPT_DIR, 'all_games.csv')
    games_data = np.genfromtxt(
        csv_path,
        delimiter=',',
        skip_header=1,
        usecols=[2, 3],
        max_rows=1000,
        filling_values=np.nan,
        invalid_raise=False
    )
    
    meta_score = games_data[:, 0]
    user_review = games_data[:, 1]
    
    print("\nSTATISTICAL SUMMARY (using nan-aware functions):")
    print("-"*80)
    
    # Meta Score statistics
    print("\nMETA SCORE:")
    print(f"  Mean:   {np.nanmean(meta_score):.2f}")
    print(f"  Median: {np.nanmedian(meta_score):.2f}")
    print(f"  Std Dev: {np.nanstd(meta_score):.2f}")
    print(f"  Min:    {np.nanmin(meta_score):.2f}")
    print(f"  Max:    {np.nanmax(meta_score):.2f}")
    
    # User Review statistics
    print("\nUSER REVIEW:")
    print(f"  Mean:   {np.nanmean(user_review):.2f}")
    print(f"  Median: {np.nanmedian(user_review):.2f}")
    print(f"  Std Dev: {np.nanstd(user_review):.2f}")
    print(f"  Min:    {np.nanmin(user_review):.2f}")
    print(f"  Max:    {np.nanmax(user_review):.2f}")
    
    return games_data


def exercise_2_part_c():
    """
    Exercise 2 - Part C: Data Cleaning Options
    
    This part demonstrates different strategies for handling missing data.
    
    CLEANING STRATEGIES:
    1. Remove rows with any NaN values
    2. Remove rows where specific column has NaN
    3. Fill NaN with a value (mean, median, or constant)
    """
    print("\n" + "="*80)
    print("EXERCISE 2 - PART C: Data Cleaning Strategies")
    print("="*80)
    
    # Load the data
    csv_path = os.path.join(SCRIPT_DIR, 'all_games.csv')
    games_data = np.genfromtxt(
        csv_path,
        delimiter=',',
        skip_header=1,
        usecols=[2, 3],
        max_rows=1000,
        filling_values=np.nan,
        invalid_raise=False
    )
    
    print(f"\nOriginal data shape: {games_data.shape}")
    
    # Strategy 1: Remove rows with ANY NaN values
    print("\n" + "-"*80)
    print("STRATEGY 1: Remove rows with ANY NaN values")
    print("-"*80)
    
    # Find rows without any NaN
    clean_rows = ~np.any(np.isnan(games_data), axis=1)
    cleaned_data_1 = games_data[clean_rows]
    
    print(f"Cleaned data shape: {cleaned_data_1.shape}")
    print(f"Rows removed: {games_data.shape[0] - cleaned_data_1.shape[0]}")
    
    # Strategy 2: Remove rows where user_review is NaN only
    print("\n" + "-"*80)
    print("STRATEGY 2: Remove rows where user_review (column 1) is NaN")
    print("-"*80)
    
    # Find rows where user_review is not NaN
    valid_user_review = ~np.isnan(games_data[:, 1])
    cleaned_data_2 = games_data[valid_user_review]
    
    print(f"Cleaned data shape: {cleaned_data_2.shape}")
    print(f"Rows removed: {games_data.shape[0] - cleaned_data_2.shape[0]}")
    
    # Strategy 3: Fill NaN values with mean
    print("\n" + "-"*80)
    print("STRATEGY 3: Fill NaN values with column mean")
    print("-"*80)
    
    # Create a copy to modify
    filled_data = games_data.copy()
    
    # Fill NaN in meta_score with its mean
    meta_mean = np.nanmean(filled_data[:, 0])
    meta_nan_mask = np.isnan(filled_data[:, 0])
    filled_data[meta_nan_mask, 0] = meta_mean
    
    # Fill NaN in user_review with its mean
    user_mean = np.nanmean(filled_data[:, 1])
    user_nan_mask = np.isnan(filled_data[:, 1])
    filled_data[user_nan_mask, 1] = user_mean
    
    print(f"Filled data shape: {filled_data.shape} (no rows removed)")
    print(f"NaN count after filling: {np.isnan(filled_data).sum()}")
    print(f"Meta score mean used for filling: {meta_mean:.2f}")
    print(f"User review mean used for filling: {user_mean:.2f}")
    
    return cleaned_data_1, cleaned_data_2, filled_data


def complete_exercise_sequence():
    """
    Run the complete exercise in sequence
    
    COMPLETE WORKFLOW:
    This function demonstrates the full data loading and cleaning pipeline:
    1. Load CSV with irregular data
    2. Analyze data quality
    3. Compute statistics (handling NaN)
    4. Apply cleaning strategy
    5. Verify results
    """
    print("\n" + "="*80)
    print("COMPLETE EXERCISE SEQUENCE")
    print("="*80)
    
    csv_path = os.path.join(SCRIPT_DIR, 'all_games.csv')
    
    # Step 1: Load data
    print("\nStep 1: Load first 1000 records (meta_score, user_review)")
    games_data = np.genfromtxt(
        csv_path,
        delimiter=',',
        skip_header=1,
        usecols=[2, 3],
        max_rows=1000,
        filling_values=np.nan,
        invalid_raise=False
    )
    print(f"Loaded shape: {games_data.shape}")
    
    # Step 2: Check data quality
    print("\nStep 2: Check for missing values")
    nan_count = np.isnan(games_data).sum()
    print(f"Missing values: {nan_count} ({(nan_count/games_data.size)*100:.2f}%)")
    
    # Step 3: Compute statistics
    print("\nStep 3: Compute statistics (ignoring NaN)")
    print(f"Meta score: mean={np.nanmean(games_data[:, 0]):.2f}, std={np.nanstd(games_data[:, 0]):.2f}")
    print(f"User review: mean={np.nanmean(games_data[:, 1]):.2f}, std={np.nanstd(games_data[:, 1]):.2f}")
    
    # Step 4: Clean data (remove rows with NaN)
    print("\nStep 4: Clean data (remove rows with any NaN)")
    clean_rows = ~np.any(np.isnan(games_data), axis=1)
    cleaned_data = games_data[clean_rows]
    print(f"Cleaned shape: {cleaned_data.shape}")
    print(f"Removed {games_data.shape[0] - cleaned_data.shape[0]} rows")
    
    # Step 5: Verify cleaned data
    print("\nStep 5: Verify cleaned data")
    remaining_nan = np.isnan(cleaned_data).sum()
    print(f"Remaining NaN values: {remaining_nan}")
    print(f"First 5 rows of cleaned data:")
    print(cleaned_data[:5])
    
    print("\n" + "-"*80)
    print("SUMMARY:")
    print(f"  Original: {games_data.shape[0]} rows, {nan_count} missing values")
    print(f"  Cleaned:  {cleaned_data.shape[0]} rows, {remaining_nan} missing values")
    print(f"  Data is ready for analysis!")
    print("-"*80)


def main():
    """Main function to run Exercise 2."""
    print("="*80)
    print("WEEK 5 SEMINAR - EXERCISE 2")
    print("Programming for Data Analytics")
    print("="*80)
    
    # Run exercise parts separately
    print("\n" + "▶"*40)
    print("PART 1: Individual Demonstrations")
    print("▶"*40)
    exercise_2_part_a()  # Load data with irregular values
    exercise_2_part_b()  # Statistical analysis
    exercise_2_part_c()  # Data cleaning strategies
    
    # Run complete sequence
    print("\n" + "▶"*40)
    print("PART 2: Complete Workflow")
    print("▶"*40)
    complete_exercise_sequence()
    
    print("\n" + "="*80)
    print("Exercise 2 completed!")
    print("="*80)


if __name__ == "__main__":
    main()
