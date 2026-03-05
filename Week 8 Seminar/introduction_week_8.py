"""
Week 8 Seminar: Machine Learning with Scikit-Learn
This script covers:
1. Data Processing with SKlearn (Imputation, Scaling, Encoding)
2. Dimensionality Reduction (PCA, Feature Selection)
3. Supervised Learning with Decision Trees
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer, IterativeImputer, KNNImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OrdinalEncoder, OneHotEncoder
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import BayesianRidge
import os

print("=" * 80)
print("WEEK 8 SEMINAR: MACHINE LEARNING WITH SCIKIT-LEARN")
print("=" * 80)

# ============================================================================
# PART 1: DATA PROCESSING WITH SKLEARN
# ============================================================================
print("\n" + "=" * 80)
print("PART 1: DATA PROCESSING WITH SKLEARN")
print("=" * 80)

# Load Titanic dataset
try:
    # Use absolute path or construct path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'titanic_train.csv')
    df_titan = pd.read_csv(data_path, index_col=0)
except FileNotFoundError:
    print(f"Warning: {data_path} not found. Please ensure it's in the working directory.")
    df_titan = None

if df_titan is not None:
    print("\nDataset Info:")
    print(df_titan.info())
    
    # ========== SECTION 1: IMPUTATION ==========
    print("\n" + "-" * 80)
    print("SECTION 1: IMPUTATION")
    print("-" * 80)
    
    # Keep numeric columns for demonstration
    imputation_features = df_titan.select_dtypes(include=[np.number]).columns
    imputation_features_list = list(imputation_features)
    
    print("\n### Simple Imputation (Mean Strategy) ###")
    imp = SimpleImputer(strategy='mean')
    df_titan_numeric = df_titan.select_dtypes(include=[np.number]).copy()
    
    # Impute Age column
    df_titan_numeric['Age'] = imp.fit_transform(df_titan_numeric[['Age']])
    print("Age column imputed with mean strategy.")
    print(f"Missing values after imputation: {df_titan_numeric['Age'].isnull().sum()}")
    
    print("\n### Iterative Imputation ###")
    imputation_features = df_titan_numeric.select_dtypes(include=[np.number]).columns
    imputation_features = imputation_features.drop('Survived')  # Exclude target
    
    iter_imp = IterativeImputer(n_nearest_features=2, max_iter=10, random_state=42)
    iter_imp.fit(df_titan_numeric[imputation_features])
    print("Iterative imputer fitted with BayesianRidge estimator.")
    
    print("\n### KNN Imputation ###")
    kimp = KNNImputer(n_neighbors=5, weights="uniform")
    kimp.fit(df_titan_numeric[imputation_features])
    print("KNN imputer fitted with 5 nearest neighbors.")
    
    # ========== SECTION 2: SCALING ==========
    print("\n" + "-" * 80)
    print("SECTION 2: SCALING")
    print("-" * 80)
    
    print("\n### Standardization ###")
    scaler = StandardScaler()
    df_titan_numeric['Age_Std'] = scaler.fit_transform(df_titan_numeric[['Age']])
    print("Standardization applied to Age column.")
    print(f"Mean of standardized Age: {df_titan_numeric['Age_Std'].mean():.6f}")
    print(f"Std of standardized Age: {df_titan_numeric['Age_Std'].std():.6f}")
    
    print("\n### MinMax Scaling ###")
    mm_scaler = MinMaxScaler()
    df_titan_numeric['Age_MM'] = mm_scaler.fit_transform(df_titan_numeric[['Age']])
    print("MinMax scaling applied to Age column.")
    print(f"Min of scaled Age: {df_titan_numeric['Age_MM'].min():.6f}")
    print(f"Max of scaled Age: {df_titan_numeric['Age_MM'].max():.6f}")
    
    # ========== SECTION 3: ENCODING ==========
    print("\n" + "-" * 80)
    print("SECTION 3: ENCODING CATEGORICAL VARIABLES")
    print("-" * 80)
    
    print("\n### Ordinal Encoding ###")
    df_titan_encode = df_titan.select_dtypes(include=[np.number]).copy()
    sex_ordinal = df_titan[['Sex']].copy()
    
    enc_ordinal = OrdinalEncoder()
    sex_ordinal['Sex_Encoded'] = enc_ordinal.fit_transform(df_titan[['Sex']])
    print("Ordinal encoding applied to Sex column.")
    print(f"Mapping: {dict(zip(enc_ordinal.categories_[0], range(len(enc_ordinal.categories_[0]))))}")
    
    print("\n### One-Hot Encoding ###")
    enc_onehot = OneHotEncoder(sparse_output=False)
    sex_onehot = enc_onehot.fit_transform(df_titan[['Sex']])
    df_sex = pd.DataFrame(sex_onehot, columns=enc_onehot.get_feature_names_out())
    print("One-Hot encoding applied to Sex column.")
    print(f"Created columns: {list(df_sex.columns)}")
    
    # ========== SECTION 4: DIMENSIONALITY REDUCTION ==========
    print("\n" + "-" * 80)
    print("SECTION 4: DIMENSIONALITY REDUCTION")
    print("-" * 80)
    
    print("\n### Variance Threshold ###")
    df_titan_clean = df_titan_numeric.dropna()
    vt = VarianceThreshold(threshold=0)
    print(f"Original shape: {df_titan_clean.shape}")
    df_variance_filtered = vt.fit_transform(df_titan_clean)
    print(f"Shape after variance filtering: {df_variance_filtered.shape}")
    
    print("\n### Principal Component Analysis (PCA) ###")
    pca_full = PCA()
    pca_full.fit(df_titan_clean)
    print(f"Total variance explained by all components: {pca_full.explained_variance_ratio_.sum():.6f}")
    print(f"Explained variance ratio per component:\n{pca_full.explained_variance_ratio_}")
    
    print("\n### PCA with 3 Components ###")
    pca_3 = PCA(n_components=3)
    pca_3_data = pca_3.fit_transform(df_titan_clean)
    print(f"Variance explained by 3 components: {pca_3.explained_variance_ratio_.sum():.6f}")
    print(f"Explained variance ratio: {pca_3.explained_variance_ratio_}")
    
    print("\n### PCA with MLE Component Selection ###")
    pca_mle = PCA(n_components='mle')
    pca_mle_data = pca_mle.fit_transform(df_titan_clean)
    print(f"Automatically selected {pca_mle.n_components_} components")
    print(f"Variance explained: {pca_mle.explained_variance_ratio_.sum():.6f}")

# ============================================================================
# PART 2: SUPERVISED LEARNING WITH DECISION TREES
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: SUPERVISED LEARNING WITH DECISION TREES (IRIS DATASET)")
print("=" * 80)

# Load Iris dataset
iris = sns.load_dataset('iris')

print("\nIris Dataset Shape:", iris.shape)
print(iris.head())

# ========== STEP 1: CREATING TRAINING/TESTING DATASET ==========
print("\n" + "-" * 80)
print("STEP 1: CREATING TRAINING/TESTING DATASET")
print("-" * 80)

feature_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
X = iris[feature_cols]  # Features
y = iris.species  # Target variable

print(f"Features (X) shape: {X.shape}")
print(f"Target (y) shape: {y.shape}")

# Split into training and test sets (70-30 split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1)

print(f"\nTraining set size: {len(X_train)} samples")
print(f"Test set size: {len(X_test)} samples")

# ========== STEP 2: INSTANTIATING THE CLASSIFIER ==========
print("\n" + "-" * 80)
print("STEP 2: INSTANTIATING THE CLASSIFIER")
print("-" * 80)

clf = DecisionTreeClassifier()
print("Decision Tree Classifier instantiated with default parameters.")

# ========== STEP 3: TRAINING THE CLASSIFIER ==========
print("\n" + "-" * 80)
print("STEP 3: TRAINING THE CLASSIFIER")
print("-" * 80)

clf = clf.fit(X_train, y_train)
print("Decision Tree Classifier trained on training data.")
print(f"Tree depth: {clf.get_depth()}")
print(f"Number of leaves: {clf.get_n_leaves()}")

# ========== STEP 4: MAKING PREDICTIONS ==========
print("\n" + "-" * 80)
print("STEP 4: MAKING PREDICTIONS")
print("-" * 80)

y_pred = clf.predict(X_test)
print(f"Predictions made on {len(X_test)} test samples.")
print(f"First 10 predictions: {y_pred[:10]}")
print(f"First 10 actual values: {list(y_test.iloc[:10])}")

# ========== STEP 5: EVALUATING PERFORMANCE ==========
print("\n" + "-" * 80)
print("STEP 5: EVALUATING PERFORMANCE")
print("-" * 80)

accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")

# Additional metrics
print("\nClassification Report:")
print(metrics.classification_report(y_test, y_pred))

# ========== STEP 6: VISUALIZING THE TREE ==========
print("\n" + "-" * 80)
print("STEP 6: VISUALIZING THE TREE")
print("-" * 80)

# Create visualization
plt.figure(figsize=(20, 10))
plot_tree(clf, feature_names=feature_cols, class_names=list(iris.species.unique()), 
          filled=True, rounded=True)

# Save the tree visualization
output_dir = os.path.dirname(os.path.abspath(__file__))
svg_path = os.path.join(output_dir, 'decision_tree.svg')
png_path = os.path.join(output_dir, 'decision_tree.png')

plt.savefig(svg_path, format='svg', bbox_inches='tight', dpi=300)
plt.savefig(png_path, format='png', bbox_inches='tight', dpi=300)
print(f"Decision tree visualization saved:")
print(f"  - {svg_path}")
print(f"  - {png_path}")

# Display feature importances
print("\nFeature Importances:")
for feature, importance in zip(feature_cols, clf.feature_importances_):
    print(f"  {feature}: {importance:.4f}")

print("\n" + "=" * 80)
print("WEEK 8 SEMINAR COMPLETED SUCCESSFULLY")
print("=" * 80)
