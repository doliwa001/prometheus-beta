def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    """
    # Convert to lowercase and remove whitespace
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # Check if lengths are different
    if len(str1) != len(str2):
        return False
    
    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}
    
    # Count characters in first string
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    # Count characters in second string
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare character frequency dictionaries
    return char_count1 == char_count2