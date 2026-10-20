import importlib
is_palindrome_string = importlib.import_module('Code.13_palindrome_string').is_palindrome_string

def test_is_palindrome_string():
    assert is_palindrome_string('Madam')
    assert not is_palindrome_string('Hello')
