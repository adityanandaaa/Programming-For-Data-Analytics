"""
Week 6 Seminar: Case Study 2 - Customer Churn Analysis
=======================================================

Dataset: Telco Customer Churn
Source: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Task:
Import the customer_churn.csv dataset and conduct comprehensive exploratory data analysis (EDA)
to gain deep understanding of the dataset, identify issues, and extract insights.

HINT: There is one column that needs careful audit!

Author: Week 6 Seminar Series
Date: February 2026
"""

# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np   # For numerical operations
import matplotlib.pyplot as plt  # For creating visualizations
import seaborn as sns  # For statistical data visualization
import os  # For file path operations
import warnings  # For suppressing warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Set visualization style for better-looking plots
sns.set_style('whitegrid')  # White background with grid lines
plt.rcParams['figure.figsize'] = (14, 6)  # Default figure size
plt.rcParams['font.size'] = 10  # Default font size

# Get the absolute path of the current script file
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the 'data source' folder
data_dir = os.path.join(script_dir, 'data source')

print("="*80)
print("CASE STUDY 2: CUSTOMER CHURN ANALYSIS")
print("EXPLORATORY DATA ANALYSIS (EDA)")
print("="*80)

# =============================================================================
# STEP 1: Import Dataset
# =============================================================================

print("\n" + "-"*80)
print("STEP 1: IMPORT DATASET")
print("-"*80)

# Construct the full file path to customer_churn.csv
csv_file_path = os.path.join(data_dir, 'customer_churn.csv')
print(f"\nFile path: {csv_file_path}")

# Read CSV file into a DataFrame
df_churn = pd.read_csv(csv_file_path)

print("\nDataset loaded successfully!")
print(f"Shape: {df_churn.shape[0]:,} rows × {df_churn.shape[1]} columns")

# Display first few rows
print("\nFirst 5 rows:")
print(df_churn.head())

# Display last few rows
print("\nLast 5 rows:")
print(df_churn.tail())

# =============================================================================
# STEP 2: Initial Data Inspection
# =============================================================================

print("\n" + "-"*80)
print("STEP 2: INITIAL DATA INSPECTION")
print("-"*80)

# Display concise summary
print("\nDataFrame Info:")
print(df_churn.info())

# Display column names
print("\nColumn Names:")
for i, col in enumerate(df_churn.columns, 1):
    print(f"  {i:2d}. {col}")

# Display data types
print("\nData Types:")
print(df_churn.dtypes)

# Check for duplicate rows
duplicates = df_churn.duplicated().sum()
print(f"\nDuplicate rows: {duplicates}")

# Check for duplicate customer IDs
duplicate_ids = df_churn['customerID'].duplicated().sum()
print(f"Duplicate customer IDs: {duplicate_ids}")

# =============================================================================
# STEP 3: Missing Values Analysis
# =============================================================================

print("\n" + "-"*80)
print("STEP 3: MISSING VALUES ANALYSIS")
print("-"*80)

# Count missing values per column
missing_counts = df_churn.isnull().sum()
missing_percentages = (missing_counts / len(df_churn)) * 100

# Create summary DataFrame
missing_summary = pd.DataFrame({
    'Missing_Count': missing_counts,
    'Missing_Percentage': missing_percentages
})
missing_summary = missing_summary[missing_summary['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)

print("\nMissing Values Summary:")
if len(missing_summary) > 0:
    print(missing_summary)
else:
    print("  ✓ No missing values detected!")

# =============================================================================
# STEP 4: Data Type Analysis and AUDIT (THE HINT!)
# =============================================================================

print("\n" + "-"*80)
print("STEP 4: DATA TYPE AUDIT - IDENTIFYING ISSUES")
print("-"*80)

print("\n🔍 CAREFUL AUDIT: Checking data types and values...")

# Separate columns by expected type
print("\nExpected Column Types:")
print("\nCustomer ID:")
print(f"  • customerID: {df_churn['customerID'].dtype}")

print("\nDemographic (should be categorical/numeric):")
demographic_cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents']
for col in demographic_cols:
    print(f"  • {col}: {df_churn[col].dtype}")

print("\nAccount Information:")
account_cols = ['tenure', 'Contract', 'PaperlessBilling', 'PaymentMethod']
for col in account_cols:
    print(f"  • {col}: {df_churn[col].dtype}")

print("\nServices:")
service_cols = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
                'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
for col in service_cols:
    print(f"  • {col}: {df_churn[col].dtype}")

print("\nCharges (should be numeric):")
charge_cols = ['MonthlyCharges', 'TotalCharges']
for col in charge_cols:
    print(f"  • {col}: {df_churn[col].dtype} ⚠️")

print("\nTarget Variable:")
print(f"  • Churn: {df_churn['Churn'].dtype}")

# THE CRITICAL ISSUE: TotalCharges is object, not numeric!
print("\n" + "!"*80)
print("🚨 ISSUE IDENTIFIED: TotalCharges is 'object' type, should be numeric!")
print("!"*80)

# Investigate TotalCharges
print("\nInvestigating TotalCharges column:")
print(f"  Data type: {df_churn['TotalCharges'].dtype}")
print(f"  Unique values: {df_churn['TotalCharges'].nunique()}")
print(f"  Sample values: {df_churn['TotalCharges'].head(10).tolist()}")

# Check for non-numeric values
print("\n  Checking for non-numeric values...")
# Try to convert to numeric, errors='coerce' turns non-numeric to NaN
totalcharges_numeric = pd.to_numeric(df_churn['TotalCharges'], errors='coerce')
non_numeric_mask = totalcharges_numeric.isnull() & df_churn['TotalCharges'].notna()
non_numeric_count = non_numeric_mask.sum()

print(f"  Non-numeric values found: {non_numeric_count}")

if non_numeric_count > 0:
    print("\n  Sample of problematic records:")
    problematic_records = df_churn[non_numeric_mask].head(10)
    print(problematic_records[['customerID', 'tenure', 'MonthlyCharges', 'TotalCharges']])
    
    # What are the actual values?
    unique_bad_values = df_churn.loc[non_numeric_mask, 'TotalCharges'].unique()
    print(f"\n  Unique non-numeric values in TotalCharges: {unique_bad_values}")
    
    # Check if they're empty strings or spaces
    for val in unique_bad_values[:5]:  # Check first 5
        print(f"    '{val}' (length: {len(str(val))}, type: {type(val)})")

# =============================================================================
# STEP 5: Fix Data Quality Issues
# =============================================================================

print("\n" + "-"*80)
print("STEP 5: FIX DATA QUALITY ISSUES")
print("-"*80)

print("\nCleaning TotalCharges column...")

# Create a copy for cleaning
df_clean = df_churn.copy()

# Convert TotalCharges to numeric, coercing errors to NaN
df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'], errors='coerce')

print(f"  ✓ Converted TotalCharges to numeric type")
print(f"  New data type: {df_clean['TotalCharges'].dtype}")

# Check for NaN values created by conversion
totalcharges_nan = df_clean['TotalCharges'].isnull().sum()
print(f"  NaN values after conversion: {totalcharges_nan}")

# Analyze records with missing TotalCharges
if totalcharges_nan > 0:
    print("\n  Analyzing records with missing TotalCharges:")
    missing_tc = df_clean[df_clean['TotalCharges'].isnull()]
    print(f"    Number of records: {len(missing_tc)}")
    print(f"    Percentage: {(len(missing_tc) / len(df_clean) * 100):.2f}%")
    
    # Check tenure distribution for these records
    print(f"\n    Tenure statistics for missing TotalCharges:")
    print(missing_tc['tenure'].describe())
    print(f"\n    Most common tenure: {missing_tc['tenure'].mode().values}")
    
    # These are likely new customers (tenure = 0 or very low)
    # TotalCharges should be close to MonthlyCharges
    print(f"\n    Sample of missing TotalCharges records:")
    print(missing_tc[['customerID', 'tenure', 'MonthlyCharges', 'TotalCharges']].head(10))
    
    # Strategy: For tenure 0-1, use MonthlyCharges as TotalCharges
    print("\n  Imputation strategy:")
    print("    For customers with very low tenure, TotalCharges ≈ MonthlyCharges")
    
    # Fill missing TotalCharges with MonthlyCharges for low tenure customers
    mask_missing_tc = df_clean['TotalCharges'].isnull()
    df_clean.loc[mask_missing_tc, 'TotalCharges'] = df_clean.loc[mask_missing_tc, 'MonthlyCharges']
    
    print(f"  ✓ Imputed {totalcharges_nan} missing TotalCharges values")
    print(f"  Remaining NaN in TotalCharges: {df_clean['TotalCharges'].isnull().sum()}")

print("\nData cleaning completed!")
print(f"Final dataset shape: {df_clean.shape[0]:,} rows × {df_clean.shape[1]} columns")

# =============================================================================
# STEP 6: Statistical Summary
# =============================================================================

print("\n" + "-"*80)
print("STEP 6: STATISTICAL SUMMARY")
print("-"*80)

# Identify numeric and categorical columns
numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df_clean.select_dtypes(include=['object']).columns.tolist()

print(f"\nNumeric columns ({len(numeric_cols)}): {numeric_cols}")
print(f"\nCategorical columns ({len(categorical_cols)}): {categorical_cols}")

# Statistical summary for numeric columns
print("\nDescriptive Statistics - Numeric Columns:")
print(df_clean[numeric_cols].describe())

# Categorical columns value counts
print("\nCategorical Columns - Unique Values:")
for col in categorical_cols:
    unique_count = df_clean[col].nunique()
    print(f"  • {col}: {unique_count} unique values")

# =============================================================================
# STEP 7: Target Variable Analysis - Churn
# =============================================================================

print("\n" + "-"*80)
print("STEP 7: TARGET VARIABLE ANALYSIS - CHURN")
print("-"*80)

# Churn distribution
churn_counts = df_clean['Churn'].value_counts()
churn_percentages = df_clean['Churn'].value_counts(normalize=True) * 100

print("\nChurn Distribution:")
print(churn_counts)
print("\nChurn Percentages:")
print(churn_percentages)

churn_rate = (df_clean['Churn'] == 'Yes').sum() / len(df_clean) * 100
print(f"\n📊 Overall Churn Rate: {churn_rate:.2f}%")

# Visualize churn distribution
plt.figure(figsize=(10, 6))
colors = ['#2ecc71', '#e74c3c']  # Green for No, Red for Yes
churn_counts.plot(kind='bar', color=colors, alpha=0.7, edgecolor='black')
plt.title('Customer Churn Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Churn Status', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.xticks(rotation=0)
for i, v in enumerate(churn_counts):
    plt.text(i, v + 100, f'{v:,}\n({churn_percentages.iloc[i]:.1f}%)', 
             ha='center', va='bottom', fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('exercise_cs2_churn_distribution.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: exercise_cs2_churn_distribution.png")
plt.close()

# =============================================================================
# STEP 8: Demographic Analysis
# =============================================================================

print("\n" + "-"*80)
print("STEP 8: DEMOGRAPHIC ANALYSIS")
print("-"*80)

demographic_cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents']

print("\nDemographic Distributions:")
for col in demographic_cols:
    print(f"\n{col}:")
    counts = df_clean[col].value_counts()
    percentages = df_clean[col].value_counts(normalize=True) * 100
    for val, count in counts.items():
        pct = percentages[val]
        print(f"  {val}: {count:,} ({pct:.2f}%)")

# Churn rate by demographics
print("\nChurn Rate by Demographics:")
for col in demographic_cols:
    print(f"\n{col}:")
    churn_by_demo = df_clean.groupby(col)['Churn'].apply(lambda x: (x == 'Yes').sum() / len(x) * 100)
    for val, rate in churn_by_demo.items():
        print(f"  {val}: {rate:.2f}%")

# Visualize demographics vs churn
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for idx, col in enumerate(demographic_cols):
    # Create cross-tabulation
    ct = pd.crosstab(df_clean[col], df_clean['Churn'], normalize='index') * 100
    ct.plot(kind='bar', ax=axes[idx], color=['#2ecc71', '#e74c3c'], alpha=0.7)
    axes[idx].set_title(f'Churn Rate by {col}', fontsize=12, fontweight='bold')
    axes[idx].set_xlabel(col, fontsize=10)
    axes[idx].set_ylabel('Percentage (%)', fontsize=10)
    axes[idx].legend(['No Churn', 'Churn'], loc='upper right')
    axes[idx].tick_params(axis='x', rotation=45)
    axes[idx].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('exercise_cs2_demographics_churn.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: exercise_cs2_demographics_churn.png")
plt.close()

# =============================================================================
# STEP 9: Service Usage Analysis
# =============================================================================

print("\n" + "-"*80)
print("STEP 9: SERVICE USAGE ANALYSIS")
print("-"*80)

service_cols = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
                'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

print("\nService Subscription Rates:")
for col in service_cols:
    print(f"\n{col}:")
    counts = df_clean[col].value_counts()
    for val, count in counts.items():
        pct = (count / len(df_clean)) * 100
        print(f"  {val}: {count:,} ({pct:.2f}%)")

# Churn rate by service
print("\nChurn Rate by Service:")
for col in service_cols:
    print(f"\n{col}:")
    churn_by_service = df_clean.groupby(col)['Churn'].apply(lambda x: (x == 'Yes').sum() / len(x) * 100)
    churn_by_service_sorted = churn_by_service.sort_values(ascending=False)
    for val, rate in churn_by_service_sorted.items():
        count = (df_clean[col] == val).sum()
        print(f"  {val}: {rate:.2f}% ({count:,} customers)")

# =============================================================================
# STEP 10: Contract and Payment Analysis
# =============================================================================

print("\n" + "-"*80)
print("STEP 10: CONTRACT AND PAYMENT ANALYSIS")
print("-"*80)

# Contract type analysis
print("\nContract Type Distribution:")
contract_counts = df_clean['Contract'].value_counts()
for val, count in contract_counts.items():
    pct = (count / len(df_clean)) * 100
    print(f"  {val}: {count:,} ({pct:.2f}%)")

print("\nChurn Rate by Contract Type:")
churn_by_contract = df_clean.groupby('Contract')['Churn'].apply(lambda x: (x == 'Yes').sum() / len(x) * 100)
for val, rate in churn_by_contract.sort_values(ascending=False).items():
    print(f"  {val}: {rate:.2f}%")

# Payment method analysis
print("\nPayment Method Distribution:")
payment_counts = df_clean['PaymentMethod'].value_counts()
for val, count in payment_counts.items():
    pct = (count / len(df_clean)) * 100
    print(f"  {val}: {count:,} ({pct:.2f}%)")

print("\nChurn Rate by Payment Method:")
churn_by_payment = df_clean.groupby('PaymentMethod')['Churn'].apply(lambda x: (x == 'Yes').sum() / len(x) * 100)
for val, rate in churn_by_payment.sort_values(ascending=False).items():
    print(f"  {val}: {rate:.2f}%")

# Visualize contract and payment
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Contract churn
ct_contract = pd.crosstab(df_clean['Contract'], df_clean['Churn'], normalize='index') * 100
ct_contract.plot(kind='bar', ax=axes[0], color=['#2ecc71', '#e74c3c'], alpha=0.7)
axes[0].set_title('Churn Rate by Contract Type', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Contract Type', fontsize=10)
axes[0].set_ylabel('Percentage (%)', fontsize=10)
axes[0].legend(['No Churn', 'Churn'])
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(axis='y', alpha=0.3)

# Payment method churn
ct_payment = pd.crosstab(df_clean['PaymentMethod'], df_clean['Churn'], normalize='index') * 100
ct_payment.plot(kind='bar', ax=axes[1], color=['#2ecc71', '#e74c3c'], alpha=0.7)
axes[1].set_title('Churn Rate by Payment Method', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Payment Method', fontsize=10)
axes[1].set_ylabel('Percentage (%)', fontsize=10)
axes[1].legend(['No Churn', 'Churn'])
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('exercise_cs2_contract_payment_churn.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: exercise_cs2_contract_payment_churn.png")
plt.close()

# =============================================================================
# STEP 11: Tenure Analysis
# =============================================================================

print("\n" + "-"*80)
print("STEP 11: TENURE ANALYSIS")
print("-"*80)

print("\nTenure Statistics:")
print(df_clean['tenure'].describe())

print("\nTenure by Churn Status:")
for churn_status in ['No', 'Yes']:
    tenure_stats = df_clean[df_clean['Churn'] == churn_status]['tenure']
    print(f"\n{churn_status} Churn:")
    print(f"  Mean tenure: {tenure_stats.mean():.2f} months")
    print(f"  Median tenure: {tenure_stats.median():.2f} months")
    print(f"  Std dev: {tenure_stats.std():.2f} months")

# Visualize tenure distribution
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Histogram
df_clean[df_clean['Churn'] == 'No']['tenure'].hist(ax=axes[0], bins=30, alpha=0.6, 
                                                     color='green', label='No Churn', edgecolor='black')
df_clean[df_clean['Churn'] == 'Yes']['tenure'].hist(ax=axes[0], bins=30, alpha=0.6, 
                                                      color='red', label='Churn', edgecolor='black')
axes[0].set_title('Tenure Distribution by Churn Status', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Tenure (months)', fontsize=10)
axes[0].set_ylabel('Frequency', fontsize=10)
axes[0].legend()
axes[0].grid(axis='y', alpha=0.3)

# Box plot
df_clean.boxplot(column='tenure', by='Churn', ax=axes[1], patch_artist=True)
axes[1].set_title('Tenure by Churn Status', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Churn Status', fontsize=10)
axes[1].set_ylabel('Tenure (months)', fontsize=10)
axes[1].get_figure().suptitle('')
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('exercise_cs2_tenure_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: exercise_cs2_tenure_analysis.png")
plt.close()

# =============================================================================
# STEP 12: Charges Analysis
# =============================================================================

print("\n" + "-"*80)
print("STEP 12: CHARGES ANALYSIS")
print("-"*80)

print("\nMonthly Charges Statistics:")
print(df_clean['MonthlyCharges'].describe())

print("\nTotal Charges Statistics:")
print(df_clean['TotalCharges'].describe())

print("\nCharges by Churn Status:")
for churn_status in ['No', 'Yes']:
    subset = df_clean[df_clean['Churn'] == churn_status]
    print(f"\n{churn_status} Churn:")
    print(f"  Mean Monthly Charges: ${subset['MonthlyCharges'].mean():.2f}")
    print(f"  Mean Total Charges: ${subset['TotalCharges'].mean():.2f}")

# Visualize charges distribution
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# Monthly charges histogram
df_clean[df_clean['Churn'] == 'No']['MonthlyCharges'].hist(ax=axes[0, 0], bins=30, 
                                                             alpha=0.6, color='green', 
                                                             label='No Churn', edgecolor='black')
df_clean[df_clean['Churn'] == 'Yes']['MonthlyCharges'].hist(ax=axes[0, 0], bins=30, 
                                                              alpha=0.6, color='red', 
                                                              label='Churn', edgecolor='black')
axes[0, 0].set_title('Monthly Charges Distribution', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Monthly Charges ($)', fontsize=10)
axes[0, 0].set_ylabel('Frequency', fontsize=10)
axes[0, 0].legend()
axes[0, 0].grid(axis='y', alpha=0.3)

# Monthly charges box plot
df_clean.boxplot(column='MonthlyCharges', by='Churn', ax=axes[0, 1], patch_artist=True)
axes[0, 1].set_title('Monthly Charges by Churn', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Churn Status', fontsize=10)
axes[0, 1].set_ylabel('Monthly Charges ($)', fontsize=10)
axes[0, 1].get_figure().suptitle('')
axes[0, 1].grid(axis='y', alpha=0.3)

# Total charges histogram
df_clean[df_clean['Churn'] == 'No']['TotalCharges'].hist(ax=axes[1, 0], bins=30, 
                                                           alpha=0.6, color='green', 
                                                           label='No Churn', edgecolor='black')
df_clean[df_clean['Churn'] == 'Yes']['TotalCharges'].hist(ax=axes[1, 0], bins=30, 
                                                            alpha=0.6, color='red', 
                                                            label='Churn', edgecolor='black')
axes[1, 0].set_title('Total Charges Distribution', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Total Charges ($)', fontsize=10)
axes[1, 0].set_ylabel('Frequency', fontsize=10)
axes[1, 0].legend()
axes[1, 0].grid(axis='y', alpha=0.3)

# Total charges box plot
df_clean.boxplot(column='TotalCharges', by='Churn', ax=axes[1, 1], patch_artist=True)
axes[1, 1].set_title('Total Charges by Churn', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Churn Status', fontsize=10)
axes[1, 1].set_ylabel('Total Charges ($)', fontsize=10)
axes[1, 1].get_figure().suptitle('')
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('exercise_cs2_charges_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: exercise_cs2_charges_analysis.png")
plt.close()

# =============================================================================
# STEP 13: Correlation Analysis
# =============================================================================

print("\n" + "-"*80)
print("STEP 13: CORRELATION ANALYSIS")
print("-"*80)

# Convert Churn to binary for correlation
df_corr = df_clean.copy()
df_corr['Churn_Binary'] = (df_corr['Churn'] == 'Yes').astype(int)

# Select numeric columns for correlation
numeric_for_corr = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Churn_Binary']
correlation_matrix = df_corr[numeric_for_corr].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

print("\nCorrelations with Churn:")
churn_correlations = correlation_matrix['Churn_Binary'].sort_values(ascending=False)
print(churn_correlations)

# Visualize correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.3f', cmap='coolwarm', 
            center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix - Numeric Features', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('exercise_cs2_correlation_matrix.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: exercise_cs2_correlation_matrix.png")
plt.close()

# =============================================================================
# STEP 14: Key Insights Summary
# =============================================================================

print("\n" + "="*80)
print("KEY INSIGHTS AND ISSUES IDENTIFIED")
print("="*80)

print("\n1. DATA QUALITY ISSUE (THE HINT!):")
print("   🚨 TotalCharges column was incorrectly stored as 'object' instead of numeric")
print("   • Contained empty string values (likely for new customers)")
print(f"   • {totalcharges_nan} records had non-numeric values")
print("   • Fixed by converting to numeric and imputing with MonthlyCharges")
print("   ✓ Resolution: Converted to float64 and imputed missing values")

print("\n2. CHURN RATE:")
print(f"   • Overall churn rate: {churn_rate:.2f}%")
print("   • This represents a significant customer retention challenge")

print("\n3. DEMOGRAPHIC INSIGHTS:")
senior_churn = df_clean[df_clean['SeniorCitizen'] == 1]['Churn'].value_counts(normalize=True)['Yes'] * 100
print(f"   • Senior citizens have higher churn rate: {senior_churn:.2f}%")
no_partner_churn = df_clean[df_clean['Partner'] == 'No']['Churn'].value_counts(normalize=True)['Yes'] * 100
print(f"   • Customers without partners churn more: {no_partner_churn:.2f}%")

print("\n4. CONTRACT TYPE - CRITICAL FACTOR:")
mtm_churn = df_clean[df_clean['Contract'] == 'Month-to-month']['Churn'].value_counts(normalize=True)['Yes'] * 100
one_year_churn = df_clean[df_clean['Contract'] == 'One year']['Churn'].value_counts(normalize=True)['Yes'] * 100
two_year_churn = df_clean[df_clean['Contract'] == 'Two year']['Churn'].value_counts(normalize=True)['Yes'] * 100
print(f"   • Month-to-month: {mtm_churn:.2f}% churn (HIGH RISK)")
print(f"   • One year: {one_year_churn:.2f}% churn")
print(f"   • Two year: {two_year_churn:.2f}% churn (LOW RISK)")
print("   💡 Recommendation: Incentivize longer contract commitments")

print("\n5. PAYMENT METHOD:")
elec_check_churn = df_clean[df_clean['PaymentMethod'] == 'Electronic check']['Churn'].value_counts(normalize=True)['Yes'] * 100
print(f"   • Electronic check has highest churn: {elec_check_churn:.2f}%")
print("   💡 Recommendation: Review payment experience for electronic check users")

print("\n6. TENURE PATTERN:")
churned_avg_tenure = df_clean[df_clean['Churn'] == 'Yes']['tenure'].mean()
retained_avg_tenure = df_clean[df_clean['Churn'] == 'No']['tenure'].mean()
print(f"   • Churned customers avg tenure: {churned_avg_tenure:.1f} months")
print(f"   • Retained customers avg tenure: {retained_avg_tenure:.1f} months")
print("   💡 Customers with longer tenure are more loyal")

print("\n7. CHARGES IMPACT:")
churned_avg_monthly = df_clean[df_clean['Churn'] == 'Yes']['MonthlyCharges'].mean()
retained_avg_monthly = df_clean[df_clean['Churn'] == 'No']['MonthlyCharges'].mean()
print(f"   • Churned customers avg monthly: ${churned_avg_monthly:.2f}")
print(f"   • Retained customers avg monthly: ${retained_avg_monthly:.2f}")
print("   💡 Higher monthly charges correlate with higher churn")

print("\n8. INTERNET SERVICE:")
fiber_churn = df_clean[df_clean['InternetService'] == 'Fiber optic']['Churn'].value_counts(normalize=True)['Yes'] * 100
dsl_churn = df_clean[df_clean['InternetService'] == 'DSL']['Churn'].value_counts(normalize=True)['Yes'] * 100
print(f"   • Fiber optic churn: {fiber_churn:.2f}%")
print(f"   • DSL churn: {dsl_churn:.2f}%")
print("   💡 Fiber optic customers churn more despite premium service")

print("\n" + "="*80)
print("VISUALIZATIONS CREATED")
print("="*80)
visualizations = [
    'exercise_cs2_churn_distribution.png',
    'exercise_cs2_demographics_churn.png',
    'exercise_cs2_contract_payment_churn.png',
    'exercise_cs2_tenure_analysis.png',
    'exercise_cs2_charges_analysis.png',
    'exercise_cs2_correlation_matrix.png'
]
for viz in visualizations:
    print(f"  ✓ {viz}")

print("\n" + "="*80)
print("RECOMMENDATIONS FOR CHURN REDUCTION")
print("="*80)

print("""
1. CONTRACT STRATEGY:
   • Offer incentives for customers to switch from month-to-month to longer contracts
   • Provide discounts or benefits for annual/2-year commitments
   
2. PAYMENT METHOD:
   • Investigate why electronic check users churn more
   • Promote automatic payment methods with benefits
   
3. CUSTOMER ONBOARDING:
   • Focus on first 6 months - critical retention period
   • Implement early engagement programs for new customers
   
4. PRICING REVIEW:
   • Customers with higher monthly charges churn more
   • Consider value-based pricing or loyalty discounts
   
5. FIBER OPTIC SERVICE:
   • High churn despite premium service suggests service quality or value perception issues
   • Conduct satisfaction survey for fiber optic customers
   
6. SENIOR CITIZEN SUPPORT:
   • Develop specialized support programs for senior citizens
   • Simplify service offerings and provide better assistance
   
7. TECH SUPPORT & SERVICES:
   • Customers without online security, backup, or tech support churn more
   • Bundle these services or make them more attractive
""")

print("\n" + "="*80)
print("EDA COMPLETED SUCCESSFULLY!")
print("="*80)

# Standard Python idiom
if __name__ == "__main__":
    pass
