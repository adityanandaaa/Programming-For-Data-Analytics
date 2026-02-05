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
│   └── diamonds dataset exercise/   # Diamonds dataset analysis
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

## ✨ Features

- **📈 Data Analysis**: Pandas-based data manipulation and analysis
- **📊 Visualization**: Matplotlib and Seaborn for charts and plots
- **📓 Jupyter Notebooks**: Interactive data exploration
- **🧪 Testing**: Unit tests with pytest
- **📝 Documentation**: Comprehensive code documentation
- **🔄 Data Pipeline**: Extract, Transform, Load (ETL) workflows

## 🛠️ Technologies

- **Python 3.9+**
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Matplotlib**: Visualization
- **Seaborn**: Statistical visualization
- **Jupyter**: Interactive notebooks
- **pytest**: Testing framework

## 📋 Requirements

See `requirements.txt` for complete dependencies.

```
pandas>=2.0.0
numpy>=1.20.0
matplotlib>=3.5.0
seaborn>=0.12.0
jupyter>=1.0.0
pytest>=7.0.0
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
