import pytest
from datetime import date
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.current_date import get_current_date

def test_get_current_date():
    """
    Test that get_current_date returns the current date in correct format.
    """
    current_date = get_current_date()
    
    # Check date format matches YYYY-MM-DD
    assert len(current_date) == 10
    assert current_date[4] == '-'
    assert current_date[7] == '-'
    
    # Verify the date is today's date
    today = date.today().strftime("%Y-%m-%d")
    assert current_date == today