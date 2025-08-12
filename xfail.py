import pytest

@pytest.mark.xfail(reason="Known bug: addition is broken")
def test_bug():
    assert 1 + 1 == 3
#Mark a test that is expected to fail — pytest won’t count it as a failure.