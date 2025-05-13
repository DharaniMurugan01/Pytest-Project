import pytest
import sys 

def test_sample_one():
    print("hii")
def test_sample_two():
    a=10
    b=10
    assert a==b
def test_sample_three():
    a=10
    b=20
    assert a<b
import pytest

@pytest.mark.skip(reason="Not ready yet")
def test_feature():
    assert True

@pytest.mark.xfail(reason="Bug not fixed")
def test_known_bug():
    a=10
    b=20
    assert a==b

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_feature():
    assert True

@pytest.mark.skip(reason="wrong word")
def test_failes():
    assert 1==1
