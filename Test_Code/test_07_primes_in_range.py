import importlib
primes_in_range = importlib.import_module('Code.07_primes_in_range').primes_in_range

def test_primes_in_range():
    assert primes_in_range(1, 10) == [2, 3, 5, 7]
