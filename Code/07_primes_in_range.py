import importlib
is_prime = importlib.import_module('Code.06_prime_number').is_prime

def primes_in_range(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]
