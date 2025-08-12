import pytest
import sys

@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_only_linux():
    assert True