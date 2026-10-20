import importlib
second_largest = importlib.import_module('Code.15_second_largest').second_largest

def test_second_largest():
    assert second_largest([1, 5, 3, 5]) == 3
