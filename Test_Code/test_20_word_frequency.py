import importlib
word_frequency = importlib.import_module('Code.20_word_frequency').word_frequency

def test_word_frequency():
    assert word_frequency('Hi hi bye') == {'hi': 2, 'bye': 1}
