import importlib
fibonacci_series = importlib.import_module('Code.05_fibonacci_series').fibonacci_series

def test_fibonacci_series():
    assert fibonacci_series(5) == [0, 1, 1, 2, 3]
