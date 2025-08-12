#Fixtures to use again
import pytest

# This is a fixture
@pytest.fixture
def sample_numbers():
    #conn = "FakeConnectionObject"
    #yield conn    #yield is used for cleanup — code after yield runs after the test finishes.
    return [2, 4, 6]

def test_all_even(sample_numbers):
    assert all(num % 2 == 0 for num in sample_numbers)

def test_sum(sample_numbers):
    assert sum(sample_numbers) == 12
