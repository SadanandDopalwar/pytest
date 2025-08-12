import pytest
# We can plan the test input and output using parameterization
@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (10, -5, 5),
    (0, 0, 0)
])
def test_add(x, y, expected):
    assert x + y == expected

@pytest.mark.skip(reason="Skipping this test for now")
def test_skip():
    assert 1 + 1 == 2