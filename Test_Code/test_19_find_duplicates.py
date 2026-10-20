import importlib
find_duplicates = importlib.import_module('Code.19_find_duplicates').find_duplicates

def test_find_duplicates():
    assert find_duplicates([1, 2, 1, 3, 2]) == [1, 2]
