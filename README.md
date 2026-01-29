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
├── Week 3 Seminar/       # Week 3 seminar exercises
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
