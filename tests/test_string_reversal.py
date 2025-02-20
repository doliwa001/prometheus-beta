import pytest
from src.string_reversal import recursive_reverse_string

def test_basic_string_reversal():
    """Test basic string reversal"""
    assert recursive_reverse_string("hello") == "olleh"
    assert recursive_reverse_string("Python") == "nohtyP"

def test_single_character_string():
    """Test single character strings"""
    assert recursive_reverse_string("a") == "a"
    assert recursive_reverse_string("Z") == "Z"

def test_empty_string():
    """Test empty string"""
    assert recursive_reverse_string("") == ""

def test_string_with_spaces():
    """Test strings containing spaces"""
    assert recursive_reverse_string("hello world") == "dlrow olleh"
    assert recursive_reverse_string("  spaces  ") == "  secaps  "

def test_invalid_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        recursive_reverse_string(123)
    with pytest.raises(TypeError):
        recursive_reverse_string(None)
    with pytest.raises(TypeError):
        recursive_reverse_string(["not", "a", "string"])