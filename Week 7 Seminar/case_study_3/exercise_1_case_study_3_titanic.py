import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for visualizations
sns.set_theme(style="whitegrid")

def main():
    print("--- Case Study 3: Titanic Dataset Processing ---")
    
    # Define file paths
    # We look for the dataset in Week 7 data source first, then fallback to Week 6 or Seaborn
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(os.path.dirname(current_dir), "data source", "titanic_train.csv")
    
    if not os.path.exists(data_path):
        print(f"Warning: {data_path} not found. Loading from seaborn...")
        df_titanic = sns.load_dataset('titanic')
        # Map seaborn names to match titanic_train.csv if possible
        df_titanic = df_titanic.rename(columns={'survived': 'Survived', 'pclass': 'Pclass', 'sex': 'Sex', 
                                              'age': 'Age', 'sibsp': 'SibSp', 'parch': 'Parch', 
                                              'fare': 'Fare', 'embarked': 'Embarked'})
    else:
        df_titanic = pd.read_csv(data_path)
    
    print(f"Initial Dataset Shape: {df_titanic.shape}")
    print("\nInitial Missing Values:")
    print(df_titanic.isnull().sum())

    # --- STEP 1: Remove rows with more than 1 missing value ---
    # We use .isnull().sum(axis=1) to count missing values per row
    df_step1 = df_titanic[df_titanic.isnull().sum(axis=1) <= 1].copy()
    print(f"\nStep 1: Removed rows with >1 missing value. New shape: {df_step1.shape}")

    # --- STEP 2: Remove columns with more than 33% missing values ---
    # We calculate the percentage of missing values per column
    missing_pct = (df_step1.isnull().sum() / len(df_step1)) * 100
    cols_to_keep = missing_pct[missing_pct <= 33].index
    df_step2 = df_step1[cols_to_keep].copy()
    print(f"Step 2: Removed columns with >33% missingness ({list(set(df_step1.columns) - set(cols_to_keep))} dropped). New shape: {df_step2.shape}")

    # --- STEP 3: Impute missing values ---
    # For numeric columns (like Age), we fill with the median
    # For categorical columns (like Embarked), we fill with the mode
    for col in df_step2.columns:
        if df_step2[col].isnull().any():
            if pd.api.types.is_numeric_dtype(df_step2[col]):
                median_val = df_step2[col].median()
                df_step2[col] = df_step2[col].fillna(median_val)
                print(f"Imputed numeric '{col}' with median: {median_val}")
            else:
                mode_val = df_step2[col].mode()[0]
                df_step2[col] = df_step2[col].fillna(mode_val)
                print(f"Imputed categorical '{col}' with mode: {mode_val}")

    # --- STEP 4: Remove outliers in 'Fare' using IQR ---
    # Outliers can skew statistical models, so we remove values outside 1.5 * IQR
    Q1 = df_step2['Fare'].quantile(0.25)
    Q3 = df_step2['Fare'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    df_step4 = df_step2[(df_step2['Fare'] >= lower_bound) & (df_step2['Fare'] <= upper_bound)].copy()
    print(f"\nStep 4: Removed Fare outliers. New shape: {df_step4.shape}")

    # --- STEP 5: Log transformation for highly skewed numeric features ---
    # We check for skewness and apply np.log1p (log(1+x)) to normalize the distribution
    # This is useful for features with a long right tail
    viz_dir = os.path.join(current_dir, "visualizations")
    if not os.path.exists(viz_dir):
        os.makedirs(viz_dir)
        
    num_cols = df_step4.select_dtypes(include=[np.number]).columns
    skewed_cols = []
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(df_step4['Fare'], kde=True)
    plt.title(f"Original Fare (Skew: {df_step4['Fare'].skew():.2f})")
    
    for col in num_cols:
        if abs(df_step4[col].skew()) > 1:
            df_step4[col] = np.log1p(df_step4[col])
            skewed_cols.append(col)
            
    plt.subplot(1, 2, 2)
    sns.histplot(df_step4['Fare'], kde=True)
    plt.title(f"Log Transformed Fare (Skew: {df_step4['Fare'].skew():.2f})")
    plt.savefig(os.path.join(viz_dir, "log_transformations_titanic.png"))
    print(f"Step 5: Applied log transformation to: {skewed_cols}")

    # --- STEP 6: Dummy encoding for categorical variables ---
    # We convert categorical labels into numeric columns (One-Hot Encoding)
    # This is done for features with limited unique values (<= 5)
    cat_cols = df_step4.select_dtypes(include=['object']).columns
    cols_to_encode = [col for col in cat_cols if df_step4[col].nunique() <= 5]
    
    df_step6 = pd.get_dummies(df_step4, columns=cols_to_encode, drop_first=True)
    print(f"Step 6: Created dummies for: {cols_to_encode}. Final columns: {df_step6.columns.tolist()}")

    # --- STEP 7: Feature Engineering - Group Age into periods ---
    # We group Age into Child, Adult, and Senior to capture non-linear effects
    # Then we encode these new categories as dummies
    def age_group(age):
        if age < 18: return 'Child'
        if age < 60: return 'Adult'
        return 'Senior'

    df_step6['AgeGroup'] = df_step6['Age'].apply(age_group)
    df_final = pd.get_dummies(df_step6, columns=['AgeGroup'], drop_first=True)
    
    print(f"\nStep 7: Created AgeGroup and encoded as dummies.")
    print(f"Final Dataset Sample:\n{df_final.head()}")
    print(f"Final Metadata: {df_final.shape[0]} rows, {df_final.shape[1]} columns")
    print(f"Missing values after processing: {df_final.isnull().sum().sum()}")

if __name__ == "__main__":
    main()
