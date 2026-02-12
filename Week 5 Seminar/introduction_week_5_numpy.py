# Week 5 Seminar - NumPy Basics
# Programming for Data Analytics
# Date: February 12, 2026

"""
Week 5 Seminar Exercise - NumPy Fundamentals
--------------------------------------------
This file covers fundamental NumPy operations and concepts.

Topics covered:
- NumPy array creation and types
- Loading data from text files (CSV)
- Saving and loading binary files (.npy)
- Array shapes and reshaping
- Computation differences (lists vs arrays)
- Array indexing and slicing
- Advanced indexing techniques
"""

import numpy as np
import time
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def numpy_array_basics():
    """Demonstrate basic NumPy array creation and types."""
    print("\n" + "="*80)
    print("NUMPY ARRAY BASICS")
    print("="*80)
    
    # Creating arrays with mixed types (will convert to common type)
    array = np.array(['a', 1, 2])
    print("\nMixed type array:")
    print(f"array = np.array(['a', 1, 2])")
    print(f"Result: {array}")
    print(f"Data type: {array.dtype}")


def load_from_text_files():
    """Demonstrate loading data from CSV files."""
    print("\n" + "="*80)
    print("LOAD FROM TEXT FILES")
    print("="*80)
    
    # Method 1: np.loadtxt() - requires numeric data
    print("\n1. Using np.loadtxt() with parameters:")
    print("   - skiprows=1 (skip header)")
    print("   - usecols=(0, 1, 6) (select columns)")
    print("   - max_rows=10 (limit rows)")
    print("   - delimiter=',' (CSV format)")
    
    tips_path = os.path.join(SCRIPT_DIR, 'tips.csv')
    tips1 = np.loadtxt(tips_path,
                       skiprows=1,
                       usecols=(0, 1, 6),
                       max_rows=10,
                       delimiter=',')
    print(f"\ntips1 shape: {tips1.shape}")
    print(tips1)
    
    # Method 2: np.genfromtxt() - handles missing data better
    print("\n2. Using np.genfromtxt() with column names:")
    tips2 = np.genfromtxt(tips_path, 
                          delimiter=',', 
                          usecols=[0, 1, 6],
                          max_rows=100,
                          names=True)
    print(f"\ntips2 shape: {tips2.shape}")
    print(f"Column names: {tips2.dtype.names}")
    print(tips2[:5])  # Show first 5 rows


def save_and_load_binary():
    """Demonstrate saving and loading NumPy binary files."""
    print("\n" + "="*80)
    print("SAVE AND LOAD IN BINARY FILES")
    print("="*80)
    
    # Load data first
    tips_path = os.path.join(SCRIPT_DIR, 'tips.csv')
    tips1 = np.loadtxt(tips_path,
                       skiprows=1,
                       usecols=(0, 1, 6),
                       max_rows=10,
                       delimiter=',')
    
    # Save as binary (.npy format)
    print("\nSaving array to 'tips.npy'...")
    tips_npy_path = os.path.join(SCRIPT_DIR, 'tips')
    np.save(tips_npy_path, tips1)
    print("Saved successfully!")
    
    # Load from binary
    print("\nLoading array from 'tips.npy'...")
    tips3 = np.load(tips_npy_path + '.npy')
    print(f"Loaded array shape: {tips3.shape}")
    print(tips3)


def array_shapes():
    """Demonstrate array shapes and dimensions."""
    print("\n" + "="*80)
    print("ARRAY SHAPES")
    print("="*80)
    
    # 1D array
    a = np.array([1, 2, 3])
    print(f"\n1D array: {a}")
    print(f"Shape: {a.shape}")
    
    # 2D array
    b = np.array([[1, 2, 3], [2, 3, 4]])
    print(f"\n2D array:\n{b}")
    print(f"Shape: {b.shape}")
    
    # 3D array
    c = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                  [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])
    print(f"\n3D array shape: {c.shape}")
    print(f"3D array:\n{c}")


def reshape_arrays():
    """Demonstrate array reshaping operations."""
    print("\n" + "="*80)
    print("RESHAPE YOUR ARRAY")
    print("="*80)
    
    c = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                  [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])
    
    print(f"\nOriginal shape: {c.shape}")
    
    # reshape() - returns a view, not a copy
    print("\n1. reshape(2, 2, 2, 3) - returns view:")
    reshaped = c.reshape(2, 2, 2, 3)
    print(f"   New shape: {reshaped.shape}")
    
    # Reshape to 2D
    c = c.reshape(6, 4)
    print(f"\n2. reshape(6, 4):\n{c}")
    
    # ravel() - flatten to 1D
    print(f"\n3. ravel() - flatten to 1D:")
    raveled = c.ravel()
    print(f"   Shape: {raveled.shape}")
    print(f"   Result: {raveled}")
    
    # resize() - in-place modification
    print(f"\n4. resize(2, 12) - modifies in place:")
    c.resize(2, 12)
    print(f"   New shape: {c.shape}")
    print(f"   Result:\n{c}")
    
    # transpose()
    print(f"\n5. transpose() - swap axes:")
    transposed = c.transpose()
    print(f"   Original shape: {c.shape}")
    print(f"   Transposed shape: {transposed.shape}")
    
    # Using .T attribute
    c = np.arange(1, 25).reshape(4, 6)
    print(f"\n6. Using .T attribute:")
    print(f"   Original shape: {c.shape}")
    print(f"   c.T shape: {c.T.shape}")


def computation_differences():
    """Demonstrate computation differences between lists and NumPy arrays."""
    print("\n" + "="*80)
    print("COMPUTATION DIFFERENCES: Lists vs NumPy Arrays")
    print("="*80)
    
    # List concatenation
    ls1 = [1, 2, 3]
    ls2 = [4, 5, 6]
    print(f"\nList addition (concatenation):")
    print(f"ls1 + ls2 = {ls1 + ls2}")
    
    # Array element-wise addition
    a = np.array(ls1)
    b = np.array(ls2)
    print(f"\nNumPy array addition (element-wise):")
    print(f"a + b = {a + b}")
    
    # Speed comparison
    print("\n" + "-"*80)
    print("SPEED COMPARISON (100,000 elements)")
    print("-"*80)
    
    rng = np.random.RandomState(42)
    x = rng.rand(100000)
    y = rng.rand(100000)
    
    # NumPy timing
    start = time.time()
    for _ in range(100):
        result_np = x + y
    numpy_time = time.time() - start
    
    # List comprehension timing
    x_list = x.tolist()
    y_list = y.tolist()
    start = time.time()
    for _ in range(100):
        result_list = [xi + yi for xi, yi in zip(x_list, y_list)]
    list_time = time.time() - start
    
    print(f"\nNumPy array addition: {numpy_time:.6f} seconds")
    print(f"List comprehension: {list_time:.6f} seconds")
    print(f"NumPy is {list_time/numpy_time:.1f}x faster!")


def array_broadcasting():
    """Demonstrate NumPy broadcasting with arrays of different shapes."""
    print("\n" + "="*80)
    print("ARRAY BROADCASTING")
    print("="*80)
    
    a = np.array([1, 2, 3])
    print(f"\nArray a: {a}")
    print(f"Shape: {a.shape}")
    
    c = np.array([[1, 2, 3], [2, 3, 4]])
    print(f"\nArray c:\n{c}")
    print(f"Shape: {c.shape}")
    
    b = np.array([3, 4, 5])
    print(f"\nArray b: {b}")
    print(f"Shape: {b.shape}")
    
    result = a * b
    print(f"\na * b = {result}")
    
    result_c = c * b
    print(f"\nc * b (broadcasting):\n{result_c}")


def create_special_arrays():
    """Demonstrate functions to create special arrays."""
    print("\n" + "="*80)
    print("FUNCTIONS TO CREATE SPECIAL ARRAYS")
    print("="*80)
    
    # zeros array
    zarray = np.zeros([3, 2], dtype=np.int64)
    print(f"\nnp.zeros([3, 2], dtype=np.int64):")
    print(zarray)
    
    # ones array
    oarray = np.ones((2, 3, 4), dtype=np.float64)
    print(f"\nnp.ones((2, 3, 4), dtype=np.float64):")
    print(f"Shape: {oarray.shape}")
    print(oarray)
    
    # empty array (uninitialized)
    earray = np.empty((3, 3))
    print(f"\nnp.empty((3, 3)) - uninitialized values:")
    print(earray)


def array_indexing():
    """Demonstrate array indexing."""
    print("\n" + "="*80)
    print("INDEX OF ARRAY")
    print("="*80)
    
    a = np.arange(1, 25).reshape(2, 3, 4)
    print(f"\n3D array shape {a.shape}:")
    print(a)
    
    print(f"\na[1, 2, 3] = {a[1, 2, 3]}")
    print(f"\na[1, 2] = {a[1, 2]}")
    print(f"\na[1] (entire 2D slice):\n{a[1]}")


def array_slicing():
    """Demonstrate array slicing."""
    print("\n" + "="*80)
    print("SLICE YOUR ARRAY")
    print("="*80)
    
    # 1D slicing
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    print(f"\nOriginal array: {a}")
    print(f"a[1:5] = {a[1:5]}")
    print(f"a[1:6:2] (step=2) = {a[1:6:2]}")
    
    # 3D slicing
    a = np.arange(1, 25).reshape(2, 3, 4)
    print(f"\n3D array shape {a.shape}:")
    print(a)
    
    print(f"\na[0:2, 0:2, 0:2]:")
    print(a[0:2, 0:2, 0:2])
    
    print(f"\na[0:2, 0:2]:")
    print(a[0:2, 0:2])
    
    # Index arrays
    a = np.arange(10)
    i = np.array([1, 1, 4, 7, 5])
    print(f"\na = {a}")
    print(f"i = {i}")
    print(f"a[i] = {a[i]}")
    
    j = np.array([[3, 4], [9, 7]])
    print(f"\nj = \n{j}")
    print(f"a[j] = \n{a[j]}")


def advanced_indexing():
    """Demonstrate advanced indexing techniques."""
    print("\n" + "="*80)
    print("ADVANCED INDEXING")
    print("="*80)
    
    # Fancy indexing
    a = np.array([1, 2, 3, 4, 5, 6])
    print(f"\nOriginal array: {a}")
    print(f"a[[2,4,5]] = {a[[2, 4, 5]]}")
    
    # Boolean masking
    mask = a > 4
    print(f"\nmask = (a > 4) = {mask}")
    print(f"a[mask] = {a[mask]}")
    
    # 2D advanced indexing
    b = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])
    print(f"\n2D array:\n{b}")
    
    # Selecting specific elements: (row 0, col 2), (row 1, col 0), (row 2, col 1)
    print(f"\nb[[0,1,2],[2,0,1]] = {b[[0, 1, 2], [2, 0, 1]]}")
    print("This selects: b[0,2], b[1,0], b[2,1] = [3, 4, 8]")


def main():
    """Main function to run Week 5 NumPy exercises."""
    print("="*80)
    print("WEEK 5 SEMINAR - NUMPY BASICS")
    print("Programming for Data Analytics")
    print("="*80)
    
    # Run all demonstrations
    numpy_array_basics()
    load_from_text_files()
    save_and_load_binary()
    array_shapes()
    reshape_arrays()
    computation_differences()
    array_broadcasting()
    create_special_arrays()
    array_indexing()
    array_slicing()
    advanced_indexing()
    
    print("\n" + "="*80)
    print("Week 5 NumPy exercises completed!")
    print("="*80)


if __name__ == "__main__":
    main()
