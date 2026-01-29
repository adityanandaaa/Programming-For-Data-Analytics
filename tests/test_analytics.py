"""Tests for analytics module."""

import pytest
import pandas as pd
import numpy as np
from src.analytics.stats import calculate_statistics, correlation_analysis


@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing."""
    return pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': ['a', 'b', 'c', 'd', 'e']
    })


def test_calculate_statistics(sample_df):
    """Test statistics calculation."""
    stats = calculate_statistics(sample_df, 'A')
    assert stats['mean'] == 3.0
    assert stats['min'] == 1
    assert stats['max'] == 5


def test_correlation_analysis(sample_df):
    """Test correlation analysis."""
    corr = correlation_analysis(sample_df)
    assert corr.shape == (2, 2)  # Should have numeric columns only
    assert corr.loc['A', 'B'] == 1.0  # Perfect correlation
