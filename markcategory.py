import pytest

@pytest.mark.slow
def test_large_dataset():
    assert sum(range(1000000)) > 0
#You can group tests into categories (marks) and run them selectively.

#pytest -m slow