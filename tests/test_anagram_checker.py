import pytest
from src.anagram_checker import is_anagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True
    assert is_anagram("night", "thing") == True

def test_non_anagrams():
    """Test non-anagram scenarios"""
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False
    assert is_anagram("cat", "dog") == False

def test_case_insensitivity():
    """Test that the function is case-insensitive"""
    assert is_anagram("Debit Card", "Bad Credit") == True
    assert is_anagram("Astronomer", "Moon Starer") == True

def test_whitespace_handling():
    """Test that whitespace is ignored"""
    assert is_anagram("race a car", "racecar") == True
    assert is_anagram("eleven plus two", "twelve plus one") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert is_anagram("", "") == True

def test_single_character():
    """Test single character anagrams"""
    assert is_anagram("a", "a") == True
    assert is_anagram("a", "b") == False

def test_different_lengths():
    """Test strings of different lengths"""
    assert is_anagram("hello", "hello world") == False
    assert is_anagram("short", "shorter") == False