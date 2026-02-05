# Week 4 Seminar - Diamonds Dataset Exercise
# This script analyzes the diamonds dataset from seaborn
# Explores relationships between diamond features (carat, cut, color, clarity) and price

# Import required libraries
import seaborn as sns  # For loading dataset and creating visualizations
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For plotting and customization


def load_and_display_diamonds_data():
	"""Load the diamonds dataset and display basic information."""
	# Load the diamonds dataset from seaborn's built-in datasets
	# This dataset contains information about ~54,000 diamonds
	diamonds_df = sns.load_dataset("diamonds")
	
	# Display basic information about the dataset
	print("Diamonds Dataset Shape:", diamonds_df.shape)
	print("\nFirst 5 rows:")
	print(diamonds_df.head())
	
	# Display data types and non-null counts
	print("\nDataset Info:")
	print(diamonds_df.info())
	
	# Display statistical summary of numerical features
	print("\nStatistical Summary:")
	print(diamonds_df.describe())
	
	# Display value counts for categorical features
	print("\nCut Distribution:")
	print(diamonds_df["cut"].value_counts())
	
	print("\nColor Distribution:")
	print(diamonds_df["color"].value_counts())
	
	print("\nClarity Distribution:")
	print(diamonds_df["clarity"].value_counts())
	
	return diamonds_df


def plot_scatter_price_vs_carat(diamonds_df):
	"""Create a scatter plot of price vs. carat, differentiated by cut."""
	# Create a large figure for better visibility
	plt.figure(figsize=(14, 8))
	
	# sns.scatterplot() creates a scatter plot with multiple parameters:
	# data: The DataFrame to plot from
	# x: Feature on x-axis (carat - weight of the diamond)
	# y: Feature on y-axis (price in US dollars)
	# hue: Color points by cut quality to see how cut affects price
	# palette: Color scheme for different cut qualities
	# s: Size of the markers (50 = medium)
	# alpha: Transparency level (0.6 = 60% opaque for better overlap visibility)
	# edgecolor: Border color for each point
	# linewidth: Thickness of point borders
	sns.scatterplot(
		data=diamonds_df,
		x="carat",
		y="price",
		hue="cut",
		palette="viridis",
		s=50,
		alpha=0.6,
		edgecolor=None,
		linewidth=0
	)
	
	# Add title and axis labels
	plt.title("Diamond Price vs. Carat by Cut Quality", 
			  fontsize=16, fontweight="bold", pad=20)
	plt.xlabel("Carat (Weight)", fontsize=13, fontweight="bold")
	plt.ylabel("Price (USD)", fontsize=13, fontweight="bold")
	
	# Add grid for easier reading of values
	plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
	
	# Add legend with better positioning
	plt.legend(title="Cut Quality", title_fontsize=12, fontsize=11, loc="upper left")
	
	# Adjust layout
	plt.tight_layout()
	
	# Save the figure
	plt.savefig("scatter_price_vs_carat_by_cut.png", dpi=300, bbox_inches='tight')
	print("\nSaved: scatter_price_vs_carat_by_cut.png")
	
	# Display the scatter plot
	plt.show()


def explore_price_factors(diamonds_df):
	"""Explore other factors affecting the price of diamonds."""
	
	# Create a figure with multiple subplots to explore different factors
	fig, axes = plt.subplots(2, 2, figsize=(16, 12))
	
	# 1. Box plot: Price by Cut
	# Box plots show distribution and outliers
	sns.boxplot(data=diamonds_df, x="cut", y="price", palette="Set2", ax=axes[0, 0])
	axes[0, 0].set_title("Price Distribution by Cut Quality", fontsize=14, fontweight="bold")
	axes[0, 0].set_xlabel("Cut Quality", fontsize=12, fontweight="bold")
	axes[0, 0].set_ylabel("Price (USD)", fontsize=12, fontweight="bold")
	axes[0, 0].grid(True, alpha=0.3, linestyle='--', axis='y')
	
	# 2. Box plot: Price by Color
	# Color grades from D (best) to J (worst)
	sns.boxplot(data=diamonds_df, x="color", y="price", palette="coolwarm", ax=axes[0, 1])
	axes[0, 1].set_title("Price Distribution by Color Grade", fontsize=14, fontweight="bold")
	axes[0, 1].set_xlabel("Color Grade (D=Best, J=Worst)", fontsize=12, fontweight="bold")
	axes[0, 1].set_ylabel("Price (USD)", fontsize=12, fontweight="bold")
	axes[0, 1].grid(True, alpha=0.3, linestyle='--', axis='y')
	
	# 3. Box plot: Price by Clarity
	# Clarity grades from IF (best) to I1 (worst)
	sns.boxplot(data=diamonds_df, x="clarity", y="price", palette="plasma", ax=axes[1, 0])
	axes[1, 0].set_title("Price Distribution by Clarity Grade", fontsize=14, fontweight="bold")
	axes[1, 0].set_xlabel("Clarity Grade", fontsize=12, fontweight="bold")
	axes[1, 0].set_ylabel("Price (USD)", fontsize=12, fontweight="bold")
	axes[1, 0].tick_params(axis='x', rotation=45)
	axes[1, 0].grid(True, alpha=0.3, linestyle='--', axis='y')
	
	# 4. Correlation heatmap: Numerical features
	# Select only numerical columns for correlation analysis
	numerical_cols = diamonds_df.select_dtypes(include=['float64', 'int64']).columns
	correlation_matrix = diamonds_df[numerical_cols].corr()
	
	# Create heatmap showing correlation between numerical features
	# annot=True displays correlation values in each cell
	# fmt='.2f' formats numbers to 2 decimal places
	# cmap='coolwarm' uses blue-white-red color scheme
	sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
				square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=axes[1, 1])
	axes[1, 1].set_title("Correlation Matrix of Numerical Features", 
						 fontsize=14, fontweight="bold")
	
	# Adjust layout to prevent overlap
	plt.tight_layout()
	
	# Save the figure
	plt.savefig("price_factors_analysis.png", dpi=300, bbox_inches='tight')
	print("Saved: price_factors_analysis.png")
	
	# Display the plots
	plt.show()
	
	# Print detailed analysis
	print("\n" + "="*70)
	print("ANALYSIS: Factors Affecting Diamond Price")
	print("="*70)
	
	# Calculate correlation with price
	numerical_cols = diamonds_df.select_dtypes(include=['float64', 'int64']).columns
	price_correlation = diamonds_df[numerical_cols].corr()['price'].sort_values(ascending=False)
	
	print("\nCorrelation with Price (strongest to weakest):")
	print(price_correlation)
	
	# Calculate average price by categorical features
	print("\n" + "-"*70)
	print("Average Price by Cut Quality:")
	print("-"*70)
	print(diamonds_df.groupby('cut')['price'].agg(['mean', 'median', 'min', 'max']).round(2))
	
	print("\n" + "-"*70)
	print("Average Price by Color Grade:")
	print("-"*70)
	print(diamonds_df.groupby('color')['price'].agg(['mean', 'median', 'min', 'max']).round(2))
	
	print("\n" + "-"*70)
	print("Average Price by Clarity Grade:")
	print("-"*70)
	print(diamonds_df.groupby('clarity')['price'].agg(['mean', 'median', 'min', 'max']).round(2))
	
	print("\n" + "="*70)
	print("KEY FINDINGS:")
	print("="*70)
	print("1. CARAT (Weight): Strongest predictor of price (correlation: ~0.92)")
	print("   • Larger diamonds are significantly more expensive")
	print("   • Exponential relationship between carat and price")
	print("\n2. DIMENSIONS (x, y, z): High correlation with price (~0.88)")
	print("   • Larger physical dimensions correlate with higher carat")
	print("   • Strong positive relationship with price")
	print("\n3. CUT QUALITY: Surprisingly, better cut doesn't always mean higher price")
	print("   • Ideal cuts have lower average price than Premium cuts")
	print("   • This is because cut interacts with other factors (carat, clarity)")
	print("\n4. COLOR: Better color (D) generally commands higher prices")
	print("   • Clear gradient from D (colorless) to J (light color)")
	print("\n5. CLARITY: Better clarity generally means higher price")
	print("   • IF (Internally Flawless) commands premium prices")
	print("   • But carat weight often dominates over clarity")
	print("\n6. CONCLUSION:")
	print("   • Carat is the most important factor determining price")
	print("   • Physical dimensions closely follow carat importance")
	print("   • Quality factors (cut, color, clarity) matter but are secondary")
	print("   • Interaction effects: large diamonds with poor quality can cost")
	print("     more than small diamonds with excellent quality")
	print("="*70)


def main():
	"""Main function to orchestrate the diamonds dataset analysis."""
	print("="*70)
	print("DIAMONDS DATASET ANALYSIS")
	print("="*70)
	
	# Load and display dataset information
	diamonds_df = load_and_display_diamonds_data()
	
	# Create scatter plot of price vs carat by cut
	print("\nGenerating scatter plot: Price vs. Carat by Cut...")
	plot_scatter_price_vs_carat(diamonds_df)
	
	# Explore other factors affecting price
	print("\nExploring other factors affecting diamond price...")
	explore_price_factors(diamonds_df)
	
	print("\n" + "="*70)
	print("Analysis complete! All visualizations saved.")
	print("="*70)


if __name__ == "__main__":
	main()
