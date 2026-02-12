# Week 5 Seminar - Exercise 1
# Programming for Data Analytics
# Date: February 12, 2026

"""
Week 5 Exercise 1 - NumPy Array Manipulation
---------------------------------------------
EXERCISE QUESTIONS:
1. Create a 2D array of 16 random integers between 0 and 100
2. Reshape the array into a 4x4 2D-array
3. Extract the subarray consisting of the last two columns of first two rows
4. Find all numbers that are greater than 50 from the array
5. Replace these numbers with 0

CONCEPTS COVERED:
- np.random.randint(): Generate random integers
- reshape(): Convert 1D array to 2D array
- Array slicing: Extract subarrays using [row_start:row_end, col_start:col_end]
- Boolean masking: Create conditions to filter array elements
- In-place modification: Replace values based on conditions

LEARNING OBJECTIVES:
- Understand NumPy array creation and manipulation
- Practice array reshaping and slicing techniques
- Master boolean indexing for conditional operations
- Learn efficient array modification methods
"""

import numpy as np
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def exercise_1_part_a():
    """
    Exercise 1 - Part A: Create and reshape array
    
    QUESTION 1: Create a 2D array of 16 random integers between 0 and 100
    ANSWER: Use np.random.randint(0, 101, 16) to generate 16 random integers
            The range is [0, 101) which means 0 to 100 inclusive
    
    QUESTION 2: Reshape the array into a 4x4 2D-array
    ANSWER: Use .reshape(4, 4) method to convert 1D array (16 elements) into 2D array (4 rows × 4 columns)
            Total elements must match: 16 = 4 × 4
    """
    print("\n" + "="*80)
    print("EXERCISE 1 - PART A: Create 2D Array")
    print("="*80)
    
    # STEP 1: Create a 2D array of 16 random integers between 0 and 100
    # np.random.randint(low, high, size) generates random integers from low (inclusive) to high (exclusive)
    print("\n1. Creating array of 16 random integers between 0 and 100:")
    array_1d = np.random.randint(0, 101, 16)  # 101 because upper bound is exclusive
    print(f"1D Array:\n{array_1d}")
    
    # STEP 2: Reshape the array into a 4x4 2D-array
    # reshape(rows, cols) changes the shape without changing the data
    # Original: [a0, a1, a2, ..., a15] → New: [[a0, a1, a2, a3], [a4, a5, a6, a7], ...]
    print("\n2. Reshaping into 4x4 2D array:")
    array_2d = array_1d.reshape(4, 4)
    print(f"4x4 Array:\n{array_2d}")
    
    return array_2d


def exercise_1_part_b():
    """
    Exercise 1 - Part B: Extract subarray
    
    QUESTION 3: Extract the subarray consisting of the last two columns of first two rows
    ANSWER: Use array slicing with [row_slice, col_slice]
            - First two rows: [0:2] or [:2] means rows 0 and 1
            - Last two columns: [2:4] or [-2:] means columns 2 and 3 (the last two)
            - Combined: array_2d[0:2, 2:4] or array_2d[:2, -2:]
    
    SLICING SYNTAX EXPLANATION:
    - array[start:end] → elements from start to end-1
    - array[:n] → first n elements
    - array[-n:] → last n elements
    - array[row_slice, col_slice] → 2D slicing
    """
    print("\n" + "="*80)
    print("EXERCISE 1 - PART B: Extract Subarray")
    print("="*80)
    
    # Create array for demonstration
    array_2d = np.random.randint(0, 101, 16).reshape(4, 4)
    print(f"\nOriginal 4x4 Array:\n{array_2d}")
    
    # STEP 3: Extract the subarray consisting of the last two columns of first two rows
    # Slicing format: array[row_start:row_end, col_start:col_end]
    # First two rows: 0:2 (rows 0 and 1)
    # Last two columns: 2:4 (columns 2 and 3) or -2: (last 2 columns)
    print("\n3. Extracting last two columns of first two rows:")
    print("   Using slicing: array_2d[0:2, 2:4] or array_2d[:2, -2:]")
    subarray = array_2d[0:2, 2:4]
    print(f"Subarray (first 2 rows, last 2 columns):\n{subarray}")
    
    # Visual representation:
    # Original:          Extracted:
    # [[a, b, c, d]      [[c, d]
    #  [e, f, g, h]  →    [g, h]]
    #  [i, j, k, l]
    #  [m, n, o, p]]
    
    return array_2d


def exercise_1_part_c():
    """
    Exercise 1 - Part C: Find and replace values
    
    QUESTION 4: Find all numbers that are greater than 50 from the array
    ANSWER: Use boolean masking: array > 50 creates a boolean array (True/False)
            Then use array[mask] to extract elements where condition is True
    
    QUESTION 5: Replace these numbers with 0
    ANSWER: Use boolean indexing for assignment: array[mask] = 0
            This replaces all elements where mask is True with 0
    
    BOOLEAN MASKING EXPLANATION:
    - Condition creates boolean array: array > 50 → [True, False, True, ...]
    - Use mask to filter: array[mask] → returns only True elements
    - Use mask to modify: array[mask] = value → replaces True elements
    """
    print("\n" + "="*80)
    print("EXERCISE 1 - PART C: Find and Replace Values")
    print("="*80)
    
    # Create array for demonstration
    array_2d = np.random.randint(0, 101, 16).reshape(4, 4)
    print(f"\nOriginal Array:\n{array_2d}")
    
    # STEP 4: Find all numbers that are greater than 50 from the array
    # Boolean comparison creates a mask (True where condition is met, False otherwise)
    print("\n4. Finding all numbers greater than 50:")
    mask = array_2d > 50  # Creates boolean array
    print(f"Boolean mask (True where > 50):\n{mask}")
    
    # Use the mask to extract values (fancy indexing)
    numbers_greater_than_50 = array_2d[mask]  # Returns 1D array of values where mask is True
    print(f"\nNumbers greater than 50: {numbers_greater_than_50}")
    
    # STEP 5: Replace these numbers with 0
    # Boolean indexing can be used on the left side of assignment
    # This modifies the original array in-place
    print("\n5. Replacing all numbers > 50 with 0:")
    array_2d[mask] = 0  # All positions where mask is True are set to 0
    print(f"Array after replacement:\n{array_2d}")
    
    # Note: This is an in-place modification - the original array is changed
    # If you need to keep the original, make a copy first: array_copy = array_2d.copy()
    
    return array_2d


def complete_exercise_sequence():
    """
    Run the complete exercise in sequence with one array
    
    COMPLETE WORKFLOW:
    This function demonstrates all 5 steps applied sequentially to the same array,
    showing how NumPy operations can be chained together in a data processing pipeline.
    
    WORKFLOW STEPS:
    1. Generate random data → 2. Reshape data → 3. Extract subset → 4. Filter data → 5. Clean data
    """
    print("\n" + "="*80)
    print("COMPLETE EXERCISE SEQUENCE (All Steps on Same Array)")
    print("="*80)
    
    # STEP 1: Create a 2D array of 16 random integers between 0 and 100
    # Random seed can be set for reproducibility: np.random.seed(42)
    print("\nStep 1: Create array of 16 random integers between 0 and 100")
    array_1d = np.random.randint(0, 101, 16)
    print(f"1D Array: {array_1d}")
    
    # STEP 2: Reshape the array into a 4x4 2D-array
    # reshape() returns a view when possible (no data copying for efficiency)
    print("\nStep 2: Reshape into 4x4 2D array")
    array_2d = array_1d.reshape(4, 4)
    print(f"4x4 Array:\n{array_2d}")
    
    # STEP 3: Extract the subarray consisting of the last two columns of first two rows
    # Slicing creates a view (not a copy) - modifications affect original array
    print("\nStep 3: Extract subarray (first 2 rows, last 2 columns)")
    subarray = array_2d[0:2, 2:4]
    print(f"Subarray:\n{subarray}")
    
    # STEP 4: Find all numbers that are greater than 50 from the array
    # Boolean masking is very efficient - no loops needed
    print("\nStep 4: Find all numbers greater than 50")
    mask = array_2d > 50
    numbers_greater_than_50 = array_2d[mask]
    print(f"Numbers > 50: {numbers_greater_than_50}")
    print(f"Count: {len(numbers_greater_than_50)}")
    
    # STEP 5: Replace these numbers with 0
    # In-place modification using boolean indexing - memory efficient
    print("\nStep 5: Replace numbers > 50 with 0")
    array_2d[mask] = 0
    print(f"Final Array:\n{array_2d}")
    
    print("\n" + "-"*80)
    print("Summary:")
    print(f"  - Original array had {len(numbers_greater_than_50)} numbers > 50")
    print(f"  - All values > 50 have been replaced with 0")
    print(f"  - Extracted subarray was:\n{subarray}")
    print(f"  - Note: Subarray is now updated since it's a view of array_2d")
    print("-"*80)


def main():
    """Main function to run Exercise 1."""
    print("="*80)
    print("WEEK 5 SEMINAR - EXERCISE 1")
    print("Programming for Data Analytics")
    print("="*80)
    
    # Run exercise parts separately
    print("\n" + "▶"*40)
    print("PART 1: Individual Steps (Separate Arrays)")
    print("▶"*40)
    exercise_1_part_a()
    exercise_1_part_b()
    exercise_1_part_c()
    
    # Run complete sequence
    print("\n" + "▶"*40)
    print("PART 2: Complete Sequence (Single Array)")
    print("▶"*40)
    complete_exercise_sequence()
    
    print("\n" + "="*80)
    print("Exercise 1 completed!")
    print("="*80)


if __name__ == "__main__":
    main()
