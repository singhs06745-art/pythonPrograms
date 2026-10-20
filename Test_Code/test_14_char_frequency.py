import importlib
char_frequency = importlib.import_module('Code.14_char_frequency').char_frequency

def test_char_frequency():
    assert char_frequency('aba') == {'a': 2, 'b': 1}
