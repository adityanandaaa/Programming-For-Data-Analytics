# Programming for Data Analytics

A comprehensive Python project for data analysis, visualization, and reporting using modern data science tools.

## 🚀 Quick Start

```bash
# Navigate to project
cd Programming_for_Data_Analytics

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run analysis examples
python main.py
```

## 📊 Project Structure

```
Programming_for_Data_Analytics/
├── data/                    # Data files and datasets
│   ├── raw/                # Raw data inputs
│   └── processed/          # Processed data outputs
├── src/                    # Source code
│   ├── analytics/         # Analysis modules
│   ├── visualization/     # Plotting and charts
│   └── utils/            # Utility functions
├── notebooks/            # Jupyter notebooks
├── reports/              # Generated reports and visualizations
├── tests/                # Unit tests
├── Week 3 Seminar/       # Week 3 seminar exercises (API & web scraping)
├── Week 4 Seminar/       # Week 4 seminar exercises (data visualization)
│   ├── data/             # Datasets for Week 4
│   ├── irisdataset exercise/        # Iris dataset analysis
│   ├── diamonds dataset exercise/   # Diamonds dataset analysis
│   └── penguins dataset exercise/   # Penguins dataset EDA
├── Week 5 Seminar/       # Week 5 seminar exercises (NumPy fundamentals)
│   ├── introduction_week_5_numpy.py  # NumPy basics introduction
│   ├── exercise_1_week_5.py          # NumPy array manipulation
│   ├── exercise_2_week_5.py          # CSV loading with data cleaning
│   ├── tips.csv          # Restaurant tips dataset
│   ├── all_games.csv     # Video games dataset (18,802 records)
│   └── tips.npy          # Binary NumPy format example
├── requirements.txt      # Project dependencies
├── main.py              # Main entry point
└── README.md            # This file
```

## 📖 Week 3 Seminar

The **Week 3 Seminar** folder contains exercises focused on **API integration and web scraping** with two different approaches.

### Exercise 1: Open Library JSON API

**File**: `Week 3 Seminar/exercise_week_3_seminar.py`

This exercise demonstrates how to:
- Make HTTP requests to the Open Library JSON API (`https://openlibrary.org/search.json`)
- Use API parameters for searching and pagination:
  - `q`: Search query (keyword or title)
  - `fields`: Specify which fields to retrieve (title, author_name, etc.)
  - `page`: Pagination parameter to fetch multiple pages of results
- Parse JSON responses programmatically
- Process and format retrieved data
- Write results to a text file with page separators

**Example Usage**:
```bash
cd "Week 3 Seminar"
python exercise_week_3_seminar.py
```

**Output**: 
- Console display of 300 results (100 per page × 3 pages) for "Data Science" books
- Saves formatted results to `data_science_results.txt` with clear page markers

### Exercise 2: Open Library HTML Scraping with BeautifulSoup

**File**: `Week 3 Seminar/exercise_week_3_seminar_bs4.py`

This exercise demonstrates how to:
- Fetch HTML pages from Open Library web interface (`https://openlibrary.org/search`)
- Parse HTML structure using BeautifulSoup4
- Extract data from specific HTML elements:
  - Book titles from `div.resultTitle`
  - Authors from `span.bookauthor` anchor tags
- Handle multiple author names
- Scrape across multiple pages with pagination

**Example Usage**:
```bash
cd "Week 3 Seminar"
python exercise_week_3_seminar_bs4.py
```

**Output**: 
- Console display of 60 results (20 per page × 3 pages) for "data science" books
- Saves formatted results to `data_science_results_bs4.txt` with clear page markers

### Comparison: JSON API vs Web Scraping

| Aspect | JSON API | BeautifulSoup (HTML) |
|--------|----------|---------------------|
| **Results per page** | 100 | 20 |
| **Total results (3 pages)** | 300 | 60 |
| **Data format** | JSON | HTML |
| **Parsing method** | `json.loads()` | BeautifulSoup |
| **Dependencies** | Built-in libraries | `beautifulsoup4` |
| **Speed** | Faster (smaller payload) | Slower (larger HTML) |
| **Reliability** | High (structured data) | Medium (depends on HTML structure) |
| **Best for** | Programmatic access | When API unavailable |

**Key Learnings**:
- RESTful API concepts and HTTP requests
- URL encoding and parameter management
- JSON vs HTML parsing techniques
- Web scraping with BeautifulSoup
- Pagination for large result sets
- File I/O operations
- Comparing API and scraping approaches

---

## 📊 Week 4 Seminar

The **Week 4 Seminar** folder contains exercises focused on **data visualization and exploratory data analysis** using Seaborn and Matplotlib with real-world datasets.

### Exercise 1: Iris Dataset Analysis

**Folder**: `Week 4 Seminar/irisdataset exercise/`  
**File**: `exercise_iris_dataset_week_4.py`

This exercise explores the classic **Iris dataset** (150 flower measurements) with comprehensive visualizations:

#### Features Analyzed:
- **Sepal Length** and **Sepal Width**
- **Petal Length** and **Petal Width**
- **Species**: setosa, versicolor, virginica (50 samples each)

#### Visualizations Created:
1. **Histogram by Species** (`histogram_sepal_length_by_species.png`)
   - Distribution of sepal length colored by species
   - Layered histograms with KDE curves
   - Shows clear separation between species

2. **General Histogram** (`histogram_sepal_length_general.png`)
   - Overall distribution without species breakdown
   - Displays aggregate patterns across all flowers

3. **Scatter Plot** (`scatter_sepal_length_vs_petal_length.png`)
   - Relationship between sepal length and petal length
   - Color-coded by species to show clustering
   - Reveals how features distinguish species

#### Key Functions:
```python
load_and_display_iris_data()       # Load dataset and show statistics
plot_histogram_by_species()         # Create species-colored histogram
plot_general_histogram()            # Create overall histogram
plot_scatter_sepal_vs_petal()      # Create scatter plot analysis
```

#### Key Findings:
- **Setosa**: Clearly separated with shortest petal length (1-2 cm)
- **Versicolor**: Intermediate values with some overlap with Virginica
- **Virginica**: Longest measurements (petal length 4.5-7 cm)
- **Petal length** is more distinctive than sepal length for classification
- Species form distinct clusters in 2D feature space

**Technologies Used**: Seaborn (high-level statistical plots), Matplotlib (customization), Pandas (data analysis)

---

### Exercise 2: Diamonds Dataset Analysis

**Folder**: `Week 4 Seminar/diamonds dataset exercise/`  
**File**: `exercise_diamonds_dataset_week_4.py`

This exercise analyzes the **Diamonds dataset** (53,940 diamonds) to understand price determinants:

#### Features Analyzed:
- **Carat**: Diamond weight (0.2-5.01 carats)
- **Cut**: Quality levels (Fair, Good, Very Good, Premium, Ideal)
- **Color**: Grades D (best) to J (worst)
- **Clarity**: Grades IF (best) to I1 (worst)
- **Dimensions**: x, y, z (length, width, depth in mm)
- **Price**: USD ($326-$18,823)

#### Visualizations Created:
1. **Scatter Plot: Price vs Carat** (`scatter_price_vs_carat_by_cut.png`)
   - Shows exponential relationship between carat and price
   - Color-coded by cut quality
   - Reveals that carat dominates pricing

2. **Price Factors Analysis** (`price_factors_analysis.png`)
   - **Box plots** showing price distribution by cut, color, and clarity
   - **Correlation heatmap** of numerical features
   - Multi-panel layout for comprehensive comparison

#### Key Functions:
```python
load_and_display_diamonds_data()    # Load dataset and show statistics
plot_scatter_price_vs_carat()       # Price vs carat scatter plot
explore_price_factors()             # Comprehensive factor analysis
```

#### Key Findings:
1. **Carat (Weight)**: Strongest price predictor (correlation: 0.92)
   - Exponential relationship with price
   - Larger diamonds exponentially more expensive

2. **Dimensions (x, y, z)**: High correlation with price (~0.88)
   - Directly related to carat weight

3. **Cut Quality**: Counter-intuitive results
   - Ideal cuts have *lower* average price than Premium
   - Interaction effects with other factors

4. **Color**: D (colorless) commands premium prices
   - Clear gradient from D to J

5. **Clarity**: IF (Internally Flawless) most expensive
   - But carat weight dominates over clarity

6. **Interaction Effects**: Large diamonds with poor quality can cost more than small diamonds with excellent quality

**Technologies Used**: Seaborn (box plots, scatter plots, heatmaps), Matplotlib (subplots, customization), Pandas (groupby, aggregation)

---

### Week 4 Learning Outcomes

- **Data Loading**: Using `sns.load_dataset()` for built-in datasets
- **Exploratory Data Analysis**: `.shape`, `.info()`, `.describe()`, `.value_counts()`
- **Histogram Visualization**: Distribution analysis with `sns.histplot()`
- **Scatter Plots**: Relationship analysis with `sns.scatterplot()`
- **Box Plots**: Distribution comparison with `sns.boxplot()`
- **Correlation Analysis**: Heatmaps with `sns.heatmap()`
- **Multi-panel Layouts**: Using `plt.subplots()` for complex visualizations
- **Statistical Insights**: Groupby operations and aggregation
- **Plot Customization**: Titles, labels, legends, grids, color palettes
- **Saving Figures**: High-resolution PNG exports with `plt.savefig()`

### Seaborn vs Matplotlib

| Aspect | Seaborn | Matplotlib |
|--------|---------|------------|
| **Level** | High-level statistical | Low-level plotting |
| **Ease of Use** | Simple, concise | More verbose |
| **Default Styling** | Beautiful defaults | Basic defaults |
| **Statistical Plots** | Built-in (hist, scatter, box) | Requires more code |
| **DataFrame Integration** | Native support | Manual handling |
| **Customization** | Less control | Full control |
| **Best For** | Statistical visualization | Custom plots |

**In practice**: Use Seaborn for creating plots quickly with beautiful defaults, then use Matplotlib for fine-tuning (titles, grids, saving).

---

### Exercise 3: Penguins Dataset - Comprehensive EDA

**Folder**: `Week 4 Seminar/penguins dataset exercise/`  
**File**: `exercise_penguins_dataset_week_4.py`

This exercise performs comprehensive **Exploratory Data Analysis (EDA)** on the **Penguins dataset** (344 penguin observations) to demonstrate data quality assessment, visualization techniques, and actionable preprocessing recommendations.

#### Dataset Overview:
- **344 observations** across 3 Antarctic penguin species
- **7 features**: species, island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex
- **3 species**: Adelie (152), Gentoo (124), Chinstrap (68)
- **Missing values**: 2 numeric (0.58%), 11 sex values (3.2%)
- **Target**: Classification (species prediction) with sex as secondary predictor

#### Visualizations Created (4 Plots):

1. **PLOT 1: Missing Values Heatmap** (`plot_1_missing_values_heatmap.png`)
   - Visualizes data completeness across all variables
   - Shows scattered missing values (not systematic)
   - Identifies sex as most problematic variable (11 missing)
   - **Insight**: Manageable missingness - can drop rows or impute

2. **PLOT 2: Numeric Distributions - Species × Sex Analysis** (`plot_2_numeric_distributions.png`)
   - **Layout**: 4×3 grid (4 numeric features × 3 species)
   - **Feature rows**: Bill Length | Bill Depth | Flipper Length | Body Mass
   - **Species columns**: Adelie | Chinstrap | Gentoo
   - **Visualization**: Dual overlaid histograms (Male: blue, Female: red) + KDE curves
   - **Enhancements**: Added sex granularity showing sexual dimorphism within each species
   - **Key insights**:
     - Species-specific distributions clearly separated
     - Males consistently larger across all measurements (3-4mm bills, 300-500g mass)
     - Adelie: Deepest, most compact bills; lightest body mass
     - Chinstrap: Longest bills (>50mm) - diagnostic feature
     - Gentoo: Shallowest bills, longest flippers, heaviest bodies
     - Gentoo body mass shows right skew

3. **PLOT 3: Species Relationships with Sex Analysis** (`plot_3_species_relationships.png`)
   - **Layout**: 2×2 grid (4 complementary views)
   - **Subplot 1**: Scatter plot (Bill Length vs Flipper Length) colored by species
   - **Subplot 2**: Same scatter but colored by sex, shaped by species (shows sexual dimorphism)
   - **Subplot 3**: Box plot of Body Mass by species × sex combinations
   - **Subplot 4**: Violin plot (split by sex) showing Bill Length distributions
   - **Key insights**:
     - Nearly perfect species separability (minimal overlap)
     - Sex-species interaction: 6 distinct populations (3 species × 2 sexes)
     - Sexual dimorphism: ~300-400g mass difference
     - Classification potential: Species ~99% separable; Sex detectable within species

4. **PLOT 4: Correlation Analysis** (`plot_4_correlation_analysis.png`)
   - **Correlation Heatmap**: Shows numeric feature relationships
   - **Violin Plot**: Bill depth distribution across species
   - **Key correlations**:
     - Flipper length ↔ Body mass: 0.871 (strong multicollinearity)
     - Bill length ↔ Flipper length: 0.656 (moderate)
     - Bill depth ↔ Bill length: -0.235 (inverse, trade-off)
     - Bill depth ↔ Flipper length: -0.584 (inverse, species-dependent)

#### Key Functions:
```python
load_and_display_penguins_data()        # Load dataset, show stats and missing values
plot_missing_values_analysis()          # PLOT 1: Missing values heatmap
plot_distributions_numeric_features()  # PLOT 2: Species × sex distributions
plot_species_relationships()            # PLOT 3: Species/sex relationships
plot_correlation_analysis()             # PLOT 4: Correlation matrix + violin plots
generate_eda_summary()                  # Comprehensive preprocessing recommendations
```

#### Comprehensive EDA Summary Output:
The script generates a detailed **7-section EDA summary** with actionable recommendations:

1. **Data Quality & Missingness Handling**
   - Drop incomplete rows (recommended) or use KNN imputation
   - Results in 333 complete observations

2. **Feature Distributions & Transformations**
   - Log transform for body_mass_g (right-skewed)
   - StandardScaler for all numeric features

3. **Categorical Encoding & Class Balance**
   - One-hot encoding for species/island/sex
   - Manageable class imbalance (2.2:1 ratio)

4. **Outliers & Anomalies**
   - All outliers are legitimate biological variations
   - No erroneous measurements detected

5. **Feature Engineering & Selection**
   - Create interaction features: bill_ratio, size_index, mass_efficiency
   - Manage multicollinearity (flipper_length & body_mass)
   - Different strategies for linear vs tree-based models

6. **Complete Preprocessing Pipeline**
   - Drop missing values → Scale numerics → Encode categoricals
   - Integrated with scikit-learn Pipeline

7. **Model Development Guidance**
   - Expected accuracy: >95% (features highly discriminative)
   - Recommended models: Logistic Regression, Random Forest, XGBoost
   - Classification should be nearly perfect (species nearly separable)

#### Technologies Used:
- **Seaborn**: Statistical plotting, KDE curves, multi-plot coordination
- **Matplotlib**: Subplots, customization, figure saving (300 DPI PNG)
- **Pandas**: Data loading, groupby, missing value analysis
- **NumPy**: Numerical operations
- **SciPy**: Kernel Density Estimation (gaussian_kde)

#### Key Findings:

| Aspect | Finding |
|--------|---------|
| **Species Separability** | Nearly perfect (>99% discriminative) |
| **Primary Predictor** | Bill morphology (length + depth + flipper) |
| **Secondary Predictor** | Sex (males consistently larger) |
| **Best Feature** | Flipper length (high correlation with body mass) |
| **Most Diagnostic** | Bill length for Chinstrap (>50mm threshold) |
| **Multicollinearity** | Flipper length ↔ Body mass (r=0.871) |
| **Transformation Needed** | Log scale for body_mass_g |
| **Missing Data Impact** | Low (<4%), manageable |
| **Expected ML Accuracy** | >95% (likely >97%) |

---

## 📊 Week 5 Seminar

The **Week 5 Seminar** folder contains exercises focused on **NumPy fundamentals** - the foundation library for numerical computing in Python.

### Introduction: NumPy Basics

**File**: `Week 5 Seminar/introduction_week_5_numpy.py`

This comprehensive introduction covers fundamental NumPy operations and demonstrates why NumPy is essential for data analysis and scientific computing.

#### Topics Covered:

1. **NumPy Array Basics**
   - Array creation with mixed types
   - Automatic type conversion
   - Understanding dtype (data types)

2. **Loading Data from Text Files**
   - `np.loadtxt()`: Fast loading for numeric data
     - Parameters: skiprows, usecols, max_rows, delimiter
   - `np.genfromtxt()`: Better handling of missing data
     - Column name support with `names=True`
   - Loading from `tips.csv` with different methods

3. **Binary File Operations**
   - `np.save()`: Save arrays in efficient .npy format
   - `np.load()`: Load binary NumPy files
   - Benefits: Faster I/O, preserves data types

4. **Array Shapes and Dimensions**
   - 1D arrays: `(n,)` shape
   - 2D arrays: `(rows, cols)` shape
   - 3D arrays: `(depth, rows, cols)` shape
   - Understanding multi-dimensional data structures

5. **Array Reshaping Operations**
   - `reshape()`: Returns view (no data copying)
   - `ravel()`: Flatten to 1D array
   - `resize()`: In-place modification
   - `transpose()` and `.T`: Swap axes
   - Memory efficiency considerations

6. **Computation Speed Differences**
   - **List addition**: Concatenation `[1,2,3] + [4,5,6] = [1,2,3,4,5,6]`
   - **NumPy addition**: Element-wise `[1,2,3] + [4,5,6] = [5,7,9]`
   - **Performance**: NumPy is **100-120x faster** than Python lists
   - Benchmark with 100,000 elements demonstrates dramatic speed advantage

7. **Array Broadcasting**
   - Operations between arrays of different shapes
   - Automatic dimension expansion
   - Example: `(2,3)` array × `(3,)` array = `(2,3)` result

8. **Creating Special Arrays**
   - `np.zeros()`: Array filled with zeros
   - `np.ones()`: Array filled with ones
   - `np.empty()`: Uninitialized array (faster but contains garbage values)
   - Specifying dtype for memory efficiency

9. **Array Indexing**
   - Single element: `array[1, 2, 3]` for 3D arrays
   - Slicing dimensions: `array[1, 2]` returns entire row
   - Full slice: `array[1]` returns 2D slice of 3D array

10. **Array Slicing Techniques**
    - Basic slicing: `array[start:end]`
    - Step parameter: `array[1:6:2]` (every 2nd element)
    - Multi-dimensional: `array[0:2, 0:2, 0:2]`
    - Index arrays: `array[i]` where i is array of indices

11. **Advanced Indexing**
    - **Fancy indexing**: `array[[2,4,5]]` select specific indices
    - **Boolean masking**: `array[array > 50]` filter by condition
    - **Multi-dimensional indexing**: `array[[0,1,2], [2,0,1]]` select specific elements

#### Performance Comparison:
```python
# Speed test with 100,000 elements (100 iterations):
NumPy array addition:    ~0.002 seconds
List comprehension:      ~0.270 seconds
Result: NumPy is 117x faster! 🚀
```

#### Key Functions Demonstrated:
```python
np.array()              # Create arrays
np.random.randint()     # Generate random integers
np.loadtxt()           # Load CSV data
np.genfromtxt()        # Load with missing value handling
np.save() / np.load()  # Binary file operations
array.reshape()        # Change array dimensions
array.ravel()          # Flatten array
array.transpose()      # Swap axes
np.zeros() / np.ones() # Special arrays
```

---

### Exercise 1: NumPy Array Manipulation

**File**: `Week 5 Seminar/exercise_1_week_5.py`

This exercise practices fundamental NumPy operations through a structured workflow of array creation, manipulation, filtering, and modification.

#### Exercise Questions:
1. Create a 2D array of 16 random integers between 0 and 100
2. Reshape the array into a 4×4 2D array
3. Extract the subarray consisting of the last two columns of first two rows
4. Find all numbers that are greater than 50 from the array
5. Replace these numbers with 0

#### Detailed Solutions:

**Question 1: Create Random Array**
```python
# Generate 16 random integers in range [0, 100]
array_1d = np.random.randint(0, 101, 16)  # 101 because upper bound is exclusive
# Result: [55, 6, 65, 69, 56, 33, 1, 70, 8, 13, 79, 81, 63, 74, 88, 40]
```

**Question 2: Reshape to 4×4**
```python
# Convert 1D array to 2D array (4 rows × 4 columns)
array_2d = array_1d.reshape(4, 4)
# Result:
# [[55,  6, 65, 69]
#  [56, 33,  1, 70]
#  [ 8, 13, 79, 81]
#  [63, 74, 88, 40]]
```

**Question 3: Extract Subarray**
```python
# Slice first 2 rows, last 2 columns
subarray = array_2d[0:2, 2:4]  # or array_2d[:2, -2:]
# Result:
# [[65, 69]
#  [ 1, 70]]
```

**Question 4: Find Values > 50**
```python
# Boolean masking creates True/False array
mask = array_2d > 50
numbers_gt_50 = array_2d[mask]
# Result: [55, 65, 69, 56, 70, 79, 81, 63, 74, 88]
# Count: 10 elements
```

**Question 5: Replace with 0**
```python
# In-place modification using boolean indexing
array_2d[mask] = 0
# Result:
# [[ 0,  6,  0,  0]
#  [ 0, 33,  1,  0]
#  [ 8, 13,  0,  0]
#  [ 0,  0,  0, 40]]
```

#### Concepts Demonstrated:
- **Random number generation**: `np.random.randint(low, high, size)`
- **Array reshaping**: `.reshape(rows, cols)` converts dimensions
- **Array slicing**: `[row_slice, col_slice]` extracts subarrays
- **Boolean masking**: Conditional filtering with `array > value`
- **In-place modification**: `array[mask] = new_value` efficient updates
- **Views vs copies**: Understanding memory efficiency

#### Exercise Structure:
The file contains two approaches:
1. **Part 1**: Individual demonstrations (separate arrays for each concept)
   - Part A: Create and reshape
   - Part B: Extract subarray
   - Part C: Find and replace
2. **Part 2**: Complete sequence (all operations on single array)
   - Shows full data processing pipeline
   - Demonstrates how operations chain together

#### Learning Outcomes:
✅ Understand NumPy array creation and random generation  
✅ Master array reshaping and dimension manipulation  
✅ Practice multi-dimensional slicing techniques  
✅ Apply boolean indexing for filtering  
✅ Perform efficient in-place array modifications  
✅ Recognize views vs copies for memory optimization

---

### Exercise 2: Loading CSV Data with Irregular Values

**File**: `Week 5 Seminar/exercise_2_week_5.py`

This exercise teaches practical data science skills by loading real-world CSV data with missing/irregular values and applying common data cleaning strategies.

#### Exercise Question:
Load the first 1000 records from `all_games.csv` into a NumPy array, selecting only the "meta_score" and "user_review" columns, and properly handle irregular data (e.g., "tbd" values).

#### Detailed Solutions:

**Part A: Data Loading**
```python
# Load CSV with irregular data handling
games_data = np.genfromtxt(
    csv_path,
    delimiter=',',           # CSV format
    skip_header=1,           # Skip header row
    usecols=[2, 3],          # Select meta_score (col 2) and user_review (col 3)
    max_rows=1000,           # Load first 1000 records
    filling_values=np.nan,   # Replace irregular values with NaN
    invalid_raise=False      # Don't raise error on non-numeric values
)
# Result: (1000, 2) array with 3 NaN values (0.15% missing)
```

**Key Data Characteristics:**
- CSV has 7 columns: name, platform, meta_score, user_review, year, month, day
- meta_score (column 2): Video game metadata score, mostly numeric with few missing values
- user_review (column 3): User review scores, sometimes contains "tbd" (to be determined)
- Total records in CSV: 18,802; Exercise loads first 1,000

**Part B: Statistical Analysis with Missing Values**
```python
# Use NaN-aware functions for statistics
print(f"Meta Score Mean: {np.nanmean(games_data[:, 0])}")        # 90.34
print(f"Meta Score Median: {np.nanmedian(games_data[:, 0])}")    # 90.00
print(f"User Review Mean: {np.nanmean(games_data[:, 1])}")       # 8.20
print(f"User Review Median: {np.nanmedian(games_data[:, 1])}")   # 8.30
```

**NaN-Aware Functions:**
- `np.nanmean()`: Mean excluding NaN values
- `np.nanmedian()`: Median excluding NaN values
- `np.nanstd()`: Standard deviation excluding NaN values
- `np.nanmin() / np.nanmax()`: Min/max excluding NaN values
- `np.isnan()`: Identify NaN values

**Part C: Data Cleaning Strategies**

**Strategy 1: Remove All Rows with Any NaN**
```python
# Create boolean mask for rows without NaN
clean_rows = ~np.any(np.isnan(games_data), axis=1)
cleaned_data = games_data[clean_rows]
# Result: 997 rows (3 rows removed)
# Advantage: Complete data, no missing values
# Disadvantage: Data loss
```

**Strategy 2: Remove Specific Column NaN Only**
```python
# Remove rows where user_review is missing
valid_rows = ~np.isnan(games_data[:, 1])
cleaned_data = games_data[valid_rows]
# Result: 998 rows (2 rows removed)
# Advantage: Keeps meta_score data even if user_review missing
# Disadvantage: Inconsistent column availability
```

**Strategy 3: Fill Missing Values with Column Mean**
```python
# Replace NaN with column mean
for col in range(games_data.shape[1]):
    col_mean = np.nanmean(games_data[:, col])
    games_data[np.isnan(games_data[:, col]), col] = col_mean
# Result: 1000 rows (0 NaN remaining)
# Advantage: No data loss, retains all records
# Disadvantage: Artificial values may bias analysis
```

#### Concepts Demonstrated:
- **File I/O**: `np.genfromtxt()` with column selection and row limiting
- **Data Quality**: Identifying and handling missing/irregular values
- **NaN Handling**: NumPy functions that ignore NaN (nanmean, nanmedian, etc.)
- **Boolean Indexing**: `axis` parameter for row-wise operations
- **Data Cleaning**: Multiple strategies with different trade-offs
- **Practical Decision-Making**: Choosing appropriate cleaning method

#### Exercise Structure:
The file contains two approaches:
1. **Part 1**: Individual demonstrations
   - Part A: Load and inspect data quality
   - Part B: Calculate statistics with missing values
   - Part C: Demonstrate three cleaning strategies
2. **Part 2**: Complete sequence
   - Full data science workflow from load to clean
   - Shows how parts connect in real analysis pipeline

#### Learning Outcomes:
✅ Load real-world CSV data with missing values  
✅ Identify data quality issues and NaN patterns  
✅ Use NaN-aware statistical functions  
✅ Apply multiple data cleaning strategies  
✅ Understand trade-offs between cleaning approaches  
✅ Work with practical datasets (all_games.csv)

#### Data Summary:
- **Total records**: 18,802
- **Loaded for exercise**: 1,000 (first 1000 records)
- **Columns used**: meta_score, user_review
- **Missing values**: 3 NaN (0.15%)
  - meta_score: 1 missing
  - user_review: 2 missing (from "tbd" values)

#### Files in Week 5 Seminar:
- `introduction_week_5_numpy.py` - Complete NumPy basics tutorial
- `exercise_1_week_5.py` - Array manipulation exercise with detailed comments
- `exercise_2_week_5.py` - CSV loading with data cleaning strategies
- `tips.csv` - Sample dataset (244 restaurant tips)
- `all_games.csv` - Video games dataset (18,802 records with metadata)
- `tips.npy` - Binary NumPy format example

---


## ✨ Features

- **📈 Data Analysis**: Pandas-based data manipulation and analysis
- **📊 Visualization**: Matplotlib and Seaborn for charts and plots
- **📓 Jupyter Notebooks**: Interactive data exploration
- **🧪 Testing**: Unit tests with pytest
- **📝 Documentation**: Comprehensive code documentation
- **🔄 Data Pipeline**: Extract, Transform, Load (ETL) workflows

## 🛠️ Technologies

- **Python 3.9+**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing and array operations
- **Matplotlib**: Data visualization and plotting
- **Seaborn**: Statistical visualization
- **SciPy**: Scientific computing and statistics
- **Jupyter**: Interactive notebooks
- **pytest**: Testing framework
- **BeautifulSoup4**: Web scraping
- **requests**: HTTP library for API calls

## 📋 Requirements

See `requirements.txt` for complete dependencies.

```
pandas>=2.0.0
numpy>=1.20.0
matplotlib>=3.5.0
seaborn>=0.12.0
scipy>=1.13.0
jupyter>=1.0.0
pytest>=7.0.0
beautifulsoup4>=4.12.0
requests>=2.31.0
```

## 🏃 Running the Project

### Basic Usage
```python
python main.py
```

### Run Tests
```python
pytest tests/
```

### Open Jupyter Notebooks
```bash
jupyter notebook
```

## 📊 Example Workflows

### Week 3: API Integration & Web Scraping
1. **Fetch Data**: Use REST APIs or web scraping
2. **Parse Responses**: Extract structured data from JSON/HTML
3. **Paginate**: Handle multiple pages of results
4. **Save Results**: Write data to text files

### Week 4: Data Visualization & EDA
1. **Load Data**: Read datasets using Seaborn/Pandas
2. **Explore**: Summary statistics and distributions
3. **Visualize**: Create histograms, scatter plots, box plots, heatmaps
4. **Analyze Relationships**: Correlation analysis and feature relationships
5. **Generate Insights**: Extract actionable preprocessing recommendations

### Week 5: NumPy Operations
1. **Create Arrays**: Generate random data or load from CSV
2. **Reshape**: Transform array dimensions
3. **Slice**: Extract subarrays using advanced indexing
4. **Filter**: Apply boolean masking for conditional operations
5. **Modify**: Perform efficient in-place transformations

### General Data Analysis Pipeline
1. **Load Data**: Read CSV/Excel files
2. **Explore**: Summary statistics and data profiling
3. **Clean**: Handle missing values and outliers
4. **Analyze**: Statistical analysis and insights
5. **Visualize**: Create charts and plots
6. **Report**: Generate analysis reports

## 🎯 Project Goals

- Learn data analysis workflows
- Practice data visualization techniques
- Develop ETL pipelines
- Create reproducible analysis
- Generate insights from data

## 📝 License

This project is for educational purposes.

## 🤝 Contributing

Feel free to extend this project with new analysis modules and visualizations.
