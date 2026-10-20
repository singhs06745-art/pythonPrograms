import importlib
count_vowels_consonants = importlib.import_module('Code.11_vowels_consonants').count_vowels_consonants

def test_count_vowels_consonants():
    assert count_vowels_consonants('Hello') == (2, 3)
