# Week 4 Seminar - Iris Dataset Exercise
# Load and analyze the Iris dataset using seaborn and pandas
# The Iris dataset is a classic dataset containing 150 flower measurements

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def load_and_display_iris_data():
	"""Load the Iris dataset and display basic information."""
	# Load the Iris dataset from seaborn's built-in datasets
	# sns.load_dataset() downloads and caches datasets from the seaborn-data repository
	# Returns a pandas DataFrame with 150 rows and 5 columns
	iris_df = sns.load_dataset("iris")
	
	# Display the shape of the dataset
	# shape returns a tuple (rows, columns) showing dataset dimensions
	print("Iris Dataset Shape:", iris_df.shape)
	
	# Display the first 5 rows of the dataset
	# head() is a pandas method that returns the first n rows (default is 5)
	# Useful for quickly inspecting the data structure
	print("\nFirst 5 rows:")
	print(iris_df.head())
	
	# Display comprehensive information about the dataset
	# info() shows column names, non-null counts, and data types
	# Useful for identifying missing values and data type issues
	print("\nDataset Info:")
	print(iris_df.info())
	
	# Display statistical summary of numerical columns
	# describe() calculates count, mean, std, min, 25%, 50%, 75%, max
	# Provides quick insight into data distribution and range
	print("\nStatistical Summary:")
	print(iris_df.describe())
	
	# Count occurrences of each unique species
	# value_counts() returns a series with counts of each unique value
	# Useful for understanding categorical data distribution
	print("\nSpecies Distribution:")
	print(iris_df["species"].value_counts())
	
	return iris_df


def plot_histogram_by_species(iris_df):
	"""Create a histogram of sepal_length colored by species."""
	# Create a histogram of sepal_length to visualize distribution
	# plt.figure() creates a new figure with specified size (width, height)
	plt.figure(figsize=(12, 7))
	
	# sns.histplot() creates an enhanced histogram with multiple parameters:
	# data: The DataFrame to plot from
	# x: The column to plot (sepal_length)
	# hue: Color the bars by species to see distribution per category
	# kde: Overlay a kernel density estimate curve for smoothed distribution
	# bins: Number of bins/bars (30 for finer detail)
	# multiple: How to handle overlapping data - "layer" stacks them semi-transparently
	# palette: Color scheme for different species
	# edgecolor: Border color for bars
	# alpha: Transparency level (0.6 = 60% opaque)
	# stat: Display 'density' instead of count for better comparison
	sns.histplot(
		data=iris_df, 
		x="sepal_length",
		hue="species",
		kde=True, 
		bins=30,
		multiple="layer",
		palette="Set2",
		edgecolor="black",
		alpha=0.6,
		stat="density",
		linewidth=1.5
	)
	
	# Add detailed title and axis labels with grid for better readability
	plt.title("Distribution of Sepal Length by Species in Iris Dataset", 
			  fontsize=16, fontweight="bold", pad=20)
	plt.xlabel("Sepal Length (cm)", fontsize=13, fontweight="bold")
	plt.ylabel("Density", fontsize=13, fontweight="bold")
	
	# Add grid for easier reading of values
	plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
	
	# Add legend with better positioning
	plt.legend(title="Species", title_fontsize=12, fontsize=11, loc="upper right")
	
	# Adjust layout to prevent label cutoff
	plt.tight_layout()
	
	# Save the figure
	plt.savefig("histogram_sepal_length_by_species.png", dpi=300, bbox_inches='tight')
	print("Saved: histogram_sepal_length_by_species.png")
	
	# Display the plot
	# show() renders the plot window
	plt.show()


def plot_general_histogram(iris_df):
	"""Create a general histogram of sepal_length (all species combined)."""
	# This shows the overall distribution without breaking down by species
	plt.figure(figsize=(10, 6))
	
	# sns.histplot() with no hue parameter treats all data as one group
	# color: Single color for all bars
	# kde: Kernel density estimate curve shows smoothed distribution
	# bins: Number of bars (25 for moderate detail)
	# stat: 'density' normalizes the histogram for probability distribution
	sns.histplot(
		data=iris_df,
		x="sepal_length",
		color="steelblue",
		kde=True,
		bins=25,
		edgecolor="black",
		alpha=0.7,
		stat="density",
		linewidth=1.2
	)
	
	# Add title and labels
	plt.title("Overall Distribution of Sepal Length (All Species Combined)", 
			  fontsize=15, fontweight="bold", pad=15)
	plt.xlabel("Sepal Length (cm)", fontsize=12, fontweight="bold")
	plt.ylabel("Density", fontsize=12, fontweight="bold")
	
	# Add grid for readability
	plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
	
	# Adjust layout
	plt.tight_layout()
	
	# Save the figure
	plt.savefig("histogram_sepal_length_general.png", dpi=300, bbox_inches='tight')
	print("Saved: histogram_sepal_length_general.png")
	
	# Display the general histogram
	plt.show()


def plot_scatter_sepal_vs_petal(iris_df):
	"""Create a scatter plot of sepal_length vs petal_length to distinguish species."""
	# Create a scatter plot to visualize the relationship between two features
	plt.figure(figsize=(12, 8))
	
	# sns.scatterplot() creates a scatter plot with multiple parameters:
	# data: The DataFrame to plot from
	# x: Feature on x-axis (sepal_length)
	# y: Feature on y-axis (petal_length)
	# hue: Color points by species to see separation between groups
	# palette: Color scheme for different species
	# s: Size of the markers (100 = medium-large)
	# alpha: Transparency level (0.7 = 70% opaque for better overlap visibility)
	# edgecolor: Border color for each point
	# linewidth: Thickness of point borders
	sns.scatterplot(
		data=iris_df,
		x="sepal_length",
		y="petal_length",
		hue="species",
		palette="Set1",
		s=100,
		alpha=0.7,
		edgecolor="black",
		linewidth=0.5
	)
	
	# Add title and axis labels
	plt.title("Scatter Plot: Sepal Length vs Petal Length by Species", 
			  fontsize=16, fontweight="bold", pad=20)
	plt.xlabel("Sepal Length (cm)", fontsize=13, fontweight="bold")
	plt.ylabel("Petal Length (cm)", fontsize=13, fontweight="bold")
	
	# Add grid for easier reading of values
	plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
	
	# Add legend with better positioning
	plt.legend(title="Species", title_fontsize=12, fontsize=11, loc="upper left")
	
	# Adjust layout
	plt.tight_layout()
	
	# Save the figure
	plt.savefig("scatter_sepal_length_vs_petal_length.png", dpi=300, bbox_inches='tight')
	print("Saved: scatter_sepal_length_vs_petal_length.png")
	
	# Display the scatter plot
	plt.show()
	
	# Provide analysis insights
	print("\n" + "="*70)
	print("ANALYSIS: Species Distinction by Sepal Length vs Petal Length")
	print("="*70)
	
	# Calculate statistics for each species
	for species in iris_df["species"].unique():
		species_data = iris_df[iris_df["species"] == species]
		print(f"\n{species.capitalize()}:")
		print(f"  Sepal Length - Mean: {species_data['sepal_length'].mean():.2f} cm, "
			  f"Range: [{species_data['sepal_length'].min():.2f} - {species_data['sepal_length'].max():.2f}]")
		print(f"  Petal Length - Mean: {species_data['petal_length'].mean():.2f} cm, "
			  f"Range: [{species_data['petal_length'].min():.2f} - {species_data['petal_length'].max():.2f}]")
	
	print("\n" + "-"*70)
	print("KEY FINDINGS:")
	print("-"*70)
	print("1. SETOSA: Clearly separated - shortest petal length (1-2 cm)")
	print("   • Forms a distinct cluster in the lower-left region")
	print("   • Easily distinguishable from other species")
	print("\n2. VERSICOLOR: Intermediate values")
	print("   • Petal length: 3-5 cm, Sepal length: 5-7 cm")
	print("   • Some overlap with Virginica")
	print("\n3. VIRGINICA: Longest measurements")
	print("   • Petal length: 4.5-7 cm, Sepal length: 6-8 cm")
	print("   • Upper-right region of the plot")
	print("   • Slight overlap with Versicolor")
	print("\n4. CONCLUSION:")
	print("   • Petal length is MORE distinctive than sepal length")
	print("   • These two features together provide good species separation")
	print("   • Setosa is perfectly separable; Versicolor and Virginica have")
	print("     minor overlap but are still largely distinguishable")
	print("="*70)


def main() -> None:
	"""Main function to run all analysis and visualizations."""
	# Load and display basic dataset information
	iris_df = load_and_display_iris_data()
	
	# Create histogram by species
	print("\nGenerating histogram by species...")
	plot_histogram_by_species(iris_df)
	
	# Create general histogram
	print("Generating general histogram...")
	plot_general_histogram(iris_df)
	
	# Create scatter plot
	print("\nGenerating scatter plot of sepal_length vs petal_length...")
	plot_scatter_sepal_vs_petal(iris_df)


if __name__ == "__main__":
	main()
