import pytest

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (7,49)
])
def test_square(input, expected):
    assert input ** 2 == expected