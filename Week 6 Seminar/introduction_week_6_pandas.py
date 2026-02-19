"""
Week 6 Seminar: Lecture - Pandas Basics
========================================

This file is converted from Lecture_Week_6_Pandas.ipynb
Covers fundamental Pandas operations including:
- Creating Pandas Series
- Creating DataFrames
- Reading CSV files
- Element-wise operations
- Column and row selection, addition, deletion
- Data processing and exploration
- Visualization with matplotlib and seaborn

Author: Week 6 Seminar Series
Date: February 2026
"""

import pandas as pd
import numpy as np
import os

# Set display options
pd.set_option('display.max_columns', None)

print("="*70)
print("WEEK 6 LECTURE: PANDAS BASICS")
print("="*70)

# =============================================================================
# CREATE PANDAS SERIES
# =============================================================================

print("\n" + "="*70)
print("SECTION 1: CREATE PANDAS SERIES")
print("="*70)

print("\n--- A series can be created using pandas function Series with python list or numpy 1-D array ---")

s1 = pd.Series([1, 2, 3])
s2 = pd.Series(np.array([1, 2, 3, 4, 5]))
print("\nSeries s2:")
print(s2)

print("\n--- Compare Series with ndarray ---")
print("\nNumPy array:")
print(np.array([1, 2, 3, 4, 5]))

print("\n--- An explicit index can be specified by providing the index with a list ---")
s3 = pd.Series([1, 2, 3, 'a', 'b', 'c'], index=['A', 'B', 'C', 'D', 'E', 'A'])
print("\nSeries s3 (with custom index, duplicate 'A'):")
print(s3)

print("\n--- When a dictionary is provided, the key will be used as the index ---")
s4 = pd.Series({'A': 1, 'B': 2, 'C': 3})
print("\nSeries s4 (from dictionary):")
print(s4)

print("\n--- Testing: Each index label needs to be unique? ---")
s5 = pd.Series({'A': 1, 'B': 2, 'A': 3})
print("\nSeries s5 (duplicate key 'A' in dictionary):")
print(s5)
print("Note: In dictionary, duplicate keys get overwritten")

print("\n--- Data can be accessed similar to a Python list with default numeric index ---")
print("\ns4[2]:")
print(s4[2])

print("\ns2[:2]:")
print(s2[:2])

print("\n--- Data can be accessed similar to a dictionary with specified index label ---")
print("\ns3['A'] (how many rows?):")
print(s3['A'])

print("\n--- Retrieve multiple data by providing a list of labels ---")
print("\ns3[['A', 'B']]:")
print(s3[['A', 'B']])

# =============================================================================
# CREATE DATAFRAME
# =============================================================================

print("\n" + "="*70)
print("SECTION 2: CREATE DATAFRAME")
print("="*70)

print("\n--- Create DataFrame from dictionary of arrays/lists/series ---")
print("\nDataFrame from single list:")
d1 = pd.DataFrame([1, 2, 3])
print(d1)

print("\nSeries s1 for comparison:")
print(s1)

print("\nDataFrame from dictionary with mixed types:")
d1 = pd.DataFrame({'A': [1, 2, 3], 'B': [2, 3, "4"]})
print(d1)

print("\n--- Specify index label for rows ---")
d2 = pd.DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4]}, index=['X', 'Y', 'Z'])
print(d2)

print("\nDataFrame with NumPy array and list (mixed data types):")
d3 = pd.DataFrame({
    'A': np.array([1, 2, 3]),
    'B': [2, 3, 4]
}, index=['X', 'Y', 'Z'])
print(d3)

print("\nDataFrame from tuple and Series:")
d4 = pd.DataFrame({'A': (1, 2, 3), 'B': s1})
print(d4)

print("\n--- Items in dictionary must have same length unless all are series ---")
try:
    d5 = pd.DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4, 5]})
except ValueError as e:
    print(f"\nError creating d5: {e}")

print("\nDataFrame from series with different lengths:")
d6 = pd.DataFrame({'A': s1, 'B': s2})
print(d6)

print("\nSeries s2 for reference:")
print(s2)

print("\n--- When series have different length, Python matches their index and appends NaN ---")
d7 = pd.DataFrame({'A': s1, 'B': s2})
print("\nDataFrame d7 (using default numeric index):")
print(d7)

print("\nDataFrame with custom index matching:")
data = {
    'A': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'B': pd.Series([1, 2, 3, 4], index=['b', 'c', 'd', 'e'])
}
df8 = pd.DataFrame(data)
print(df8)

print("\n--- DataFrame from a single list or list of lists ---")
d9 = pd.DataFrame([1, 2, 3, 4, 5, 6])
print("\nDataFrame d9 (from single list):")
print(d9)

s9 = pd.Series([1, 2, 3, 4, 5, 6])
print("\nSeries s9 for comparison:")
print(s9)

print("\nDataFrame from list of lists:")
d10 = pd.DataFrame([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
print(d10)

print("\n--- Specify labels for columns and index ---")
d12 = pd.DataFrame([[1, 2, 3], [12, 3, 4], [3, 4, 5]],
                   columns=['A', 'B', 'C'],
                   index=['X', 'Y', 'Z'])
print(d12)

print("\n--- DataFrame from list of dictionaries ---")
d13 = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 5, 'b': 10}])
print("\nDataFrame d13:")
print(d13)

d14 = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 5, 'b': 10}], index=['A', 'B'])
print("\nDataFrame d14 (with index):")
print(d14)

print("\nWhat happens if you provide Columns parameter?")
d14_custom = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 5, 'b': 10}], 
                          columns=['A', 'B'], index=['A', 'B'])
print(d14_custom)
print("Note: Column labels don't match dictionary keys, so all NaN")

print("\n--- Items in list can have different length ---")
df_test = pd.DataFrame([{'a': 1, 'b': 2}, {'b': 5, 'c': 10, 'd': 15}])
print("\nDataFrame df_test:")
print(df_test)

try:
    df_test_list = pd.DataFrame([[1, 2], [2, 3], [3, 4, 5]])
except ValueError as e:
    print(f"\nError with list of lists with different lengths: {e}")

print("\n--- When column labels are specified, Python matches keys with labels ---")
df_test = pd.DataFrame([{
    'a': 1,
    'b': 2
}, {
    'b': 5,
    'c': 10,
    'd': 15
}], columns=['b', 'd', 'e'])
print(df_test)
print("Note: Values with non-matching keys are ignored")

df_test = pd.DataFrame({
    'A': np.array([1, 2, 3]),
    'B': [2, 3, 4]
}, index=['X', 'Y', 'Z'], columns=['aa', 'bb'])
print("\nDataFrame with columns that don't match keys:")
print(df_test)
print("Note: All NaN because column names don't match dictionary keys")

# =============================================================================
# CREATE DATAFRAME FROM FILES
# =============================================================================

print("\n" + "="*70)
print("SECTION 3: CREATE DATAFRAME FROM FILES")
print("="*70)

print("\n--- Pandas can read from csv, Excel, JSON, SQL, etc. Focus: CSV files ---")

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, 'data source')
output_dir = os.path.join(script_dir, 'visualizations')
os.makedirs(output_dir, exist_ok=True)

# Check if tips.csv exists
tips_csv_path = os.path.join(data_dir, 'tips.csv')
if not os.path.exists(tips_csv_path):
    print(f"\nWarning: tips.csv not found in {data_dir}. Skipping CSV examples.")
    tips_csv_path = None

if tips_csv_path:
    print("\n--- Use read_csv() function. Filename is the only required argument ---")
    df_tips = pd.read_csv(tips_csv_path)
    print("\nDataFrame df_tips:")
    print(df_tips.head())
    
    print("\nReading CSV without header:")
    df_tips_no_header = pd.read_csv(tips_csv_path, header=None)
    print(df_tips_no_header.head())
    
    print("\nReading CSV with custom column names:")
    df_tips_custom = pd.read_csv(tips_csv_path, header=None, names=[1, 2])
    print(df_tips_custom.head())
    
    print("\nReading CSV with index_col=0:")
    df_tips1 = pd.read_csv(tips_csv_path, index_col=0)
    print(df_tips1.head())
    
    print("\nReading CSV with specific column as index:")
    df_tips_idx = pd.read_csv(tips_csv_path, index_col='tip')
    print(df_tips_idx.head())
    
    print("\nReading specific columns (usecols):")
    df_tips_cols = pd.read_csv(tips_csv_path, usecols=[1, 2, 3])
    print(df_tips_cols.head())
    
    print("\nSkipping rows and limiting rows:")
    df_tips_skip = pd.read_csv(tips_csv_path, skiprows=3, nrows=10)
    print(df_tips_skip)

# =============================================================================
# CONVERSION BETWEEN DATAFRAME AND NDARRAY
# =============================================================================

print("\n" + "="*70)
print("SECTION 4: CONVERSION BETWEEN DATAFRAME AND NDARRAY")
print("="*70)

array = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 7]])
df_array = pd.DataFrame(data=array)
print("\nDataFrame from NumPy array:")
print(df_array)

print("\nConvert DataFrame to NumPy array (.to_numpy()):")
print(df_array.to_numpy())

print("\nUsing .values attribute:")
print(df_array.values)

if tips_csv_path:
    print("\nWhat would df_tips look like after converting to ndarray?")
    print(df_tips.head().to_numpy())

# =============================================================================
# ELEMENT-WISE OPERATIONS
# =============================================================================

print("\n" + "="*70)
print("SECTION 5: ELEMENT-WISE OPERATIONS")
print("="*70)

print("\n--- Pandas basic operations are element-wise ---")
if tips_csv_path:
    print("\ndf_tips * 2:")
    print((df_tips * 2).head())

# =============================================================================
# COLUMN SELECTION, ADDITION AND DELETION
# =============================================================================

print("\n" + "="*70)
print("SECTION 6: COLUMN SELECTION, ADDITION AND DELETION")
print("="*70)

if tips_csv_path:
    df_tips = pd.read_csv(tips_csv_path)
    
    print("\n--- Column selection using column label ---")
    print("\ndf_tips['tip'] (returns Series):")
    print(df_tips['tip'].head())
    
    print("\ndf_tips.tip (dot notation):")
    print(df_tips.tip.head())
    print("Note: Bracket notation is preferred over dot notation")
    
    print("\ndf_tips[['tip']] (returns DataFrame):")
    print(df_tips[['tip']].head())
    
    print("\n--- Add new column with label ---")
    df_tips['f'] = pd.Series([10, 10])
    print("\nDataFrame after adding column 'f':")
    print(df_tips.head())
    
    print("\n--- New column from calculation ---")
    df_tips['total'] = df_tips['total_bill'] + df_tips['tip']
    print("\nDataFrame after adding 'total' column:")
    print(df_tips.head())
    
    print("\nUpdate 'total' column:")
    df_tips['total'] = df_tips['tip'] + 100
    print(df_tips.head())
    
    print("\n--- Delete column with del ---")
    del df_tips['f']
    print("\nDataFrame after deleting column 'f':")
    print(df_tips.head())
    print("Note: Can also use df.drop(['f'], axis=1) which returns a copy")

# =============================================================================
# ROW SELECTION
# =============================================================================

print("\n" + "="*70)
print("SECTION 7: ROW SELECTION")
print("="*70)

if tips_csv_path:
    print("\n--- Row selection by passing row labels to loc[] ---")
    print("\ndf_tips.loc[1] (returns Series):")
    print(df_tips.loc[1])
    
    print("\n--- Multiple rows can be selected ---")
    print("\ndf_tips.loc[[1,2,3]] (returns DataFrame):")
    print(df_tips.loc[[1, 2, 3]])
    
    print("\ndf_tips.loc[1:3] (slice, both start and end included):")
    print(df_tips.loc[1:3])
    
    print("\n--- Column labels can filter results ---")
    print("\ndf_tips.loc[[1, 2, 3], 'smoker']:")
    print(df_tips.loc[[1, 2, 3], 'smoker'])
    
    print("\n--- Select rows with Boolean expression ---")
    print("\ndf_tips['total_bill'] > 10 (element-wise operation):")
    print((df_tips['total_bill'] > 10).head())
    
    print("\ndf_tips.loc[df_tips['total_bill'] > 10]:")
    print(df_tips.loc[df_tips['total_bill'] > 10].head())
    
    print("\ndf_tips.loc[df_tips['total_bill'] > 10, ['smoker']]:")
    print(df_tips.loc[df_tips['total_bill'] > 10, ['smoker']].head())
    
    print("\nAlternative (less safe with potential SettingWithCopyWarning):")
    print("df_tips[df_tips['tip'] > 2]")
    print(df_tips[df_tips['tip'] > 2].head())
    
    print("\n--- Select rows by integer position with iloc[] ---")
    print("\ndf_tips.iloc[1]:")
    print(df_tips.iloc[1])
    
    print("\ndf_tips.loc[1] (for comparison):")
    print(df_tips.loc[1])
    
    print("\ndf_tips.iloc[1:3] (end not included):")
    print(df_tips.iloc[1:3])
    
    print("\ndf_tips.loc[1:3] (end included):")
    print(df_tips.loc[1:3])
    
    print("\nDataFrame with custom index:")
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]
    }, index=['a', 'b', 'c', 'd'])
    print(df)
    
    print("\ndf.iloc[1]:")
    print(df.iloc[1])

# =============================================================================
# ADD AND DELETE ROWS
# =============================================================================

print("\n" + "="*70)
print("SECTION 8: ADD AND DELETE ROWS")
print("="*70)

if tips_csv_path:
    print("\n--- Add new rows with pd.concat() (append removed in pandas 2.0) ---")
    print("\npd.concat([df_tips, pd.DataFrame([99, 99])]):")
    print("Note: Original dataframe not updated")
    
    df_tips_concat = pd.concat([df_tips, pd.DataFrame([99, 99])])
    print("\nDataFrame after concat (reassigned):")
    print(df_tips_concat.tail())
    
    print("\n--- Row deletion with drop() method ---")
    print("\ndf_tips.drop([4]):")
    dropped = df_tips.drop([4])
    print(dropped.head())
    print("Note: Original dataframe not updated")
    
    print("\ndf_tips.drop([1, 2]):")
    print(df_tips.drop([1, 2]).head())
    
    df_tips1 = pd.read_csv(tips_csv_path)
    print("\ndf_drop = df_tips1.drop(range(3)):")
    df_drop = df_tips1.drop(range(3))
    print(df_drop.head())
    
    print("\ndf_tips1 = df_tips1.drop([2]):")
    df_tips1 = df_tips1.drop([2])
    print(df_tips1.head())
    
    print("\ndf_tips1.drop([5], inplace=True) - existing dataframe updated:")
    df_tips1.drop([5], inplace=True)
    print(df_tips1.head())

# =============================================================================
# IMPORTANT DATAFRAME ATTRIBUTES
# =============================================================================

print("\n" + "="*70)
print("SECTION 9: IMPORTANT DATAFRAME ATTRIBUTES")
print("="*70)

if tips_csv_path:
    print("\n--- .index returns a list of row indexes ---")
    print("\ndf_tips.index:")
    print(df_tips.index)
    
    print("\ndf_tips.loc[df_tips['total_bill'] > 20].index:")
    print(df_tips.loc[df_tips['total_bill'] > 20].index)
    
    print("\n--- Very handy to remove rows based on condition ---")
    df_tips3 = df_tips.drop(df_tips.loc[df_tips['total_bill'] > 20].index)
    print("\ndf_tips3 (removed rows where total_bill > 20):")
    print(df_tips3.head())

# =============================================================================
# SCALAR OPERATIONS
# =============================================================================

print("\n" + "="*70)
print("SECTION 10: SCALAR OPERATIONS")
print("="*70)

if tips_csv_path:
    print("\n--- Basic arithmetic and Boolean operations with scalar are element-wise ---")
    print("\ndf_tips * 2 (broadcasting):")
    print((df_tips * 2).head())
    
    print("\ndf_tips['tip'] * 2:")
    print((df_tips['tip'] * 2).head())
    
    print("\n--- Operations with list or Series performed based on matching labels ---")
    d10 = pd.DataFrame([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
    print("\nDataFrame d10:")
    print(d10)
    
    print("\nd10 - [1, 2, 3] (default: compare by column):")
    print(d10 - [1, 2, 3])
    
    print("\nd10 > [3, 3, 3]:")
    print(d10 > [3, 3, 3])
    
    print("\nd10 - pd.Series([1, 2]) (NaN for non-matching columns):")
    print(d10 - pd.Series([1, 2]))
    
    print("\n--- For operations by row, specify axis='index' ---")
    print("\nd10.sub(pd.Series([1, 2, 3]), axis='index'):")
    print(d10.sub(pd.Series([1, 2, 3]), axis='index'))
    
    print("\nd10.sub(pd.Series([1, 2, 3], index=[1, 2, 3]), axis='index'):")
    print(d10.sub(pd.Series([1, 2, 3], index=[1, 2, 3]), axis='index'))
    print("Note: NaN for non-matching rows")
    
    print("\nd10.mul(pd.Series([1, 2, 3], index=[1, 2, 3]), axis='index'):")
    print(d10.mul(pd.Series([1, 2, 3], index=[1, 2, 3]), axis='index'))

# =============================================================================
# DATA PROCESSING - EXPLORE DATASET
# =============================================================================

print("\n" + "="*70)
print("SECTION 11: DATA PROCESSING - EXPLORE DATASET")
print("="*70)

if tips_csv_path:
    df_tips = pd.read_csv(tips_csv_path)
    
    print("\ndf_tips.shape:")
    print(df_tips.shape)
    
    print("\ndf_tips.size:")
    print(df_tips.size)
    
    print("\ndf_tips.info():")
    print(df_tips.info())
    
    print("\ndf_tips.head(3):")
    print(df_tips.head(3))
    
    print("\ndf_tips.tail(3):")
    print(df_tips.tail(3))
    
    print("\ndf_tips.describe(include='all'):")
    print(df_tips.describe(include='all'))

# =============================================================================
# EXPLORATION VIA VISUALIZATION
# =============================================================================

print("\n" + "="*70)
print("SECTION 12: EXPLORATION VIA VISUALIZATION")
print("="*70)

if tips_csv_path:
    try:
        import matplotlib
        import matplotlib.pyplot as plt
        
        print("\nGenerating visualizations...")
        
        # Histogram
        df_tips.hist()
        plt.suptitle('All Columns Histogram')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'tips_histogram_all.png'))
        plt.close()
        print("Saved: tips_histogram_all.png")
        
        # Single column histogram
        df_tips.hist('total_bill')
        plt.title('Total Bill Histogram')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'tips_histogram_total_bill.png'))
        plt.close()
        print("Saved: tips_histogram_total_bill.png")
        
        # Histogram by category
        df_tips.hist('total_bill', by='sex')
        plt.suptitle('Total Bill by Sex')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'tips_histogram_by_sex.png'))
        plt.close()
        print("Saved: tips_histogram_by_sex.png")
        
        print("\n--- Using Seaborn for advanced visualizations ---")
        try:
            import seaborn as sns
            
            # Category plot
            sns.catplot(x='sex', kind='count', hue='day', data=df_tips)
            plt.title('Count by Sex and Day')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'tips_catplot.png'))
            plt.close()
            print("Saved: tips_catplot.png")
            
            # Distribution plot
            sns.displot(df_tips['total_bill'])
            plt.title('Total Bill Distribution')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'tips_displot.png'))
            plt.close()
            print("Saved: tips_displot.png")
            
            # Pairplot
            sns.pairplot(df_tips, hue='sex')
            plt.suptitle('Pairplot by Sex', y=1.02)
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'tips_pairplot.png'))
            plt.close()
            print("Saved: tips_pairplot.png")
            
            # Box plot
            sns.catplot(x='day', y='tip', kind='box', data=df_tips)
            plt.title('Tip by Day (Box Plot)')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'tips_boxplot.png'))
            plt.close()
            print("Saved: tips_boxplot.png")
            
            print("\nAll Seaborn visualizations completed!")
            
        except ImportError:
            print("\nSeaborn not available. Install with: pip install seaborn")
    
    except ImportError:
        print("\nMatplotlib not available. Install with: pip install matplotlib")

print("\n" + "="*70)
print("LECTURE COMPLETED!")
print("="*70)
print("\nYou've covered comprehensive Pandas basics from the lecture material.")
print("Practice these concepts with different datasets to master Pandas!")

if __name__ == "__main__":
    pass
