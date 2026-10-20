import importlib
largest_of_three = importlib.import_module('Code.02_largest_of_three').largest_of_three

def test_largest_of_three():
    assert largest_of_three(2, 9, 4) == 9
