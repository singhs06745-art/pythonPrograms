def count_vowels_consonants(text):
    vowels = sum(c.lower() in "aeiou" for c in text if c.isalpha())
    consonants = sum(c.isalpha() and c.lower() not in "aeiou" for c in text)
    return vowels, consonants
