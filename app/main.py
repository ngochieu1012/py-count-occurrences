def count_occurrences(phrase: str, letter: str) -> int:
    """
    Counts the number of occurrences of a specific letter in a phrase.
    
    Args:
        phrase (str): The phrase to search within.
        letter (str): The letter to count.
        
    Returns:
        int: The number of times the letter appears in the phrase.
    """
    # ... phần code hiện tại của bạn ...
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    return phrase_lower.count(letter_lower)