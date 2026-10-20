import importlib
is_prime = importlib.import_module('Code.06_prime_number').is_prime

def test_is_prime():
    assert is_prime(7)
    assert not is_prime(1)
    assert not is_prime(9)
