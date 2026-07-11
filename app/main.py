def count_occurrences(phrase: str, letter: str) -> int:
    # Convert both to lowercase for case-insensitive comparison
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    # Use count() method - this is the key!
    return phrase_lower.count(letter_lower)
