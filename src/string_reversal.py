def recursive_reverse_string(s: str) -> str:
    """
    Recursively reverse a string containing lowercase, uppercase letters, and spaces.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Base case: if string is empty or has single character, return it
    if len(s) <= 1:
        return s
    
    # Recursive case: first character becomes last, recursively reverse rest of string
    return recursive_reverse_string(s[1:]) + s[0]