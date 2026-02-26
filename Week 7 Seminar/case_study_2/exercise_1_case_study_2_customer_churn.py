import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Setup Paths ---
script_dir = os.path.dirname(os.path.abspath(__file__))
week7_data_dir = os.path.join(script_dir, "..", "data source")
week6_data_dir = os.path.join(script_dir, "..", "..", "Week 6 Seminar", "data source")
output_dir = os.path.join(script_dir, "visualizations")

os.makedirs(output_dir, exist_ok=True)

print("--- Case Study 2: Customer Churn Data Processing ---\n")

# Load Dataset (prefer Week 7 data source, fallback to Week 6 data source)
file_path_week7 = os.path.join(week7_data_dir, "customer_churn.csv")
file_path_week6 = os.path.join(week6_data_dir, "customer_churn.csv")

if os.path.exists(file_path_week7):
    churn_df = pd.read_csv(file_path_week7)
    print("Loaded dataset from Week 7 data source.")
elif os.path.exists(file_path_week6):
    churn_df = pd.read_csv(file_path_week6)
    print("Loaded dataset from Week 6 data source.")
else:
    raise FileNotFoundError("customer_churn.csv not found in Week 7 or Week 6 data source.")

print(f"Initial shape: {churn_df.shape}")
print(f"Initial columns: {list(churn_df.columns)}\n")

# ============================================================================
# STEP 1: CLEAN TOTALCHARGES (LAST WEEK'S EDA ISSUE)
# ============================================================================
# TotalCharges contains empty strings for new customers; convert to NaN then numeric
if "TotalCharges" in churn_df.columns:
    churn_df["TotalCharges"] = churn_df["TotalCharges"].astype(str).str.strip()
    churn_df.loc[churn_df["TotalCharges"] == "", "TotalCharges"] = np.nan
    churn_df["TotalCharges"] = pd.to_numeric(churn_df["TotalCharges"], errors="coerce")

# ============================================================================
# STEP 2: REMOVE ROWS WITH MORE THAN 1 MISSING VALUE
# ============================================================================
# .isnull().sum(axis=1) counts missing values per row; <= 1 keeps rows with 0 or 1 missing
initial_rows = len(churn_df)
churn_df = churn_df[churn_df.isnull().sum(axis=1) <= 1]
print(f"Rows removed (>1 missing): {initial_rows - len(churn_df)}")

# ============================================================================
# STEP 3: REMOVE COLUMNS WITH MORE THAN 33% MISSING VALUES
# ============================================================================
# Calculate missing percentage per column and drop those above the threshold
missing_pct = (churn_df.isnull().sum() / len(churn_df)) * 100
cols_to_drop = missing_pct[missing_pct > 33].index.tolist()
churn_df = churn_df.drop(columns=cols_to_drop)
print(f"Dropped columns (>33% missing): {cols_to_drop}\n")

# ============================================================================
# STEP 4: IMPUTE REMAINING MISSING VALUES
# ============================================================================
# Numeric -> median; Categorical -> mode
for col in churn_df.columns:
    if churn_df[col].isnull().sum() > 0:
        if churn_df[col].dtype in ["int64", "float64"]:
            churn_df[col].fillna(churn_df[col].median(), inplace=True)
        else:
            churn_df[col].fillna(churn_df[col].mode()[0], inplace=True)

print(f"Missing values after imputation: {churn_df.isnull().sum().sum()}\n")

# ============================================================================
# STEP 5: REMOVE OUTLIERS (MONTHLYCHARGES & TOTALCHARGES)
# ============================================================================
# IQR method for numeric columns with billing amounts
for col in ["MonthlyCharges", "TotalCharges"]:
    if col in churn_df.columns:
        Q1 = churn_df[col].quantile(0.25)
        Q3 = churn_df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        churn_df = churn_df[(churn_df[col] >= lower) & (churn_df[col] <= upper)]

# ============================================================================
# STEP 6: LOG TRANSFORMATION FOR SKEWED NUMERIC COLUMNS
# ============================================================================
numeric_cols = churn_df.select_dtypes(include=["int64", "float64"]).columns
skewed_cols = [col for col in numeric_cols if abs(churn_df[col].skew()) > 1]

if skewed_cols:
    fig, axes = plt.subplots(len(skewed_cols), 2, figsize=(12, 4 * len(skewed_cols)))
    if len(skewed_cols) == 1:
        axes = axes.reshape(1, -1)

    for idx, col in enumerate(skewed_cols):
        # Plot original distribution
        axes[idx, 0].hist(churn_df[col], bins=30, edgecolor="black")
        axes[idx, 0].set_title(f"{col} - Original")

        # Log-transform and replace
        churn_df[col] = np.log1p(churn_df[col])
        axes[idx, 1].hist(churn_df[col], bins=30, edgecolor="black")
        axes[idx, 1].set_title(f"{col} - Log Transformed")

    plt.tight_layout()
    plot_path = os.path.join(output_dir, "log_transformations_churn.png")
    plt.savefig(plot_path, dpi=100, bbox_inches="tight")
    plt.close()
    print(f"Log transform visualization saved to: {plot_path}\n")

# ============================================================================
# STEP 7: CREATE DUMMY VARIABLES (CATEGORICAL <=5 UNIQUE VALUES)
# ============================================================================
cat_cols = churn_df.select_dtypes(include=["object"]).columns
for col in cat_cols:
    if churn_df[col].nunique() <= 5:
        dummies = pd.get_dummies(churn_df[col], prefix=col, drop_first=True)
        churn_df = pd.concat([churn_df, dummies], axis=1)
        churn_df.drop(columns=[col], inplace=True)

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("--- Final Data Summary ---")
print(f"Final shape: {churn_df.shape}")
print(f"Missing values: {churn_df.isnull().sum().sum()}")
print(churn_df.head())