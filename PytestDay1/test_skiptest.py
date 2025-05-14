import pytest
import sys

def test_sample_one():
    print("Test 1: Basic print")
    assert True

def test_sample_two():
    a = 10
    b = 10
    assert a == b

def test_sample_three():
    a = 10
    b = 20
    assert a < b

@pytest.mark.skip(reason="Feature not ready yet")
def test_feature():
    assert True

@pytest.mark.xfail(reason="Bug not fixed yet")
def test_known_bug():
    a = 10
    b = 20
    assert a == b  # Expected to fail

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_feature():
    assert True

@pytest.mark.skip(reason="Skipping for demo")
def test_to_be_skipped():
    assert True
