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

The **Week 3 Seminar** folder contains exercises focused on **API integration and data retrieval**.

### Exercise: Open Library API Data Retrieval

**File**: `Week 3 Seminar/exercise_week_3_seminar.py`

This exercise demonstrates how to:
- Make HTTP requests to the Open Library API (`https://openlibrary.org/search.json`)
- Use API parameters for searching and pagination:
  - `q`: Search query (keyword or title)
  - `fields`: Specify which fields to retrieve (title, author_name, etc.)
  - `page`: Pagination parameter to fetch multiple pages of results
- Parse JSON responses
- Process and format retrieved data
- Write results to a text file

**Example Usage**:
```bash
cd "Week 3 Seminar"
python exercise_week_3_seminar.py
```

**Output**: 
- Console display of 300 results (pages 1-3) for "Data Science" books
- Saves formatted results to `data_science_results.txt`

**Key Learnings**:
- RESTful API concepts and HTTP requests
- URL encoding and parameter management
- JSON parsing with Python
- Pagination for large result sets
- File I/O operations

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
