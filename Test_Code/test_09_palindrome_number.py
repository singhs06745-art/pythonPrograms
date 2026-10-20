import importlib
is_palindrome_number = importlib.import_module('Code.09_palindrome_number').is_palindrome_number

def test_is_palindrome_number():
    assert is_palindrome_number(121)
    assert not is_palindrome_number(123)
