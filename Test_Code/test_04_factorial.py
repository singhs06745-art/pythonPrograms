import importlib
factorial = importlib.import_module('Code.04_factorial').factorial

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
