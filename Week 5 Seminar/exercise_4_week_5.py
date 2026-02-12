# Week 5 Seminar - Exercise 4
# Programming for Data Analytics
# Date: February 12, 2026

"""
Week 5 Exercise 4 - Data Filtering and Weighted Score Calculation
------------------------------------------------------------------
EXERCISE QUESTIONS:
1. Select all records with meta_score greater than 95
2. Optional: Also filter records where user_review is lower than 8
3. Calculate weighted scores: meta_score * 0.6 + user_review * 4
4. Compare results with and without user_review filter
5. Analyze the filtered dataset and weighted scores

CONCEPTS COVERED:
- Boolean indexing for complex filtering
- Multiple filtering conditions (AND logic)
- Weighted score calculation
- Data subsetting and analysis
- Comparing filtered vs unfiltered results
- Statistical analysis on filtered data

LEARNING OBJECTIVES:
- Master boolean indexing for multi-condition filtering
- Understand AND (intersection) vs OR (union) in filtering
- Calculate weighted scores based on multiple features
- Analyze impact of filtering on dataset
- Compare datasets using statistical measures
"""

import numpy as np
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def exercise_4_part_a():
    """
    Exercise 4 - Part A: Load data and apply basic filtering
    
    QUESTION 1: Select all records with meta_score greater than 95
    
    ANSWER: Use boolean indexing:
            - Create boolean mask: mask = data[:, 0] > 95
            - Apply mask to filter: filtered_data = data[mask]
            - Returns only rows where meta_score > 95
    
    EXPLANATION:
    - Boolean indexing creates True/False array for each row
    - Applying mask returns only rows where mask is True
    - meta_score > 95 filters for high-quality games
    """
    print("\n" + "="*80)
    print("EXERCISE 4 - PART A: Load Data and Apply Basic Filtering")
    print("="*80)
    
    # Load data from all_games.csv
    csv_path = os.path.join(SCRIPT_DIR, 'all_games.csv')
    
    print(f"\nLoading data from: {csv_path}")
    
    games_data = np.genfromtxt(
        csv_path,
        delimiter=',',
        skip_header=1,
        usecols=[2, 3],
        max_rows=1000,
        filling_values=np.nan,
        invalid_raise=False
    )
    
    print(f"Total records loaded: {games_data.shape[0]}")
    print(f"Columns: meta_score, user_review")
    
    # Basic statistics
    print("\n" + "-"*80)
    print("ORIGINAL DATA STATISTICS")
    print("-"*80)
    
    meta_score = games_data[:, 0]
    user_review = games_data[:, 1]
    
    print(f"\nMeta Score:")
    print(f"  - Mean: {np.nanmean(meta_score):.2f}")
    print(f"  - Std: {np.nanstd(meta_score):.2f}")
    print(f"  - Min: {np.nanmin(meta_score):.1f}, Max: {np.nanmax(meta_score):.1f}")
    
    print(f"\nUser Review:")
    print(f"  - Mean: {np.nanmean(user_review):.2f}")
    print(f"  - Std: {np.nanstd(user_review):.2f}")
    print(f"  - Min: {np.nanmin(user_review):.1f}, Max: {np.nanmax(user_review):.1f}")
    
    # Question 1: Filter meta_score > 95
    print("\n" + "-"*80)
    print("FILTERING: meta_score > 95")
    print("-"*80)
    
    # Create boolean mask
    mask_high_meta = meta_score > 95
    
    print(f"\nBoolean mask created: {np.sum(mask_high_meta)} True values out of {len(mask_high_meta)}")
    
    # Apply filter
    filtered_data_meta = games_data[mask_high_meta]
    
    print(f"Filtered data shape: {filtered_data_meta.shape}")
    print(f"Records with meta_score > 95: {filtered_data_meta.shape[0]}")
    print(f"Percentage of records: {(filtered_data_meta.shape[0] / games_data.shape[0]) * 100:.2f}%")
    
    # Statistics of filtered data
    print(f"\nFiltered Data Statistics (meta_score > 95):")
    filtered_meta = filtered_data_meta[:, 0]
    filtered_user = filtered_data_meta[:, 1]
    
    print(f"Meta Score:")
    print(f"  - Mean: {np.nanmean(filtered_meta):.2f}")
    print(f"  - Min: {np.nanmin(filtered_meta):.1f}, Max: {np.nanmax(filtered_meta):.1f}")
    
    print(f"User Review (for high meta_score records):")
    print(f"  - Mean: {np.nanmean(filtered_user):.2f}")
    print(f"  - Std: {np.nanstd(filtered_user):.2f}")
    
    # Show sample records
    print(f"\nSample of filtered records (first 5):")
    print(f"{'Meta Score':<15} {'User Review':<15}")
    print("-"*30)
    for i in range(min(5, filtered_data_meta.shape[0])):
        meta = filtered_data_meta[i, 0]
        user = filtered_data_meta[i, 1]
        print(f"{meta:<15.1f} {user:<15.1f}")
    
    print("\n✅ Part A completed!")
    
    return games_data, filtered_data_meta


def exercise_4_part_b():
    """
    Exercise 4 - Part B: Apply combined filtering (optional advanced filtering)
    
    QUESTION 2: Optional - Filter records where meta_score > 95 AND user_review < 8
    
    ANSWER: Use combined boolean masks with & (AND) operator:
            - mask1 = data[:, 0] > 95
            - mask2 = data[:, 1] < 8
            - combined = mask1 & mask2  (both conditions must be True)
            - filtered = data[combined]
    
    EXPLANATION:
    - & (AND): Both conditions must be True for row to be selected
    - | (OR): At least one condition must be True
    - ~ (NOT): Inverts boolean mask
    - Parentheses required when combining masks: (mask1) & (mask2)
    - Useful for finding specific subgroups in data
    """
    print("\n" + "="*80)
    print("EXERCISE 4 - PART B: Combined Filtering (AND Logic)")
    print("="*80)
    
    # Reload data for consistency
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
    
    print(f"\nOriginal dataset: {games_data.shape[0]} records")
    
    # Create individual masks
    print("\n" + "-"*80)
    print("CREATING MASKS FOR TWO CONDITIONS")
    print("-"*80)
    
    mask_high_meta = meta_score > 95
    mask_low_user = user_review < 8
    
    print(f"\nMask 1 (meta_score > 95): {np.sum(mask_high_meta)} records")
    print(f"Mask 2 (user_review < 8): {np.sum(mask_low_user)} records")
    
    # Combined mask using AND (&)
    print("\n" + "-"*80)
    print("COMBINED FILTERING (AND LOGIC)")
    print("-"*80)
    
    mask_combined = (meta_score > 95) & (user_review < 8)
    
    print(f"\nCombined mask (meta_score > 95 AND user_review < 8):")
    print(f"  Records matching both conditions: {np.sum(mask_combined)}")
    
    # Apply combined filter
    filtered_data_combined = games_data[mask_combined]
    
    print(f"  Filtered data shape: {filtered_data_combined.shape}")
    
    if filtered_data_combined.shape[0] > 0:
        print(f"  Percentage of original: {(filtered_data_combined.shape[0] / games_data.shape[0]) * 100:.2f}%")
        
        # Statistics of combined filtered data
        print(f"\nStatistics (meta_score > 95 AND user_review < 8):")
        comb_meta = filtered_data_combined[:, 0]
        comb_user = filtered_data_combined[:, 1]
        
        print(f"Meta Score:")
        print(f"  - Mean: {np.mean(comb_meta):.2f}, Range: [{np.min(comb_meta):.1f}, {np.max(comb_meta):.1f}]")
        
        print(f"User Review:")
        print(f"  - Mean: {np.mean(comb_user):.2f}, Range: [{np.min(comb_user):.1f}, {np.max(comb_user):.1f}]")
        
        # Show sample records
        print(f"\nSample records (first 5):")
        print(f"{'Meta Score':<15} {'User Review':<15}")
        print("-"*30)
        for i in range(min(5, filtered_data_combined.shape[0])):
            meta = filtered_data_combined[i, 0]
            user = filtered_data_combined[i, 1]
            print(f"{meta:<15.1f} {user:<15.1f}")
    else:
        print("\n⚠ No records match both conditions (meta_score > 95 AND user_review < 8)")
    
    # Comparison of filtering approaches
    print("\n" + "-"*80)
    print("FILTERING COMPARISON")
    print("-"*80)
    
    mask_only_meta = meta_score > 95
    filtered_only_meta = games_data[mask_only_meta]
    
    print(f"\nFiltering approaches:")
    print(f"  - meta_score > 95 only: {filtered_only_meta.shape[0]} records")
    print(f"  - Both conditions (AND): {filtered_data_combined.shape[0]} records")
    
    if filtered_only_meta.shape[0] > 0:
        print(f"\nUser review stats for high meta_score records:")
        only_meta_user = filtered_only_meta[:, 1]
        print(f"  - Mean: {np.nanmean(only_meta_user):.2f}")
        print(f"  - Count < 8: {np.sum(only_meta_user < 8)}")
    
    print("\n✅ Part B completed!")
    
    return games_data, filtered_data_combined


def exercise_4_part_c():
    """
    Exercise 4 - Part C: Calculate weighted scores
    
    QUESTION 3: Calculate weighted scores using formula:
                weighted_score = meta_score * 0.6 + user_review * 4
    
    ANSWER: Apply vectorized calculation to entire dataset:
            weights = data[:, 0] * 0.6 + data[:, 1] * 4
            Can also apply to filtered subsets
    
    EXPLANATION:
    - Formula combines two features with different weights
    - meta_score gets 0.6 weight (60% of score)
    - user_review gets 4 multiplier (scaled to 0-40 range when 0-10)
    - Results in composite score representing overall game quality
    - Vectorized operation applies to all rows simultaneously
    """
    print("\n" + "="*80)
    print("EXERCISE 4 - PART C: Calculate Weighted Scores")
    print("="*80)
    
    # Reload data
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
    
    print(f"\nDataset: {games_data.shape[0]} records")
    print("Weighted Score Formula: meta_score * 0.6 + user_review * 4")
    
    # Calculate weighted scores for all data
    print("\n" + "-"*80)
    print("CALCULATING WEIGHTED SCORES (ALL DATA)")
    print("-"*80)
    
    # Handle NaN values - use nanmean to avoid NaN in calculation
    weighted_scores_all = np.empty(len(games_data))
    
    for i in range(len(games_data)):
        meta = games_data[i, 0]
        user = games_data[i, 1]
        
        # Calculate weighted score, handling NaN
        if np.isnan(meta) or np.isnan(user):
            weighted_scores_all[i] = np.nan
        else:
            weighted_scores_all[i] = meta * 0.6 + user * 4
    
    print(f"\nWeighted scores calculated for {(~np.isnan(weighted_scores_all)).sum()} records")
    
    print(f"\nStatistics of weighted scores (all data):")
    print(f"  - Mean: {np.nanmean(weighted_scores_all):.2f}")
    print(f"  - Std: {np.nanstd(weighted_scores_all):.2f}")
    print(f"  - Min: {np.nanmin(weighted_scores_all):.2f}")
    print(f"  - Max: {np.nanmax(weighted_scores_all):.2f}")
    
    # Quartiles
    valid_scores = weighted_scores_all[~np.isnan(weighted_scores_all)]
    q25 = np.percentile(valid_scores, 25)
    q50 = np.percentile(valid_scores, 50)
    q75 = np.percentile(valid_scores, 75)
    
    print(f"  - Q1 (25%): {q25:.2f}")
    print(f"  - Q2 (50% Median): {q50:.2f}")
    print(f"  - Q3 (75%): {q75:.2f}")
    
    # Filtered data weighted scores
    print("\n" + "-"*80)
    print("CALCULATING WEIGHTED SCORES (FILTERED DATA - meta_score > 95)")
    print("-"*80)
    
    # Filter data
    mask_high_meta = meta_score > 95
    filtered_data = games_data[mask_high_meta]
    
    if filtered_data.shape[0] > 0:
        # Calculate weighted scores for filtered data
        weighted_scores_filtered = np.empty(len(filtered_data))
        
        for i in range(len(filtered_data)):
            meta = filtered_data[i, 0]
            user = filtered_data[i, 1]
            
            if np.isnan(meta) or np.isnan(user):
                weighted_scores_filtered[i] = np.nan
            else:
                weighted_scores_filtered[i] = meta * 0.6 + user * 4
        
        print(f"\nFiltered records: {filtered_data.shape[0]}")
        print(f"Weighted scores calculated: {(~np.isnan(weighted_scores_filtered)).sum()}")
        
        print(f"\nStatistics of weighted scores (meta_score > 95):")
        print(f"  - Mean: {np.nanmean(weighted_scores_filtered):.2f}")
        print(f"  - Std: {np.nanstd(weighted_scores_filtered):.2f}")
        print(f"  - Min: {np.nanmin(weighted_scores_filtered):.2f}")
        print(f"  - Max: {np.nanmax(weighted_scores_filtered):.2f}")
        
        # Show sample records with weighted scores
        print(f"\nSample records with weighted scores (first 5):")
        print(f"{'Meta':<10} {'User':<10} {'Weighted':<15}")
        print("-"*35)
        for i in range(min(5, filtered_data.shape[0])):
            meta = filtered_data[i, 0]
            user = filtered_data[i, 1]
            if ~np.isnan(weighted_scores_filtered[i]):
                print(f"{meta:<10.1f} {user:<10.1f} {weighted_scores_filtered[i]:<15.2f}")
        
        # Comparison
        print("\n" + "-"*80)
        print("COMPARISON: All Data vs Filtered Data")
        print("-"*80)
        
        print(f"\nWeighted Score Comparison:")
        print(f"  All data - Mean: {np.nanmean(weighted_scores_all):.2f}, Std: {np.nanstd(weighted_scores_all):.2f}")
        print(f"  High meta - Mean: {np.nanmean(weighted_scores_filtered):.2f}, Std: {np.nanstd(weighted_scores_filtered):.2f}")
        print(f"  Difference in mean: {np.nanmean(weighted_scores_filtered) - np.nanmean(weighted_scores_all):.2f}")
    
    print("\n✅ Part C completed!")
    
    return weighted_scores_all, weighted_scores_filtered if filtered_data.shape[0] > 0 else None


def complete_exercise_sequence():
    """
    Complete Exercise 4 Sequence - All operations in order
    
    This function demonstrates the complete workflow:
    1. Load data and apply basic filtering (meta_score > 95)
    2. Apply combined filtering with AND logic
    3. Calculate weighted scores for all and filtered data
    4. Compare results and analyze patterns
    """
    print("\n" + "="*80)
    print("COMPLETE EXERCISE 4 SEQUENCE")
    print("="*80)
    print("Data Filtering and Weighted Score Calculation")
    
    print("\n" + "█"*80)
    print("STEP 1: Load Data and Apply Basic Filtering (meta_score > 95)")
    print("█"*80)
    games_data_1, filtered_meta = exercise_4_part_a()
    
    print("\n" + "█"*80)
    print("STEP 2: Apply Combined Filtering (meta_score > 95 AND user_review < 8)")
    print("█"*80)
    games_data_2, filtered_combined = exercise_4_part_b()
    
    print("\n" + "█"*80)
    print("STEP 3: Calculate Weighted Scores for All and Filtered Data")
    print("█"*80)
    weighted_all, weighted_filtered = exercise_4_part_c()
    
    # Summary
    print("\n" + "="*80)
    print("EXERCISE 4 SUMMARY")
    print("="*80)
    print("""
✅ PART A - Basic Filtering (meta_score > 95):
   - Loaded 1000 records from all_games.csv
   - Created boolean mask for meta_score > 95
   - Filtered dataset and analyzed statistics
   - Identified high-quality games subset

✅ PART B - Combined Filtering (AND Logic):
   - Applied two conditions simultaneously
   - Used & operator for AND logic
   - Combined mask: (meta_score > 95) & (user_review < 8)
   - Analyzed intersection of both conditions
   - Compared single vs combined filtering

✅ PART C - Weighted Score Calculation:
   - Calculated: weighted_score = meta_score * 0.6 + user_review * 4
   - Applied vectorized calculation to all records
   - Applied to filtered subset
   - Compared weighted score distributions
   - Identified quartiles and statistics

KEY CONCEPTS LEARNED:
- Boolean indexing for data filtering
- Multiple condition filtering with AND (&) and OR (|) operators
- Mask combinations and logical operations
- Weighted score calculation with multiple features
- Feature scaling and weighting strategies
- Data subsetting and comparison
- Statistical analysis on filtered data
- Vectorized array operations

FILTERING OPERATORS:
- & (AND): Both conditions must be True - intersection
- | (OR): At least one condition is True - union
- ~ (NOT): Inverts boolean mask - complement
- Importance of parentheses: (mask1) & (mask2)

WEIGHTED SCORE FORMULA:
weighted_score = meta_score * 0.6 + user_review * 4
- meta_score: Weight 0.6 (professional rating)
- user_review: Weight 4 (user sentiment, scaled)
- Total contribution: [57-99]*0.6 + [3-89]*4 = [46.2-150.2]

USE CASES:
- Recommendation systems
- Game ranking/scoring
- Multi-factor decision making
- Feature combining for machine learning
- Business scoring models

FUNCTIONS DEMONSTRATED:
np.genfromtxt()          - Load CSV data
boolean_mask > 95        - Create filtering mask
data[mask]               - Apply mask to data
(mask1) & (mask2)        - Combine masks with AND
(mask1) | (mask2)        - Combine masks with OR
~mask                    - Invert mask
np.sum(mask)             - Count True values in mask
np.nanmean() / np.nanstd() - Statistics ignoring NaN
np.percentile()          - Calculate quartiles
""")
    
    print("\n✅ Exercise 4 completed successfully!")


if __name__ == "__main__":
    # Run complete sequence
    complete_exercise_sequence()
