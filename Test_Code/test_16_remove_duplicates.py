import importlib
remove_duplicates = importlib.import_module('Code.16_remove_duplicates').remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 1, 3]) == [1, 2, 3]
