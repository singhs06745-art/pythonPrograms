import importlib
reverse_string = importlib.import_module('Code.12_reverse_string').reverse_string

def test_reverse_string():
    assert reverse_string('hello') == 'olleh'
