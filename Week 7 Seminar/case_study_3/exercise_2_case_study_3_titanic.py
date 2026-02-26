import pandas as pd
import numpy as np
import re
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for visualizations
sns.set_theme(style="whitegrid")

def main():
    print("--- Case Study 3: Titanic Name Parsing with Regular Expressions ---")
    
    # Define file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(os.path.dirname(current_dir), "data source", "titanic_train.csv")
    
    if not os.path.exists(data_path):
        print(f"Warning: {data_path} not found. Loading from seaborn...")
        df_titanic = sns.load_dataset('titanic')
        # Seaborn titanic doesn't have the 'Name' column, so we might need the CSV
        if 'Name' not in df_titanic.columns:
            print("Error: Seaborn dataset does not contain 'Name' column. Please ensure titanic_train.csv exists.")
            return
    else:
        df_titanic = pd.read_csv(data_path)
    
    print(f"Dataset Shape: {df_titanic.shape}")
    print(f"Original Name column samples:\n{df_titanic['Name'].head()}")

    # --- Regular Expression for Name Parsing ---
    # Format: "Surname, Title. Firstname"
    # ^([^,]+)    : Matches characters from start that are NOT a comma (Surname)
    # ,\s*        : Matches the comma and optional following spaces
    # ([^.]+)     : Matches characters between comma and dot that are NOT a dot (Title)
    # \.\s*       : Matches the dot and optional following spaces
    # (.*)$       : Matches everything else until the end of string (Firstname)
    name_regex = r'^([^,]+),\s*([^.]+)\.\s*(.*)$'

    print("\nApplying Regular Expression to split 'Name'...")
    
    # Extract the components into new columns
    name_extracted = df_titanic['Name'].str.extract(name_regex)
    name_extracted.columns = ['Surname', 'Title', 'FirstName']
    
    # Join back to original dataframe (or keep selected columns)
    df_parsed = pd.concat([df_titanic[['PassengerId', 'Name', 'Survived']], name_extracted], axis=1)

    print("\nResults of splitting (Head):")
    print(df_parsed[['Name', 'Surname', 'Title', 'FirstName']].head())

    # --- Analysis of Titles ---
    print("\nFrequency of Titles found:")
    title_counts = df_parsed['Title'].value_counts()
    print(title_counts)

    # --- Survivability by Title (Social Status Analysis) ---
    print("\nSurvivability by Title:")
    # Group uncommon titles into 'Rare' to make analysis cleaner
    rare_titles = title_counts[title_counts < 10].index
    df_parsed['TitleGroup'] = df_parsed['Title'].replace(rare_titles, 'Rare')
    
    survival_by_title = df_parsed.groupby('TitleGroup')['Survived'].mean().sort_values(ascending=False)
    print(survival_by_title)

    # Visualization
    viz_dir = os.path.join(current_dir, "visualizations")
    if not os.path.exists(viz_dir):
        os.makedirs(viz_dir)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=survival_by_title.index, y=survival_by_title.values, palette="viridis")
    plt.title("Titanic Survivability by Title (Parsed via RegEx)")
    plt.ylabel("Survival Rate")
    plt.xlabel("Title Group")
    plt.savefig(os.path.join(viz_dir, "survival_by_title.png"))
    
    print(f"\nAnalysis complete. Visualization saved to {os.path.join(viz_dir, 'survival_by_title.png')}")

if __name__ == "__main__":
    main()
