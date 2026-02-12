# Week 5 Seminar - Exercise 3
# Programming for Data Analytics
# Date: February 12, 2026

"""
Week 5 Exercise 3 - Data Visualization and Statistical Analysis
-----------------------------------------------------------------
EXERCISE QUESTIONS:
1. Visualize the distribution of meta_score and user_review
2. Visualize the relationship between meta_score and user_review
3. Find the average and standard deviation of meta_score and user_review
4. Remove rows with NaN values and repeat analysis
5. Compare statistics before and after removing NaN values

CONCEPTS COVERED:
- Data visualization with Matplotlib and Seaborn
- Histograms and distribution plots
- Scatter plots for relationship visualization
- Boolean masking to remove NaN values
- Statistical analysis (mean, std) on clean data
- Data quality assessment

LEARNING OBJECTIVES:
- Create meaningful visualizations for exploratory data analysis (EDA)
- Understand data distributions and relationships
- Calculate and interpret statistical measures
- Handle missing data effectively
- Recognize impact of NaN on statistical calculations
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def exercise_3_part_a():
    """
    Exercise 3 - Part A: Load data and visualize distributions
    
    QUESTION 1: Visualize the distribution of meta_score and user_review
    
    ANSWER: Create histograms and distribution plots using:
            - plt.hist() for histograms showing frequency of values
            - sns.histplot() for enhanced histograms with KDE overlay
            - Create separate visualizations for each variable
    
    EXPLANATION:
    - Histograms show how values are distributed across ranges
    - A good distribution visualization helps identify patterns:
      * Normal distribution (bell-shaped): Most values near mean
      * Skewed distribution: Values bunched on one side
      * Bimodal distribution: Two peaks suggest different groups
    - KDE (Kernel Density Estimation) overlay smooths the histogram
    """
    print("\n" + "="*80)
    print("EXERCISE 3 - PART A: Load Data and Visualize Distributions")
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
    
    print(f"Data shape: {games_data.shape}")
    print(f"Data type: {games_data.dtype}")
    
    meta_score = games_data[:, 0]
    user_review = games_data[:, 1]
    
    print(f"\nmeta_score - Min: {np.nanmin(meta_score):.1f}, Max: {np.nanmax(meta_score):.1f}")
    print(f"user_review - Min: {np.nanmin(user_review):.1f}, Max: {np.nanmax(user_review):.1f}")
    
    # Check for NaN values
    nan_count_meta = np.isnan(meta_score).sum()
    nan_count_user = np.isnan(user_review).sum()
    print(f"\nMissing values - meta_score: {nan_count_meta}, user_review: {nan_count_user}")
    
    # Create visualizations
    print("\n" + "-"*80)
    print("VISUALIZING DISTRIBUTIONS")
    print("-"*80)
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Meta Score and User Review Distributions', fontsize=16, fontweight='bold')
    
    # Subplot 1: Meta Score Histogram with KDE
    print("\n1. Meta Score Histogram with KDE overlay...")
    ax1 = axes[0, 0]
    sns.histplot(meta_score, kde=True, ax=ax1, bins=30, color='steelblue', stat='density')
    ax1.set_xlabel('Meta Score', fontsize=11)
    ax1.set_ylabel('Density', fontsize=11)
    ax1.set_title('Meta Score Distribution', fontsize=12, fontweight='bold')
    ax1.grid(alpha=0.3)
    
    # Subplot 2: User Review Histogram with KDE
    print("2. User Review Histogram with KDE overlay...")
    ax2 = axes[0, 1]
    sns.histplot(user_review, kde=True, ax=ax2, bins=30, color='coral', stat='density')
    ax2.set_xlabel('User Review Score', fontsize=11)
    ax2.set_ylabel('Density', fontsize=11)
    ax2.set_title('User Review Distribution', fontsize=12, fontweight='bold')
    ax2.grid(alpha=0.3)
    
    # Subplot 3: Box Plot Comparison
    print("3. Box plot comparison...")
    ax3 = axes[1, 0]
    # Normalize user_review to 0-100 scale for fair comparison
    user_review_scaled = (user_review / 10) * 100  # Convert from 0-100 scale
    box_data = [meta_score, user_review_scaled]
    bp = ax3.boxplot(box_data, labels=['Meta Score', 'User Review\n(Scaled to 0-100)'], 
                     patch_artist=True, widths=0.6)
    for patch, color in zip(bp['boxes'], ['steelblue', 'coral']):
        patch.set_facecolor(color)
    ax3.set_ylabel('Score', fontsize=11)
    ax3.set_title('Score Comparison (Box Plot)', fontsize=12, fontweight='bold')
    ax3.grid(alpha=0.3, axis='y')
    
    # Subplot 4: Violin Plot
    print("4. Violin plot for distribution shape...")
    ax4 = axes[1, 1]
    parts = ax4.violinplot([meta_score[~np.isnan(meta_score)]], positions=[1], widths=0.7, 
                           showmeans=True, showmedians=True)
    parts = ax4.violinplot([user_review[~np.isnan(user_review)]], positions=[2], widths=0.7,
                           showmeans=True, showmedians=True)
    ax4.set_xticks([1, 2])
    ax4.set_xticklabels(['Meta Score', 'User Review'])
    ax4.set_ylabel('Value', fontsize=11)
    ax4.set_title('Distribution Shape (Violin Plot)', fontsize=12, fontweight='bold')
    ax4.grid(alpha=0.3, axis='y')
    
    plt.tight_layout()
    
    # Save figure
    output_path = os.path.join(SCRIPT_DIR, 'exercise_3_distributions.png')
    print(f"\nSaving visualization to: {output_path}")
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.show()
    
    print("\n✅ Distribution visualizations created and saved!")
    
    return meta_score, user_review


def exercise_3_part_b():
    """
    Exercise 3 - Part B: Visualize relationship between variables
    
    QUESTION 2: Visualize the relationship between meta_score and user_review
    
    ANSWER: Create scatter plots and regression plots using:
            - plt.scatter() for basic scatter plot showing individual points
            - sns.regplot() for scatter plot with regression line
            - sns.heatmap() for correlation heatmap
            - Calculate correlation coefficient to quantify relationship
    
    EXPLANATION:
    - Scatter plots show relationship between two continuous variables
    - Positive correlation: Points trend upward (left to right)
    - Negative correlation: Points trend downward (left to right)
    - No correlation: Points scattered randomly
    - Regression line shows the trend direction and strength
    """
    print("\n" + "="*80)
    print("EXERCISE 3 - PART B: Visualize Relationship Between Variables")
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
    
    print("\n" + "-"*80)
    print("VISUALIZING RELATIONSHIP")
    print("-"*80)
    
    # Create figure with subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('Relationship: Meta Score vs User Review', fontsize=16, fontweight='bold')
    
    # Subplot 1: Scatter Plot with Regression Line
    print("\n1. Scatter plot with regression line...")
    ax1 = axes[0]
    
    # Create scatter plot
    ax1.scatter(meta_score, user_review, alpha=0.6, color='steelblue', s=30, edgecolors='navy', linewidth=0.5)
    
    # Add regression line (only using non-NaN values)
    valid_mask = ~(np.isnan(meta_score) | np.isnan(user_review))
    valid_meta = meta_score[valid_mask]
    valid_user = user_review[valid_mask]
    
    if len(valid_meta) > 1:
        # Calculate regression line
        z = np.polyfit(valid_meta, valid_user, 1)
        p = np.poly1d(z)
        x_line = np.linspace(np.nanmin(meta_score), np.nanmax(meta_score), 100)
        ax1.plot(x_line, p(x_line), "r-", linewidth=2, label=f'Trend line: y={z[0]:.3f}x+{z[1]:.1f}')
        
        # Calculate correlation
        correlation = np.corrcoef(valid_meta, valid_user)[0, 1]
        ax1.text(0.05, 0.95, f'Correlation: {correlation:.3f}', transform=ax1.transAxes,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                fontsize=10)
    
    ax1.set_xlabel('Meta Score', fontsize=11)
    ax1.set_ylabel('User Review Score', fontsize=11)
    ax1.set_title('Scatter Plot with Regression Line', fontsize=12, fontweight='bold')
    ax1.legend(loc='lower right')
    ax1.grid(alpha=0.3)
    
    # Subplot 2: 2D Density Plot (Hex Bin)
    print("2. 2D density plot (hexbin)...")
    ax2 = axes[1]
    hb = ax2.hexbin(meta_score, user_review, gridsize=20, cmap='YlOrRd', mincnt=1)
    ax2.set_xlabel('Meta Score', fontsize=11)
    ax2.set_ylabel('User Review Score', fontsize=11)
    ax2.set_title('2D Density Plot (Point Concentration)', fontsize=12, fontweight='bold')
    cb = plt.colorbar(hb, ax=ax2)
    cb.set_label('Count', fontsize=10)
    
    plt.tight_layout()
    
    # Save figure
    output_path = os.path.join(SCRIPT_DIR, 'exercise_3_relationship.png')
    print(f"\nSaving visualization to: {output_path}")
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.show()
    
    # Print correlation analysis
    print("\n" + "-"*80)
    print("CORRELATION ANALYSIS")
    print("-"*80)
    
    if len(valid_meta) > 1:
        correlation = np.corrcoef(valid_meta, valid_user)[0, 1]
        print(f"\nPearson Correlation Coefficient: {correlation:.4f}")
        
        if abs(correlation) < 0.3:
            strength = "weak"
        elif abs(correlation) < 0.7:
            strength = "moderate"
        else:
            strength = "strong"
        
        direction = "positive" if correlation > 0 else "negative"
        
        print(f"Interpretation: {strength.capitalize()} {direction} correlation")
        print(f"Meaning: As meta_score increases, user_review tends to {direction}ly {'increase' if correlation > 0 else 'decrease'}")
    
    print("\n✅ Relationship visualization completed!")
    
    return meta_score, user_review


def exercise_3_part_c():
    """
    Exercise 3 - Part C: Statistical analysis with NaN handling
    
    QUESTION 3: Find the average and std of meta_score and user_review
    QUESTION 4: Remove rows with NaN values and repeat analysis
    
    ANSWER: Use np.nanmean() and np.nanstd() for statistics with NaN present
            Remove NaN rows using: a[~np.isnan(a).any(axis=1)]
            Compare statistics before and after cleaning
    
    EXPLANATION:
    - np.nanmean() / np.nanstd(): Ignore NaN values in calculations
    - Removing rows with any NaN gives cleaner statistics
    - Comparing results shows impact of missing data on analysis
    - Clean data often provides more reliable statistics
    """
    print("\n" + "="*80)
    print("EXERCISE 3 - PART C: Statistical Analysis")
    print("="*80)
    
    # Load data
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
    
    print("\n" + "-"*80)
    print("STATISTICS WITH NaN VALUES PRESENT (using nanmean, nanstd)")
    print("-"*80)
    
    # Statistics with NaN present (using NaN-aware functions)
    meta_score_all = games_data[:, 0]
    user_review_all = games_data[:, 1]
    
    meta_mean_with_nan = np.nanmean(meta_score_all)
    meta_std_with_nan = np.nanstd(meta_score_all)
    user_mean_with_nan = np.nanmean(user_review_all)
    user_std_with_nan = np.nanstd(user_review_all)
    
    print(f"\nMeta Score (with NaN):")
    print(f"  - Count: {(~np.isnan(meta_score_all)).sum()} values")
    print(f"  - Missing: {np.isnan(meta_score_all).sum()} NaN")
    print(f"  - Mean: {meta_mean_with_nan:.4f}")
    print(f"  - Std Dev: {meta_std_with_nan:.4f}")
    print(f"  - Min: {np.nanmin(meta_score_all):.4f}")
    print(f"  - Max: {np.nanmax(meta_score_all):.4f}")
    
    print(f"\nUser Review (with NaN):")
    print(f"  - Count: {(~np.isnan(user_review_all)).sum()} values")
    print(f"  - Missing: {np.isnan(user_review_all).sum()} NaN")
    print(f"  - Mean: {user_mean_with_nan:.4f}")
    print(f"  - Std Dev: {user_std_with_nan:.4f}")
    print(f"  - Min: {np.nanmin(user_review_all):.4f}")
    print(f"  - Max: {np.nanmax(user_review_all):.4f}")
    
    print("\n" + "-"*80)
    print("REMOVING NaN ROWS AND RECALCULATING STATISTICS")
    print("-"*80)
    
    # Remove rows with any NaN values
    clean_data = games_data[~np.isnan(games_data).any(axis=1)]
    
    print(f"\nData shape before cleaning: {games_data.shape}")
    print(f"Data shape after cleaning: {clean_data.shape}")
    print(f"Rows removed: {games_data.shape[0] - clean_data.shape[0]}")
    
    # Statistics on clean data (without NaN)
    meta_score_clean = clean_data[:, 0]
    user_review_clean = clean_data[:, 1]
    
    meta_mean_clean = np.mean(meta_score_clean)
    meta_std_clean = np.std(meta_score_clean)
    user_mean_clean = np.mean(user_review_clean)
    user_std_clean = np.std(user_review_clean)
    
    print(f"\nMeta Score (clean data, no NaN):")
    print(f"  - Count: {len(meta_score_clean)} values")
    print(f"  - Missing: 0 NaN")
    print(f"  - Mean: {meta_mean_clean:.4f}")
    print(f"  - Std Dev: {meta_std_clean:.4f}")
    print(f"  - Min: {np.min(meta_score_clean):.4f}")
    print(f"  - Max: {np.max(meta_score_clean):.4f}")
    
    print(f"\nUser Review (clean data, no NaN):")
    print(f"  - Count: {len(user_review_clean)} values")
    print(f"  - Missing: 0 NaN")
    print(f"  - Mean: {user_mean_clean:.4f}")
    print(f"  - Std Dev: {user_std_clean:.4f}")
    print(f"  - Min: {np.min(user_review_clean):.4f}")
    print(f"  - Max: {np.max(user_review_clean):.4f}")
    
    print("\n" + "-"*80)
    print("COMPARISON: Impact of NaN on Statistics")
    print("-"*80)
    
    meta_mean_diff = abs(meta_mean_with_nan - meta_mean_clean)
    meta_std_diff = abs(meta_std_with_nan - meta_std_clean)
    user_mean_diff = abs(user_mean_with_nan - user_mean_clean)
    user_std_diff = abs(user_std_with_nan - user_std_clean)
    
    print(f"\nMeta Score:")
    print(f"  - Mean difference: {meta_mean_diff:.6f} ({(meta_mean_diff/meta_mean_clean)*100:.3f}%)")
    print(f"  - Std Dev difference: {meta_std_diff:.6f} ({(meta_std_diff/meta_std_clean)*100:.3f}%)")
    
    print(f"\nUser Review:")
    print(f"  - Mean difference: {user_mean_diff:.6f} ({(user_mean_diff/user_mean_clean)*100:.3f}%)")
    print(f"  - Std Dev difference: {user_std_diff:.6f} ({(user_std_diff/user_std_clean)*100:.3f}%)")
    
    # Create comparison visualization
    print("\n" + "-"*80)
    print("CREATING COMPARISON VISUALIZATION")
    print("-"*80)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('Statistical Comparison: With NaN vs Clean Data', fontsize=16, fontweight='bold')
    
    # Mean comparison
    ax1 = axes[0]
    categories = ['Meta Score', 'User Review']
    with_nan = [meta_mean_with_nan, user_mean_with_nan]
    without_nan = [meta_mean_clean, user_mean_clean]
    
    x = np.arange(len(categories))
    width = 0.35
    
    bars1 = ax1.bar(x - width/2, with_nan, width, label='With NaN (nanmean)', color='lightcoral')
    bars2 = ax1.bar(x + width/2, without_nan, width, label='Clean Data (mean)', color='lightgreen')
    
    ax1.set_ylabel('Mean Value', fontsize=11)
    ax1.set_title('Mean Comparison', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories)
    ax1.legend()
    ax1.grid(alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}', ha='center', va='bottom', fontsize=9)
    
    # Std Dev comparison
    ax2 = axes[1]
    with_nan_std = [meta_std_with_nan, user_std_with_nan]
    without_nan_std = [meta_std_clean, user_std_clean]
    
    bars1 = ax2.bar(x - width/2, with_nan_std, width, label='With NaN (nanstd)', color='lightcoral')
    bars2 = ax2.bar(x + width/2, without_nan_std, width, label='Clean Data (std)', color='lightgreen')
    
    ax2.set_ylabel('Standard Deviation', fontsize=11)
    ax2.set_title('Standard Deviation Comparison', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(categories)
    ax2.legend()
    ax2.grid(alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}', ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    
    # Save figure
    output_path = os.path.join(SCRIPT_DIR, 'exercise_3_statistics.png')
    print(f"\nSaving comparison visualization to: {output_path}")
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.show()
    
    print("\n✅ Statistical analysis completed!")
    
    return clean_data, (meta_mean_clean, meta_std_clean, user_mean_clean, user_std_clean)


def complete_exercise_sequence():
    """
    Complete Exercise 3 Sequence - All operations in order
    
    This function demonstrates the complete workflow:
    1. Load data and visualize distributions
    2. Visualize relationship between variables
    3. Calculate statistics with NaN present
    4. Remove NaN rows and recalculate
    5. Compare results to show impact of data quality
    """
    print("\n" + "="*80)
    print("COMPLETE EXERCISE 3 SEQUENCE")
    print("="*80)
    print("Data Visualization and Statistical Analysis with NaN Handling")
    
    print("\n" + "█"*80)
    print("STEP 1: Load Data and Visualize Distributions")
    print("█"*80)
    meta_score_1, user_review_1 = exercise_3_part_a()
    
    print("\n" + "█"*80)
    print("STEP 2: Visualize Relationship Between Variables")
    print("█"*80)
    meta_score_2, user_review_2 = exercise_3_part_b()
    
    print("\n" + "█"*80)
    print("STEP 3: Statistical Analysis (With and Without NaN)")
    print("█"*80)
    clean_data, stats = exercise_3_part_c()
    meta_mean, meta_std, user_mean, user_std = stats
    
    # Summary
    print("\n" + "="*80)
    print("EXERCISE 3 SUMMARY")
    print("="*80)
    print("""
✅ PART A - Distribution Visualization:
   - Created histograms with KDE overlay for meta_score and user_review
   - Used box plots to compare score ranges
   - Applied violin plots to visualize distribution shapes
   - Identified data spread and central tendencies

✅ PART B - Relationship Visualization:
   - Created scatter plot with regression line to show correlation
   - Calculated Pearson correlation coefficient
   - Used 2D density plot (hexbin) to show point concentration
   - Interpreted strength and direction of relationship

✅ PART C - Statistical Analysis:
   - Calculated mean and std with NaN values present (using nanmean, nanstd)
   - Removed rows with NaN using: a[~np.isnan(a).any(axis=1)]
   - Recalculated statistics on clean data
   - Compared results to show impact of missing data
   - Created visual comparison of statistics

KEY CONCEPTS LEARNED:
- Data visualization for exploratory data analysis (EDA)
- Histogram and distribution interpretation
- Scatter plots for relationship analysis
- Correlation coefficient (Pearson r)
- NaN-aware statistical functions (nanmean, nanstd)
- Boolean indexing for data cleaning
- Impact of missing data on statistical measures
- Data quality assessment and cleaning

FUNCTIONS AND TECHNIQUES DEMONSTRATED:
np.genfromtxt()          - Load CSV data with missing value handling
sns.histplot()           - Enhanced histograms with KDE
plt.boxplot()            - Box plot visualization
plt.violinplot()         - Violin plot for distribution shape
np.corrcoef()            - Calculate correlation coefficient
plt.hexbin()             - 2D density plot
np.nanmean() / np.nanstd() - Statistics ignoring NaN
np.polyfit()             - Fit regression line
np.isnan().any(axis=1)   - Remove rows with any NaN
plt.scatter()            - Scatter plot
np.polyfit() / np.poly1d() - Create and plot trend line

VISUALIZATIONS CREATED:
- exercise_3_distributions.png: Histograms, box plot, violin plot
- exercise_3_relationship.png: Scatter plot, regression line, 2D density
- exercise_3_statistics.png: Mean and std comparison charts

DATA QUALITY INSIGHTS:
- Identified NaN patterns in meta_score and user_review
- Quantified impact of missing data on mean and std dev
- Demonstrated that clean data provides more reliable statistics
- Showed relationship between two variables (correlation)
- Provided visual evidence for data exploration decisions

PRACTICAL APPLICATIONS:
- Exploratory Data Analysis (EDA) in real-world projects
- Data quality assessment before modeling
- Feature correlation analysis for machine learning
- Report generation with informative visualizations
- Statistical foundation for hypothesis testing
""")
    
    print("\n✅ Exercise 3 completed successfully!")
    print(f"\nFinal Statistics (Clean Data):")
    print(f"Meta Score - Mean: {meta_mean:.4f}, Std: {meta_std:.4f}")
    print(f"User Review - Mean: {user_mean:.4f}, Std: {user_std:.4f}")


if __name__ == "__main__":
    # Run complete sequence
    complete_exercise_sequence()
