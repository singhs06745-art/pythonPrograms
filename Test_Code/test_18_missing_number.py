import importlib
missing_number = importlib.import_module('Code.18_missing_number').missing_number

def test_missing_number():
    assert missing_number([1, 2, 4, 5]) == 3
