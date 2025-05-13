import pytest

@pytest.mark.smoke
def test_sample1():
    print("hello")

@pytest.mark.regression
def test_sample2():
    print("world")

@pytest.mark.smoke
@pytest.mark.regression
def test_sample():
    print("Test that is both smoke and regression")