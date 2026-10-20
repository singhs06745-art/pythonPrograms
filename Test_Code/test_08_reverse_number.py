import importlib
reverse_number = importlib.import_module('Code.08_reverse_number').reverse_number

def test_reverse_number():
    assert reverse_number(123) == 321
    assert reverse_number(-45) == -54
