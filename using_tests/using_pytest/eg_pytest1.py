# NB you may need to pip install pytest

def test_passing():
    assert(1,2,3) == (1,2,3) # same ordinal values

# def test_failing():
#     assert (1,2,3) == (3,2,1) # different ordinal values

def test_sets():
    assert {1,2,3} == {3,2,1} # set has no ordinal values

def test_true():
    x = True
    y = 1 # only 1 and no other number will evaluate to True
    assert x
    assert x == y