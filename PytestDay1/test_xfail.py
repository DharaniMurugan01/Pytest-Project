import pytest

@pytest.mark.xfail(reason="expected to be failure")
def test_sample1():
    a=10
    b = 10
    assert a != b 

@pytest.mark.xfail(reason="expected to be failure")
def test_sample2():
    a = 10
    b = 10
    assert a == b  

def test_sample3():
    a = "arun"
    b = "arun"
    assert a.__eq__(b)


