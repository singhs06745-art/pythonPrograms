import importlib
sum_of_digits = importlib.import_module('Code.10_sum_of_digits').sum_of_digits

def test_sum_of_digits():
    assert sum_of_digits(1234) == 10
    assert sum_of_digits(-12) == 3
