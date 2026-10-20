import importlib
even_odd = importlib.import_module('Code.01_even_odd').even_odd

def test_even_odd():
    assert even_odd(4) == 'Even'
    assert even_odd(3) == 'Odd'
    assert even_odd(0) == 'Even'
