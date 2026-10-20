import importlib
common_elements = importlib.import_module('Code.17_common_elements').common_elements

def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
