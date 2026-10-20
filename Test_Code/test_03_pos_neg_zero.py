import importlib
pos_neg_zero = importlib.import_module('Code.03_pos_neg_zero').pos_neg_zero

def test_pos_neg_zero():
    assert pos_neg_zero(2) == 'Positive'
    assert pos_neg_zero(-2) == 'Negative'
    assert pos_neg_zero(0) == 'Zero'
