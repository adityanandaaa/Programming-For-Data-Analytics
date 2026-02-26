# Programming for Data Analytics

A comprehensive Python project for data analysis, visualization, and reporting using modern data science tools.

## 📂 Project Highlights & Key Accomplishments

- **Multi-Source Data Integration**: Developed robust workflows to ingest data from diverse sources including RESTful APIs (Open Library), web scraping (BeautifulSoup4), and structured file formats (CSV/Excel).
- **Advanced Exploratory Data Analysis (EDA)**: Performed in-depth statistical profiling and visualization on real-world datasets (House Prices, Customer Churn, Penguins, etc.) to uncover non-obvious patterns and trends.
- **Critical Data Quality Auditing**: Implemented systematic "Audit-Identify-Resolve" pipelines to detect hidden data issues like incorrect data types, whitespace strings, and systemic missingness.
- **Actionable Business Intelligence**: Translated complex data findings into concrete business recommendations, such as customer retention strategies and real estate value assessment.
- **High-Performance Numerical Computing**: Leveraged vectorized operations with NumPy for high-efficiency data manipulation, filtering, and weighted score calculations.
- **Professional Visualization Design**: Crafted multi-panel statistical visualizations (Box plots, Heatmaps, Distplots) with Seaborn and Matplotlib to clearly communicate complex relationships.
- **Robust Environment Management**: Established a professional development environment using Python virtual environments and clear dependency management (`requirements.txt`).
- **Structured Project Architecture**: Organized the codebase into a clean, hierarchical structure with clear separation between data, scripts, and visualization outputs.

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

# Run analysis examples (Example: Case Study 2)
python "Week 6 Seminar/case_study_2_customer_churn/exercise_1_case_study_2_customer_churn.py"
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
│   ├── exercise_3_week_5.py          # Data visualization and statistical analysis
│   ├── exercise_4_week_5.py          # Data filtering and weighted score calculation
│   ├── tips.csv          # Restaurant tips dataset
│   ├── all_games.csv     # Video games dataset (18,802 records)
│   └── tips.npy          # Binary NumPy format example
├── Week 6 Seminar/       # Week 6 seminar exercises (Pandas fundamentals)
│   ├── introduction_week_6_pandas.py  # Pandas basics lecture (from notebook)
│   ├── case_study_1_house_pricing/ # Case Study 1: House Pricing EDA
│   │   ├── exercise_1_case_study_1_house_pricing.py
│   │   ├── exercise_2_case_study_1_house_pricing.py
│   │   ├── exercise_3_case_study_1_house_pricing.py
│   │   └── visualizations/
│   │       ├── ... (8 .png files)
│   ├── case_study_2_customer_churn/ # Case Study 2: Customer Churn EDA
│   │   ├── exercise_1_case_study_2_customer_churn.py
│   │   └── visualizations/
│   │       ├── ... (6 .png files)
│   └── data source/      # Datasets for Week 6
│       ├── house_price.csv
│       ├── house_price.xlsx
│       └── customer_churn.csv
├── Week 7 Seminar/       # Week 7 seminar exercises
│   ├── introduction_week_7.py  # Python recreation of Titanic lecture
│   ├── case_study_1/     # Case Study 1: House Price Processing
│   │   ├── exercise_1_case_study_1_titanic.py
│   │   └── visualizations/
│   ├── case_study_2/     # Case Study 2: Customer Churn Processing
│   │   ├── exercise_1_case_study_2_customer_churn.py
│   │   └── visualizations/
│   ├── case_study_3/     # Case Study 3: Titanic Dataset Processing
│   │   ├── exercise_1_case_study_3_titanic.py
│   │   ├── exercise_2_case_study_3_titanic.py
│   │   └── visualizations/
│   ├── data source/      # Datasets for Week 7 (titanic_train.csv, customer_churn.csv)
│   └── visualizations/   # Visualization outputs for Week 7
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

---

### Exercise 3: Data Visualization and Statistical Analysis

**File**: `Week 5 Seminar/exercise_3_week_5.py`

This exercise focuses on exploratory data analysis (EDA) through visualization and statistical analysis of real datasets, with emphasis on handling missing data (NaN values).

#### Exercise Questions:
1. Visualize the distribution of meta_score and user_review
2. Visualize the relationship between meta_score and user_review
3. Find the average and standard deviation of meta_score and user_review
4. Remove rows with NaN values and repeat the analysis
5. Compare statistics before and after data cleaning

#### Detailed Solutions:

**Part A: Distribution Visualization**
```python
# Create histograms with KDE overlay
sns.histplot(meta_score, kde=True, bins=30, color='steelblue', stat='density')

# Box plot for comparison
plt.boxplot([meta_score, user_review], labels=['Meta Score', 'User Review'])

# Violin plot for distribution shape
plt.violinplot([meta_score], positions=[1], showmeans=True)
```

**Key Concepts:**
- **Histogram**: Shows frequency distribution of values
- **KDE (Kernel Density Estimation)**: Smooth estimate of probability distribution
- **Box Plot**: Displays quartiles, median, and outliers
- **Violin Plot**: Shows distribution shape and density

**Part B: Relationship Visualization**
```python
# Scatter plot with regression line
plt.scatter(meta_score, user_review, alpha=0.6)
z = np.polyfit(meta_score, user_review, 1)  # Fit line
p = np.poly1d(z)
plt.plot(x_line, p(x_line), "r-")  # Plot line

# Calculate correlation
correlation = np.corrcoef(meta_score, user_review)[0, 1]

# 2D density plot (hexbin)
plt.hexbin(meta_score, user_review, gridsize=20, cmap='YlOrRd')
```

**Correlation Interpretation:**
- **Strong positive** (> 0.7): Variables move together
- **Moderate positive** (0.3-0.7): Some relationship
- **Weak positive** (< 0.3): Slight relationship
- **Near zero**: Little to no linear relationship
- **Negative values**: Inverse relationship

**Part C: Statistical Analysis with NaN Handling**
```python
# Statistics with NaN present (using NaN-aware functions)
meta_mean_with_nan = np.nanmean(meta_score)
meta_std_with_nan = np.nanstd(meta_score)

# Remove rows with any NaN values
clean_data = games_data[~np.isnan(games_data).any(axis=1)]

# Statistics on clean data
meta_mean_clean = np.mean(clean_data[:, 0])
meta_std_clean = np.std(clean_data[:, 0])
```

**NaN Handling Techniques:**
- `np.nanmean()`: Calculate mean ignoring NaN values
- `np.nanstd()`: Calculate std dev ignoring NaN values
- `np.isnan(a).any(axis=1)`: Check for NaN in each row
- `a[~np.isnan(a).any(axis=1)]`: Remove rows with any NaN

**Impact of Missing Data:**
- Small impact on mean (often < 1%)
- Large impact on std dev (can be 200%+ different)
- Std dev highly sensitive to missing value patterns
- Clean data provides more reliable statistics

#### Visualizations Created:
1. **exercise_3_distributions.png**: Histograms, box plot, violin plot
   - Shows data spread and distribution shapes
   - Compares ranges between variables
   
2. **exercise_3_relationship.png**: Scatter plot, regression line, 2D density
   - Shows correlation between variables
   - Identifies point concentrations
   
3. **exercise_3_statistics.png**: Mean and std comparison
   - Quantifies impact of NaN removal
   - Visual evidence of data quality effects

#### Concepts Demonstrated:
- **Exploratory Data Analysis (EDA)**: Visual data understanding
- **Distribution Analysis**: Histograms, KDE, box plots, violin plots
- **Correlation Analysis**: Scatter plots, regression lines, Pearson coefficient
- **NaN-Aware Statistics**: Functions that handle missing data gracefully
- **Data Cleaning**: Boolean indexing for removing missing rows
- **Data Quality Assessment**: Comparing statistics before/after cleaning
- **Visualization Best Practices**: Multiple plot types for different insights

#### Learning Outcomes:
✅ Create meaningful visualizations for exploratory data analysis  
✅ Interpret histograms, box plots, and violin plots  
✅ Calculate and interpret correlation coefficients  
✅ Use NaN-aware statistical functions  
✅ Remove missing data using boolean indexing  
✅ Quantify impact of data quality on statistics  
✅ Generate professional-quality data analysis reports

#### Data Insights from Exercise:
- **Meta Score**: Mean = 90.35, Std = 2.40 (tight distribution)
- **User Review**: Mean = 8.12, Std = 0.86 (after cleaning)
- **Correlation**: 0.22 (weak positive - some relationship)
- **Missing Data**: 3 rows removed (0.3% of 1000)
- **Data Quality**: Std dev changed 215% after removing NaN (user_review)

#### Practical Applications:
- Exploratory Data Analysis (EDA) before machine learning
- Quality assurance for datasets
- Feature correlation analysis
- Report generation with insights
- Data-driven decision making
- Statistical validation before analysis

---

### Exercise 4: Data Filtering and Weighted Score Calculation

**File**: `Week 5 Seminar/exercise_4_week_5.py`

This exercise focuses on advanced data filtering with multiple conditions and calculating composite scores from multiple features.

#### Exercise Questions:
1. Select all records with meta_score greater than 95
2. Optional: Also filter records where user_review is lower than 8
3. Calculate weighted scores: `meta_score * 0.6 + user_review * 4`
4. Compare filtering results and weighted scores
5. Analyze statistical differences between datasets

#### Detailed Solutions:

**Part A: Basic Filtering (meta_score > 95)**
```python
# Create boolean mask
mask = meta_score > 95

# Filter data
filtered_data = games_data[mask]

# Statistics
print(f"Filtered records: {filtered_data.shape[0]}")
print(f"Percentage: {(filtered_data.shape[0] / games_data.shape[0]) * 100:.2f}%")
```

**Results:**
- Records with meta_score > 95: **45 out of 1000 (4.5%)**
- Mean meta_score: 96.67 (high-quality subset)
- Mean user_review: 8.48 (strong user approval)

**Part B: Combined Filtering (AND Logic)**
```python
# Create individual masks
mask1 = meta_score > 95
mask2 = user_review < 8

# Combine with AND operator (&)
combined_mask = (meta_score > 95) & (user_review < 8)

# Filter data
filtered_combined = games_data[combined_mask]
```

**Key Operators:**
- `&` (AND): Both conditions must be True - **intersection**
- `|` (OR): At least one condition is True - **union**
- `~` (NOT): Inverts the mask - **complement**
- **Important**: Use parentheses: `(mask1) & (mask2)`

**Results:**
- Records matching BOTH conditions: **8 out of 1000 (0.8%)**
- Meta score range: [96.0, 98.0]
- User review range: [6.2, 7.9]
- Represents professionally excellent games with mixed user reviews

**Part C: Weighted Score Calculation**
```python
# Weighted score formula
weighted_score = meta_score * 0.6 + user_review * 4

# For example:
# meta_score=99.0, user_review=9.1 → 99*0.6 + 9.1*4 = 95.80
# meta_score=98.0, user_review=7.4 → 98*0.6 + 7.4*4 = 88.40
```

**Formula Components:**
- `meta_score * 0.6`: Professional rating (60% weight)
- `user_review * 4`: User sentiment scaled (scaled to match contribution)
- Result range: [46.2, 150.2] typically [60, 120]

**Results:**
- **All data**: Mean = 86.68, Std = 3.99, Range [66.00, 95.80]
- **Filtered (meta > 95)**: Mean = 91.93, Std = 2.60, Range [83.00, 95.80]
- **Difference**: Filtered subset has 5.25 higher average weighted score

#### Concepts Demonstrated:
- **Boolean Indexing**: Creating and applying boolean masks
- **Multiple Conditions**: AND/OR logic for complex filtering
- **Mask Operations**: Combining, inverting, and applying masks
- **Weighted Scoring**: Multi-feature composite scoring
- **Data Subsetting**: Comparing full vs filtered datasets
- **Statistical Analysis**: Comparing means, stds, ranges
- **Vectorized Operations**: Applying calculations to entire arrays

#### Learning Outcomes:
✅ Create complex boolean filters with multiple conditions  
✅ Understand AND (&) vs OR (|) operators  
✅ Apply weighted formulas to combine features  
✅ Compare statistical properties of different subsets  
✅ Interpret filtered dataset characteristics  
✅ Calculate composite scores for ranking/recommendations  

#### Key Functions:
```python
meta_score > 95          # Create boolean mask
(mask1) & (mask2)        # Combine masks with AND
(mask1) | (mask2)        # Combine masks with OR
~mask                    # Invert mask (NOT)
np.sum(mask)             # Count True values
data[mask]               # Apply mask to filter
np.nanmean() / np.nanstd() # Statistics with NaN handling
np.percentile()          # Calculate quartiles
```

#### Data Insights:
- **Filtering effectiveness**: AND logic reduces dataset from 4.5% to 0.8%
- **High-quality games**: Professional scores > 95 represent elite quality
- **Mixed reviews**: Some highly-rated games have lower user scores
- **Weighted score**: Gives 37.5% more weight to meta_score vs user_review
- **Composite ranking**: Useful for recommendation systems and filtering

#### Practical Applications:
- Game recommendation systems (filter by quality, score players)
- E-commerce product filtering (multi-criteria selection)
- Machine learning feature engineering (composite features)
- Business intelligence (weighted KPI calculations)
- Data quality filtering (remove outliers, find subgroups)
- Ranking and recommendation algorithms

#### Files in Week 5 Seminar:
- `introduction_week_5_numpy.py` - Complete NumPy basics tutorial
- `exercise_1_week_5.py` - Array manipulation exercise with detailed comments
- `exercise_2_week_5.py` - CSV loading with data cleaning strategies
- `exercise_3_week_5.py` - Data visualization and statistical analysis
- `exercise_4_week_5.py` - Data filtering and weighted score calculation
- `tips.csv` - Sample dataset (244 restaurant tips)
- `all_games.csv` - Video games dataset (18,802 records)
- `tips.npy` - Binary NumPy format example

---

## 📊 Week 6 Seminar

The **Week 6 Seminar** folder contains exercises focused on **Pandas fundamentals** for data manipulation and analysis.

### Introduction: Pandas Basics Lecture

**File**: `Week 6 Seminar/introduction_week_6_pandas.py`

This comprehensive introduction covers 12 essential Pandas topics converted from the lecture notebook:

**Topics Covered:**
1. **Create Pandas Series** - One-dimensional labeled arrays with custom indices
2. **Create DataFrame** - Multiple methods: dictionaries, lists, NumPy arrays, Series
3. **Create DataFrame from Files** - CSV reading with various parameters
4. **Conversion between DataFrame and ndarray** - Bidirectional conversion
5. **Element-wise Operations** - Broadcasting and vectorized operations
6. **Column Selection, Addition and Deletion** - DataFrame structure manipulation
7. **Row Selection** - Using `.loc[]`, `.iloc[]`, and boolean indexing
8. **Add and Delete Rows** - Using `pd.concat()` and `.drop()` methods
9. **Important DataFrame Attributes** - `.index`, `.columns`, `.shape`, etc.
10. **Scalar Operations** - Arithmetic with scalars, lists, and Series
11. **Data Processing - Explore Dataset** - `.info()`, `.describe()`, `.head()`, `.tail()`
12. **Exploration via Visualization** - Histograms, distributions with matplotlib/seaborn

**Key Concepts:**
- Series vs DataFrame differences
- Index alignment and matching
- NaN handling in mismatched data
- Row vs column operations (axis parameter)
- `.loc[]` (label-based) vs `.iloc[]` (position-based) indexing
- Boolean masking for filtering
- GroupBy operations for aggregation

**Visualizations Generated:**
- `tips_histogram_all.png` - All columns histograms
- `tips_histogram_total_bill.png` - Single column histogram
- `tips_histogram_by_sex.png` - Histogram grouped by category
- `tips_catplot.png` - Category count plot with Seaborn
- `tips_displot.png` - Distribution plot
- `tips_pairplot.png` - Pairwise relationships
- `tips_boxplot.png` - Box plot by category

**Example Usage**:
```bash
cd "Week 6 Seminar"
python introduction_week_6_pandas.py
```

**Requirements**: Pandas, NumPy, Matplotlib, Seaborn, openpyxl (for Excel files)

---

### Exercise 1: House Pricing Case Study

**File**: `Week 6 Seminar/case_study_1_house_pricing/exercise_1_case_study_1_house_pricing.py`

This case study uses real house sales data from Ames, Iowa (Kaggle dataset) to practice essential Pandas operations.

**Dataset**: `house_price.csv` / `house_price.xlsx` (1,460 houses × 28 features)
- **Index**: House ID (101-1560)
- **Features**: Neighborhood, Condition, Sale Price, Year Built, Quality, etc.
- **Target**: SalePrice (ranging from $34,900 to $755,000)

#### Task 1: Import CSV with Custom Index
```python
# Read CSV file with 'Id' column as row index
df_house = pd.read_csv('house_price.csv', index_col='Id')
```

**Concepts**: 
- `pd.read_csv()` function
- `index_col` parameter for custom indexing
- DataFrame inspection with `.shape`, `.info()`, `.head()`

**Output**: DataFrame with 1,460 rows × 28 columns

---

#### Task 2: Import Excel File
```python
# Read Excel file (requires openpyxl library)
df_house_excel = pd.read_excel('house_price.xlsx', index_col='Id')
```

**Concepts**:
- `pd.read_excel()` function
- Installing dependencies (`pip install openpyxl`)
- Comparing DataFrames with `.equals()`
- Error handling with try-except blocks

**Output**: Identical DataFrame from Excel format

---

#### Task 3: Create Series from Column
```python
# Extract single column as Series
price = df_house['SalePrice']
```

**Concepts**:
- Series extraction from DataFrame
- Series attributes: `.name`, `.dtype`, `len()`
- Statistical methods: `.mean()`, `.median()`, `.min()`, `.max()`, `.std()`
- Comprehensive statistics with `.describe()`

**Results**:
- Mean price: $180,921.20
- Median price: $163,000.00
- Price range: $34,900 - $755,000
- Standard deviation: $79,442.50

---

#### Task 4: Create DataFrame from Multiple Columns
```python
# Select multiple columns with double bracket notation
df_location = df_house[['Neighborhood', 'Condition1']]
```

**Concepts**:
- Multi-column selection with `[['col1', 'col2']]`
- Counting unique values with `.nunique()`
- Value frequency with `.value_counts()`
- DataFrame vs Series return types

**Results**:
- 25 unique neighborhoods
- 9 unique proximity conditions
- Most common: NAmes (225 houses), Norm condition (1,260 houses)

---

#### Additional Analysis: GroupBy Operations

**Average Price by Neighborhood:**
```python
df_location_price.groupby('Neighborhood')['SalePrice'].mean()
```

**Top 3 Most Expensive Neighborhoods:**
1. **NoRidge**: $335,295 (North Ridge)
2. **NridgHt**: $316,271 (Northridge Heights)
3. **StoneBr**: $310,499 (Stone Brook)

**Average Price by Proximity Condition:**
```python
df_location_price.groupby('Condition1')['SalePrice'].mean()
```

**Best Conditions:**
1. **PosA**: $225,875 (Adjacent to positive feature)
2. **PosN**: $215,184 (Near positive feature)
3. **RRNn**: $212,400 (Near north-south railroad)

---

#### Concepts Demonstrated:
- **Data Import**: CSV and Excel file reading
- **Index Management**: Custom row indices
- **Series Operations**: Statistical analysis on single columns
- **DataFrame Subsetting**: Selecting specific columns
- **Data Exploration**: Understanding data structure and content
- **GroupBy Aggregation**: Computing statistics by category
- **Error Handling**: Managing missing dependencies

#### Learning Outcomes:
✅ Import data from CSV and Excel files with custom indices  
✅ Extract Series from DataFrame columns  
✅ Create new DataFrames by selecting columns  
✅ Perform statistical analysis on numerical data  
✅ Use GroupBy for categorical aggregation  
✅ Compare and validate data from different sources  
✅ Handle missing dependencies gracefully  
✅ Interpret real-world housing market data  

#### Key Functions Used:
```python
pd.read_csv(file, index_col)    # Read CSV with custom index
pd.read_excel(file, index_col)  # Read Excel file
df['column']                     # Extract single column (Series)
df[['col1', 'col2']]            # Extract multiple columns (DataFrame)
df.shape                         # Get dimensions (rows, cols)
df.info()                        # Display structure and types
df.head()                        # Show first N rows
series.describe()                # Statistical summary
series.mean() / median() / std() # Specific statistics
df.nunique()                     # Count unique values
df.value_counts()                # Frequency distribution
df.groupby('col')['col2'].mean() # Group and aggregate
df.equals(other_df)              # Compare DataFrames
```

---

### Exercise 2: Case Study 1 - Advanced DataFrame Indexing and Boolean Filtering

**File**: `Week 6 Seminar/case_study_1_house_pricing/exercise_2_case_study_1_house_pricing.py` (309 lines)
**Dataset**: House Prices (Ames, Iowa)

This exercise focuses on advanced DataFrame operations including label-based indexing (`.loc[]`), position-based indexing (`.iloc[]`), and boolean masking for complex filtering operations.

#### Exercise Questions:
4. Find sale prices for houses with id 222 and 333
5. Find the first 100 records in "df_location"
6. Find all rows from df_house with OverallQual at least 8 and save as "df_great"
7. (Optional) Find rows with OverallQual >= 8 AND SalePrice < 300,000 and save as "df_deal"

#### Detailed Solutions:

---

#### Task 4: Find Sale Prices by ID
```python
# Method 1: Using .loc[] with list of IDs
prices = df_house.loc[[222, 333], 'SalePrice']

# Method 2: Individual access
price_222 = df_house.loc[222, 'SalePrice']
price_333 = df_house.loc[333, 'SalePrice']
```

**Concepts**:
- `.loc[]` for label-based indexing
- Selecting specific rows by index values
- Single vs multiple row selection
- Accessing specific columns with label indexing

**Results**:
- House Id 222: $100,000
- House Id 333: $94,500
- Mean: $97,250
- Price difference: $5,500

**Key Difference**: `.loc[]` uses index labels (Id column values), not positions

---

#### Task 5: Find First 100 Records
```python
# Method 1: Using .head() (most readable)
df_location_first_100 = df_location.head(100)

# Method 2: Using .iloc[] with slice
df_location_first_100 = df_location.iloc[0:100]

# Method 3: Direct slice notation
df_location_first_100 = df_location[0:100]
```

**Concepts**:
- `.head(n)` for retrieving first N rows
- `.iloc[]` for position-based indexing
- Slice notation with DataFrames
- Index vs position distinction

**Important Note**: With `.iloc[]`, the end position is EXCLUDED (Python standard)

**Results**:
- Shape: 100 rows × 2 columns
- All three methods produce identical results
- Most common neighborhood in first 100: NAmes (21 houses)
- Dominant condition: Norm (87 houses)

---

#### Task 6: Filter High-Quality Houses
```python
# Create boolean mask
mask_quality = df_house['OverallQual'] >= 8

# Apply mask to filter DataFrame
df_great = df_house.loc[mask_quality]

# Alternative: Direct boolean indexing
df_great = df_house[df_house['OverallQual'] >= 8]
```

**Concepts**:
- Boolean masking for filtering
- Creating condition masks
- Applying masks with `.loc[]`
- Direct boolean indexing syntax

**Results**:
- **229 houses** with OverallQual >= 8 (15.7% of dataset)
- Quality distribution: 168 houses (quality=8), 43 (quality=9), 18 (quality=10)
- Average price: $305,035.90
- Price range: $122,000 - $755,000

**Quality Premium**: High-quality houses cost **68.6% more** than average ($124,115 premium)

---

#### Task 7: Complex Boolean Filtering (Optional)
```python
# Combine multiple conditions with & (AND operator)
mask_deal = (df_house['OverallQual'] >= 8) & (df_house['SalePrice'] < 300000)

# Apply combined mask
df_deal = df_house.loc[mask_deal]
```

**Concepts**:
- Combining boolean conditions
- `&` (AND), `|` (OR), `~` (NOT) operators
- Parentheses for proper operator precedence
- Multiple criteria filtering

**Critical Note**: Use `&` for element-wise AND, not `and` (which is for boolean values only)

**Results**:
- **127 houses** meet both criteria (8.7% of total)
- Represents **55.5%** of all high-quality houses
- Average price: $243,303.09
- Average savings: $61,732.81 (20.2% cheaper than all df_great)

**Top Deal Neighborhoods**:
1. **Somerst**: 25 houses
2. **CollgCr**: 23 houses
3. **NridgHt**: 17 houses

**Year Built Range**: 1872-2009 (average: 1997)

---

#### Comparison Summary:

| DataFrame | Rows | Avg Price | % of Total | Description |
|-----------|------|-----------|------------|-------------|
| df_house | 1,460 | $180,921 | 100% | Full dataset |
| df_great | 229 | $305,036 | 15.7% | OverallQual >= 8 |
| df_deal | 127 | $243,303 | 8.7% | High quality + affordable |

**Key Insight**: Over half of high-quality houses are priced under $300k, offering significant value opportunities.

---

#### Concepts Demonstrated:
- **Label-Based Indexing**: `.loc[]` with index labels
- **Position-Based Indexing**: `.iloc[]` with integer positions
- **Head/Tail Methods**: `.head()`, `.tail()` for quick data viewing
- **Boolean Masking**: Creating and applying conditional filters
- **Complex Filtering**: Combining multiple boolean conditions
- **Logical Operators**: `&` (AND), `|` (OR), `~` (NOT)
- **Data Subsetting**: Creating new DataFrames from filtered data
- **Statistical Comparison**: Analyzing filtered vs full datasets
- **Identifying Data Patterns**: Finding high-risk segments

#### Learning Outcomes:
✅ Master `.loc[]` for label-based row/column selection  
✅ Master `.iloc[]` for position-based indexing  
✅ Create boolean masks from conditional expressions  
✅ Combine multiple conditions with logical operators  
✅ Filter DataFrames based on single and multiple criteria  
✅ Compare statistics across different data subsets  
✅ Identify data patterns and market insights  
✅ Handle complex data filtering scenarios  

#### Key Functions and Techniques:
```python
df.loc[row_labels, col_labels]   # Label-based indexing
df.iloc[row_positions, col_pos]  # Position-based indexing
df.head(n) / df.tail(n)          # First/last N rows
df[condition]                     # Boolean indexing
condition1 & condition2           # AND operator
condition1 | condition2           # OR operator
~condition                        # NOT operator
mask.sum()                        # Count True values
df.equals(other_df)               # Compare DataFrames
series.value_counts()             # Frequency counts
```

#### Data Insights:
- **Quality Distribution**: Only 15.7% of houses have OverallQual >= 8
- **Price Premium**: High quality adds 68.6% to average price
- **Value Opportunities**: 55.5% of high-quality homes are affordable (<$300k)
- **Best Deal Areas**: Somerst, CollgCr, NridgHt neighborhoods
- **Age Factor**: Deal houses average 1997 build year (relatively newer)

#### Practical Applications:
- Real estate filtering by multiple criteria
- Market segmentation analysis
- Investment opportunity identification
- Price-to-quality ratio analysis
- Neighborhood value assessment
- Complex database queries in Pandas
- Feature filtering for machine learning

---

### Exercise 3: Case Study 1 - Exploratory Data Analysis (EDA)

**File**: `Week 6 Seminar/case_study_1_house_pricing/exercise_3_case_study_1_house_pricing.py` (593 lines)
**Dataset**: House Prices (Ames, Iowa)

This exercise demonstrates comprehensive exploratory data analysis techniques including missing value identification, distribution analysis, correlation studies, and categorical feature exploration.

#### Task Overview:
Create a DataFrame from selected columns and perform complete EDA:
- **Numeric columns** (7): OverallQual, GrLivArea, TotRmsAbvGrd, YearBuilt, LotArea, LotFrontage, SalePrice
- **Categorical columns** (3): MSZoning, Neighborhood, HouseStyle

#### Analysis Steps:

**1. Missing Value Analysis**
```python
# Identify and quantify missing data
missing_counts = df_selected.isnull().sum()
missing_percentages = (missing_counts / total_rows) * 100

# Visualize missing data patterns
plt.barh(missing_counts.sort_values())
```

**Key Findings**:
- Only **LotFrontage** has missing values: 259 (17.74%)
- All other features are complete
- May require imputation strategy for LotFrontage

---

**2. Statistical Summary - Numeric Features**
```python
# Comprehensive statistics
df_selected[numeric_cols].describe()

# Additional metrics
for col in numeric_cols:
    print(f"Skewness: {df_selected[col].skew()}")
    print(f"Kurtosis: {df_selected[col].kurtosis()}")
```

**Distribution Characteristics**:
- **SalePrice**: Right-skewed (skewness=1.88), mean=$180,921, range=$34,900-$755,000
- **OverallQual**: Slightly right-skewed (skewness=0.22), most houses rated 5-7
- **GrLivArea**: Right-skewed (skewness=1.37), indicates larger homes are outliers
- **LotArea**: Heavily right-skewed (skewness=12.21), extreme outliers present
- **YearBuilt**: Left-skewed (skewness=-0.61), more recent constructions

---

**3. Distribution Visualization**
```python
# Histograms with frequency distributions
df_selected[col].hist(bins=30, color='skyblue')

# Box plots for outlier detection
df_selected.boxplot(column=col, patch_artist=True)
```

**Outlier Detection**:
- **LotArea**: Several extreme outliers (>100,000 sq ft)
- **GrLivArea**: Few houses >4,000 sq ft
- **SalePrice**: High-end luxury homes create right tail

---

**4. Categorical Feature Analysis**
```python
# Frequency distributions
df_selected[col].value_counts()

# Visualize category distributions
value_counts.plot(kind='bar', color='teal')
```

**Category Insights**:
- **MSZoning**: 5 types, dominated by RL (Residential Low Density, 1,151 houses)
- **Neighborhood**: 25 neighborhoods, NAmes most common (225), Blueste rarest (2)
- **HouseStyle**: 8 styles, 1Story most popular (726), 2.5Fin least common (8)

---

**5. Correlation Analysis - Numeric Features**
```python
# Compute correlation matrix
correlation_matrix = df_selected[numeric_cols].corr()

# Visualize with heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

# Scatter plots with trend lines
plt.scatter(df_selected[col], df_selected['SalePrice'])
```

**Correlation with SalePrice**:
1. **OverallQual**: 0.791 (Strong positive) - Quality is top predictor
2. **GrLivArea**: 0.709 (Strong positive) - Living area highly correlated
3. **TotRmsAbvGrd**: 0.534 (Moderate positive) - Room count matters
4. **YearBuilt**: 0.523 (Moderate positive) - Newer homes cost more
5. **LotFrontage**: 0.352 (Weak positive) - Street footage less important
6. **LotArea**: 0.264 (Weak positive) - Lot size has minimal impact

**Interpretation**:
- Quality and living space are strongest price drivers
- Lot characteristics have surprisingly weak correlation
- Linear relationships visible in scatter plots
- Some non-linear patterns suggest feature engineering opportunities

---

**6. Categorical Impact on SalePrice**
```python
# Group by category and aggregate
category_prices = df_selected.groupby(col)['SalePrice'].agg(['mean', 'median', 'count'])

# Box plots by category
df_selected.boxplot(column='SalePrice', by=col)

# Average price comparison
avg_prices.plot(kind='barh', color='darkgreen')
```

**Price Variation by Category**:

**MSZoning** (Residential Type):
- **Highest**: FV (Floating Village) - $214,014 avg
- **Lowest**: C (all) (Commercial) - $74,528 avg
- **Price Ratio**: 2.87x difference

**Neighborhood** (Location):
- **Highest**: NoRidge (North Ridge) - $335,295 avg
- **Lowest**: MeadowV (Meadow Village) - $98,576 avg
- **Price Ratio**: 3.40x difference (location matters most!)

**HouseStyle** (Architecture):
- **Highest**: 2.5Fin (2.5 story finished) - $220,000 avg
- **Lowest**: 1.5Unf (1.5 story unfinished) - $110,150 avg
- **Price Ratio**: 2.00x difference

---

#### Visualizations Created (8 files):
1. **exercise_3_missing_values.png**: Bar chart of missing data counts
2. **exercise_3_numeric_distributions.png**: Histograms for all 7 numeric features
3. **exercise_3_numeric_boxplots.png**: Box plots showing outliers and quartiles
4. **exercise_3_categorical_distributions.png**: Frequency bars for 3 categorical features
5. **exercise_3_correlation_heatmap.png**: Color-coded correlation matrix
6. **exercise_3_scatter_saleprice.png**: 6 scatter plots with trend lines
7. **exercise_3_saleprice_by_categories.png**: Box plots of price by category
8. **exercise_3_avg_price_by_categories.png**: Bar charts of average prices

---

#### Concepts Demonstrated:
- **Missing Value Detection**: `.isnull()`, `.sum()`, percentage calculations
- **Descriptive Statistics**: `.describe()`, `.mean()`, `.median()`, `.std()`
- **Distribution Analysis**: Histograms, KDE, skewness, kurtosis
- **Outlier Detection**: Box plots, IQR calculations
- **Correlation Analysis**: `.corr()`, Pearson coefficients, heatmaps
- **Categorical Aggregation**: `.groupby()`, `.agg()`, category-based statistics
- **Data Visualization**: Matplotlib, Seaborn, multiple plot types
- **Feature Relationships**: Scatter plots, trend lines, regression fitting

#### Learning Outcomes:
✅ Identify and quantify missing data in DataFrames  
✅ Calculate comprehensive statistical summaries  
✅ Analyze distribution shapes and detect outliers  
✅ Compute and interpret correlation coefficients  
✅ Visualize data using histograms, box plots, and heatmaps  
✅ Analyze categorical feature impact on target variable  
✅ Create professional EDA visualizations  
✅ Extract actionable insights from exploratory analysis  
✅ Prepare data quality assessment reports  
✅ Identify feature engineering opportunities  

#### Key Functions and Techniques:
```python
df.isnull().sum()                # Count missing values
df.describe()                     # Statistical summary
df[col].skew() / kurtosis()      # Distribution shape metrics
df.hist() / df.boxplot()         # Distribution visualizations
df.corr()                         # Correlation matrix
sns.heatmap()                      # Correlation visualization
df.groupby(col).agg()            # Categorical aggregation
plt.scatter()                     # Relationship visualization
np.polyfit() / np.poly1d()       # Trend line fitting
df.select_dtypes()               # Filter columns by type
```

#### Key Insights from Analysis:

**1. Data Quality**:
- 17.74% missing in LotFrontage requires imputation
- Other features have excellent completeness
- No duplicate records detected

**2. Price Distribution**:
- Right-skewed: Mean ($180,921) > Median ($163,000)
- Wide range: $34,900 to $755,000
- Suggests log transformation may help for modeling

**3. Strongest Predictors**:
- **Quality (r=0.79)**: Overall quality rating is #1 predictor
- **Size (r=0.71)**: Living area square footage is #2
- **Combination**: Quality + Size explain majority of price variance

**4. Location Premium**:
- Neighborhood creates **3.4x price difference**
- NoRidge, NridgHt, StoneBr are premium areas
- MeadowV, IDOTRR, BrDale are budget areas

**5. Outlier Patterns**:
- Several mega-lots (LotArea >100k sq ft) skew distribution
- A few luxury homes (>$600k) create price outliers
- Some exceptionally large homes (>4k sq ft GrLivArea)

**6. Feature Engineering Opportunities**:
- Create quality-size interaction term
- Bin neighborhoods into price tiers
- Log-transform skewed features (SalePrice, LotArea, GrLivArea)
- Impute LotFrontage using neighborhood median
- Create age bins from YearBuilt

#### Recommended Next Steps:
1. **Handle Missing Data**: Impute LotFrontage using neighborhood-based strategy
2. **Address Outliers**: Investigate and potentially remove extreme values
3. **Transform Features**: Apply log transformation to right-skewed variables
4. **Encode Categoricals**: One-hot encode or target encode categorical features
5. **Feature Engineering**: Create interaction terms and polynomial features
6. **Normalization**: Standardize numeric features for modeling
7. **Train-Test Split**: Prepare data for machine learning pipeline

---

### Case Study 2: Customer Churn Analysis - Complete EDA

**File**: `Week 6 Seminar/case_study_2_customer_churn/exercise_1_case_study_2_customer_churn.py` (685 lines)
**Dataset**: Telco Customer Churn (Kaggle)  
**Records**: 7,043 customers × 21 columns

This comprehensive case study demonstrates real-world data analysis workflow including data quality auditing, issue identification, data cleaning, and actionable business insights extraction from a customer churn dataset.

#### Dataset Overview:

**Source**: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

**Columns** (21 total):
- **Customer Info**: customerID
- **Demographics** (4): gender, SeniorCitizen, Partner, Dependents
- **Account Info** (4): tenure, Contract, PaperlessBilling, PaymentMethod
- **Services** (9): PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies
- **Charges** (2): MonthlyCharges, TotalCharges
- **Target**: Churn (Yes/No)

---

#### The Critical Issue (THE HINT!):

**🚨 Data Quality Problem Identified**:
```python
# TotalCharges column stored as 'object' instead of numeric!
df_churn['TotalCharges'].dtype  # Returns: object (WRONG!)

# Investigation reveals:
# - 11 records contain empty string values (' ')
# - All problematic records have tenure = 0 (new customers)
# - Empty strings prevent numeric operations
```

**Root Cause**: New customers (tenure=0) have no billing history, resulting in empty TotalCharges values saved as whitespace strings instead of NaN or 0.

**Resolution Strategy**:
```python
# Convert to numeric, coercing errors to NaN
df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'], errors='coerce')

# Impute missing values with MonthlyCharges
# (For new customers, TotalCharges ≈ MonthlyCharges)
mask_missing = df_clean['TotalCharges'].isnull()
df_clean.loc[mask_missing, 'TotalCharges'] = df_clean.loc[mask_missing, 'MonthlyCharges']
```

**Key Learning**: Always audit data types! Numeric columns stored as text prevent statistical operations and indicate upstream data quality issues.

---

#### Analysis Steps (14 comprehensive steps):

**STEP 1: Import Dataset**
- Load 7,043 customer records
- Initial data preview with `.head()` and `.tail()`

**STEP 2: Initial Data Inspection**
- `.info()` reveals data types and non-null counts
- Check for duplicates (0 found)
- Verify unique customer IDs (no duplicates)

**STEP 3: Missing Values Analysis**
- Explicit NaN values: 0 (none detected initially)
- Hidden issues require deeper audit

**STEP 4: Data Type Audit** ⚠️ **CRITICAL STEP**
- Systematic review of all column types
- **Issue identified**: TotalCharges as 'object' instead of numeric
- Investigation reveals 11 empty string values
- All problematic records have tenure = 0

**STEP 5: Fix Data Quality Issues**
- Convert TotalCharges to numeric
- Impute 11 missing values using MonthlyCharges
- Validate cleaning success

**STEP 6: Statistical Summary**
- Separate numeric (SeniorCitizen, tenure, MonthlyCharges, TotalCharges) from categorical
- Generate descriptive statistics with `.describe()`

**STEP 7: Target Variable Analysis - Churn**
- Overall churn rate: **26.54%**
- Distribution: 5,174 retained (73.46%), 1,869 churned (26.54%)
- Visualize with bar chart

**STEP 8: Demographic Analysis**
- Gender, SeniorCitizen, Partner, Dependents
- Calculate churn rates for each demographic segment
- Visualize with grouped bar charts

**STEP 9: Service Usage Analysis**
- Analyze 9 service features
- Identify which services correlate with churn
- Subscription rates and churn percentages

**STEP 10: Contract and Payment Analysis**
- Contract type distributions and churn rates
- Payment method impact on retention
- Visualize with comparative bar charts

**STEP 11: Tenure Analysis**
- Distribution comparison between churned vs retained
- Statistical comparison of tenure patterns
- Histogram and box plot visualizations

**STEP 12: Charges Analysis**
- MonthlyCharges and TotalCharges distributions
- Compare charges between churned and retained customers
- 4-panel visualization (histograms + box plots)

**STEP 13: Correlation Analysis**
- Convert Churn to binary for correlation
- Compute correlation matrix for numeric features
- Heatmap visualization

**STEP 14: Key Insights Summary**
- Comprehensive findings report
- Business recommendations
- Actionable retention strategies

---

#### Key Findings:

**1. Churn Rate**: 26.54% overall (1,869 of 7,043 customers)

**2. Demographics**:
- **Senior Citizens**: 41.68% churn (HIGH RISK)
- **No Partner**: 32.96% churn vs 19.66% with partner
- **No Dependents**: 31.28% churn vs 15.53% with dependents
- **Gender**: Minimal difference (26.92% male, 26.16% female)

**3. Contract Type** - **MOST CRITICAL FACTOR**:
```
Month-to-month: 42.71% churn  ← VERY HIGH RISK
One year:       11.27% churn
Two year:        2.83% churn  ← VERY LOW RISK
```
**15x difference** between month-to-month and two-year contracts!

**4. Payment Method**:
```
Electronic check:            45.29% churn  ← HIGHEST RISK
Mailed check:               19.08% churn
Bank transfer (automatic):  16.69% churn
Credit card (automatic):    15.22% churn  ← LOWEST RISK
```
Automatic payment methods have 3x lower churn than electronic check.

**5. Tenure Patterns**:
- **Churned customers**: Average 18.0 months tenure
- **Retained customers**: Average 37.6 months tenure
- First 6 months are critical retention period
- Customers with >2 years tenure rarely churn

**6. Charges Impact**:
- **Churned customers**: $74.44 avg monthly charges (+21% higher)
- **Retained customers**: $61.27 avg monthly charges
- Higher prices correlate with higher churn
- Total charges show inverse correlation (-0.198) - long-term customers pay more total but churn less

**7. Internet Service**:
```
Fiber optic: 41.89% churn  ← PREMIUM SERVICE, HIGH CHURN
DSL:         18.96% churn
No service:   7.40% churn  ← LOWEST CHURN
```
Counter-intuitive: Fiber optic has **2.2x higher** churn despite being premium service!

**8. Value-Added Services** (customers WITHOUT these churn more):
- **No OnlineSecurity**: 41.84% churn vs 14.55% with security
- **No TechSupport**: 41.71% churn vs 15.21% with support
- **No OnlineBackup**: 39.96% churn vs 21.63% with backup

---

#### Correlations with Churn:

```python
tenure:         -0.352  (Moderate negative - longer tenure = less churn)
TotalCharges:   -0.198  (Weak negative)
MonthlyCharges:  0.193  (Weak positive - higher price = more churn)
SeniorCitizen:   0.151  (Weak positive)
```

---

#### Visualizations Created (6 files):

1. **exercise_cs2_churn_distribution.png**
   - Bar chart showing 73.46% retention vs 26.54% churn
   - Clear visual of imbalanced target variable

2. **exercise_cs2_demographics_churn.png**
   - 2×2 grid of demographic factors
   - Percentage-based comparison showing churn rates
   - Highlights senior citizens and singles as high-risk

3. **exercise_cs2_contract_payment_churn.png**
   - Contract type vs payment method analysis
   - Clearly shows month-to-month contract risk
   - Electronic check payment red flag

4. **exercise_cs2_tenure_analysis.png**
   - Histogram + box plot combination
   - Shows churned customers cluster in 0-10 month range
   - Retained customers spread across longer tenure

5. **exercise_cs2_charges_analysis.png**
   - 4-panel analysis: Monthly and Total charges
   - Histograms and box plots for both
   - Churned customers have higher monthly but lower total charges

6. **exercise_cs2_correlation_matrix.png**
   - Heatmap of numeric feature correlations
   - Tenure shows strongest negative correlation with churn
   - MonthlyCharges shows positive correlation

---

#### Business Recommendations:

**1. CONTRACT INCENTIVE PROGRAM** (Highest Priority):
```
Problem: Month-to-month customers have 42.71% churn
Solution: 
  • Offer 15-20% discount for upgrading to annual contract
  • Provide exclusive perks for 2-year commitments (free upgrades, priority support)
  • Expected impact: Could reduce churn by 50% in month-to-month segment
```

**2. PAYMENT METHOD OPTIMIZATION**:
```
Problem: Electronic check has 45.29% churn (3x higher than auto-pay)
Solution:
  • Investigate: Is payment experience poor? Failed payments?
  • Incentivize automatic payment adoption (5% discount or waived fees)
  • Simplify payment process for electronic check users
```

**3. EARLY INTERVENTION PROGRAM**:
```
Problem: Average churned customer tenure is only 18 months
Solution:
  • Implement 30-60-90 day onboarding checkpoints
  • Proactive outreach to customers in first 6 months
  • Welcome package with value-added services trial
  • Personal account manager for first 3 months
```

**4. SENIOR CITIZEN SUPPORT**:
```
Problem: 41.68% churn among senior citizens
Solution:
  • Dedicated senior support hotline (toll-free, 24/7)
  • Simplified service packages tailored to seniors
  • In-person or video tutorials for service features
  • Senior citizen discount program (10-15% off)
```

**5. FIBER OPTIC SERVICE REVIEW**:
```
Problem: 41.89% churn despite premium pricing
Solution:
  • Customer satisfaction survey for fiber optic users
  • Service quality audit (speed tests, downtime analysis)
  • Review pricing vs competitor offerings
  • May indicate service quality or value perception issues
```

**6. VALUE-ADDED SERVICES BUNDLING**:
```
Problem: Customers without security/support/backup services churn at 40%+
Solution:
  • Bundle OnlineSecurity + TechSupport + Backup as "Peace of Mind" package
  • Include for free in first 3 months, then discounted pricing
  • Gamification: Unlock features based on tenure milestones
```

**7. PRICING STRATEGY ADJUSTMENT**:
```
Problem: $74.44 avg monthly for churned vs $61.27 for retained
Solution:
  • Introduce loyalty discounts after 12/24/36 months
  • Price freeze guarantee for long-term contract holders
  • Transparent pricing (no surprise increases)
```

---

## 📊 Week 7 Seminar

The **Week 7 Seminar** folder continues data preparation and feature engineering using Titanic, house price, and customer churn datasets.

### Introduction: Titanic Dataset

**File**: `Week 7 Seminar/introduction_week_7.py`

This script demonstrates:
- Loading the Titanic dataset from CSV (with a fallback to Seaborn’s built-in dataset)
- Basic dataset inspection and missing-value audit
- A survival-by-class visualization saved to `Week 7 Seminar/visualizations/`

### Case Study 1: House Price Processing

**File**: `Week 7 Seminar/case_study_1/exercise_1_case_study_1_titanic.py`

This exercise applies systematic cleaning and feature engineering:
- Remove rows with >1 missing value
- Drop columns with >33% missing values
- Impute remaining missing values (median/mode)
- Remove outliers in `SalePrice` using IQR
- Apply log transformation to highly skewed numeric features
- Create dummies for categorical variables (≤5 unique values)
- Create YearBuilt period groups and encode as dummies

### Case Study 2: Customer Churn Processing

**File**: `Week 7 Seminar/case_study_2/exercise_1_case_study_2_customer_churn.py`

This exercise builds on last week’s EDA findings:
- Fix `TotalCharges` (empty strings → NaN → numeric)
- Remove rows/columns with excessive missingness
- Impute missing values
- Remove outliers in `MonthlyCharges` and `TotalCharges`
- Apply log transformation to skewed numeric columns
- Create dummies for low-cardinality categorical variables

### Case Study 3: Titanic Dataset Processing

**File**: `Week 7 Seminar/case_study_3/exercise_1_case_study_3_titanic.py`

This exercise implements a robust processing pipeline for the passenger survival dataset:
- Remove rows with >1 missing value
- Drop columns with >33% missingness (e.g., `Cabin`)
- Impute missing values for `Age` (median) and `Embarked` (mode)
- Remove outliers in `Fare` using the IQR method
- Apply log transformation (`np.log1p`) to skewed features like `SibSp`, `Parch`, and `Fare`
- Create dummy variables for `Sex` and `Embarked`
- Feature engineering: Group `Age` into periods (Child, Adult, Senior) and encode as dummies

**File**: `Week 7 Seminar/case_study_3/exercise_2_case_study_3_titanic.py`

This exercise demonstrates the power of Regular Expressions for data extraction:
- Use RegEx pattern `r'^([^,]+),\s*([^.]+)\.\s*(.*)$'` to split the `Name` column
- Extract three distinct components: `Surname`, `Title`, and `FirstName`
- Analyze social status by grouping titles (Mr, Mrs, Miss, Master, and Rare)
- Calculate and visualize survival rates by title group, revealing higher survivability for female titles and young masters


